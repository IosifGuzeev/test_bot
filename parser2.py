import re
import pandas as pd

path = "test_3.txt"

with open(path, encoding='utf-8') as f:
    text = ' '.join(f.readlines())


def find_options_range(text):
    start = 0
    while text[start].find("Выберите один ответ:") == -1:
        start += 1
    end = start + 1
    while text[end].find("Отзыв") == -1:
        end += 1
    return start + 1, end

def find_answer_ind(text):
    ind = 0
    while text[ind].find("Правильный ответ:") == -1:
        ind += 1
    return ind

def find_q_id(text):
    ind = 0
    while text[ind].find("Текст вопроса") == -1:
        ind += 1
    return ind + 1

qs = re.split("Вопрос [0-9]+", text)[1:]

data = []
for q in qs:
    try:
        q_strings = q.split('\n')
        q_text = q_strings[find_q_id(q_strings)]
        q_answ = q_strings[find_answer_ind(q_strings)].split(':')[1]
        q_answ_num = 1
        start, end = find_options_range(q_strings)
        for i in range(0, end - start + 1):
            if q_strings[i + start].find(q_answ) != -1:
                q_answ_num = i
        data.append({'question':q_text.lower(), 'answer_id':q_answ_num, 'answer_text': q_answ[1:].lower()})
    except:
        print("exep")

df = pd.DataFrame(data)
print(df[['question', 'answer_text']])
df.to_csv("data3.csv")
print(df.shape)


