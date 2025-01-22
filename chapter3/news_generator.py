from dotenv import load_dotenv
load_dotenv()
from typing import List
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_chatgpt(messages):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=messages)
    return (response.choices[0].message.content)


# prompt_role = '''You are an assistant for journalists. 
# Your task is to write articles, based on the FACTS that are given to you. 
# You should respect the instructions: the TONE, the LENGTH, and the STYLE'''

prompt_role = '''당신은 노인을 위한 건강 비서입니다. 
당신의 임무는 제공된 FACTS를 바탕으로 조언을 제공하는 것입니다. 
당신은 지침을 따라야 합니다: TONE, LENGTH, STYLE.'''


def assist_journalist(
        facts: List[str],
        tone: str, length_words: int, style: str):
    facts = ", ".join(facts)
    prompt = f'{prompt_role}\nFACTS: {facts}\nTONE: {tone}\nLENGTH: {length_words} words\nSTYLE: {style}'
    return ask_chatgpt([{"role": "user", "content": prompt}])


# print(
#     assist_journalist(
#         ['The sky is blue', 'The grass is green'],
#         'informal', 100, 'blogpost'))

print(
    assist_journalist(
        ['노인은 불면증 환자', '깊은 수면이 부족한 상태'],
        '공식적인', 150, '친밀한 대화'))