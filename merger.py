import pandas as pd

path1 = 'data.csv'
path2 = 'data2.csv'
df1 = pd.read_csv('data.csv')[['answer_id', 'answer_text', 'question']]
df2 = pd.read_csv('data2.csv')[['answer_id', 'answer_text', 'question']]
df3 = pd.read_csv('data3.csv')[['answer_id', 'answer_text', 'question']]
updated_df = df1.append(df2).append(df3)
print(updated_df.shape)
updated_df = updated_df.drop_duplicates(subset ="question")
print(updated_df.shape)
updated_df.to_csv("new_data_(123).csv")