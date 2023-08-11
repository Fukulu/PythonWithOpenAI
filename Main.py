import openai
import asyncio
import pandas as pd

openai.api_key = "Your API KEY"

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                               messages=[{"role": "user", "content": "Hello Chat GPT How Are You"}])

print(chat_completion.choices[0].message.content)

df = pd.read_csv("Example.csv")
df = pd.read_csv("Example.csv", delimiter=';', skiprows=0, low_memory=False)
df.head()

def ask_gpt(word):
    prompt = f"Lütfen bundan sonra sana verdiğim almanca kelimeyi belirttiğim formatta aralarına ; koyarak tek bir satırda olacak şekilde bana cevap verebilir misin? işte formatın örneği: (almanca kelime);(Türkçe karşılığı);(İngilizce Karşılığı);(Almanca kelimenin yer aldığı Cümle);(Cümlenin Türkçesi);(Cümlenin İngilizcesi) sana verdiğim kelime ise {word}"
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                               messages=[{"role": "user", "content": prompt}])
    return chat_completion.choices[0].message.content


for i in range(0, 10):
        answer = ask_gpt(df.loc[i]["wordDe"])
        await asyncio.sleep(5)
        ans_list = answer.split(sep=';')
        await asyncio.sleep(2)
        ans_list[1] = ans_list[1].capitalize()
        ans_list[2] = ans_list[2].capitalize()
        await asyncio.sleep(2)
        df.loc[i, "wordTr"] = ans_list[1]
        df.loc[i, "wordEn"] = ans_list[2]
        df.loc[i, "sentence"] = ans_list[3]
        df.loc[i, "sentenceTr"] = ans_list[4]
        df.loc[i, "sentenceEn"] = ans_list[5]
        await asyncio.sleep(1)


df.loc[2:12]
df.iloc[2]
df.iloc[20]

for i in range(10, 19):
        answer = ask_gpt(df.loc[i]["wordDe"])
        await asyncio.sleep(5)
        ans_list = answer.split(sep=';')
        await asyncio.sleep(2)
        ans_list[1] = ans_list[1].capitalize()
        ans_list[2] = ans_list[2].capitalize()
        await asyncio.sleep(2)
        df.loc[i, "wordTr"] = ans_list[1]
        df.loc[i, "wordEn"] = ans_list[2]
        df.loc[i, "sentence"] = ans_list[3]
        df.loc[i, "sentenceTr"] = ans_list[4]
        df.loc[i, "sentenceEn"] = ans_list[5]
        await asyncio.sleep(1)


df.loc[10:19]
df.iloc[18]

df.to_csv("ExampleV2.csv", index=False)

