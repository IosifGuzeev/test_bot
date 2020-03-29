import re
import pandas as pd

path = "C:\\doc_to_txt.txt"

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

qs = re.split("Вопрос [0-9]+", text)[1:]

data = []
for q in qs:
    try:
        q_strings = q.split('\n')
        q_text = q_strings[5]
        q_answ = q_strings[find_answer_ind(q_strings)].split(':')[1]
        q_answ_num = 1
        start, end = find_options_range(q_strings)
        for i in range(0, end - start + 1):
            if q_strings[i + start].find(q_answ) != -1:
                q_answ_num = i
        data.append({'question':q_text.lower(), 'answer_id':q_answ_num, 'answer_text': q_answ[1:].lower()})
    except:
        print("exep")

data.append({'question': "ЗАДАЧИ ПРОФЕССИОНАЛЬНО-ПРИКЛАДНОЙ ФИЗИЧЕСКОЙ ПОДГОТОВКИ".lower(),
             'answer_id': 0,
             'answer_text': "Развитие ведущих для данной профессии способностей".lower()})

df = pd.DataFrame(data)
print(df['question'][31])
df.to_csv("data.csv")
print(df.shape)

