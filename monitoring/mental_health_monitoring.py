from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os
from typing import List

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat_completion(system_role, prompt, model="gpt-4", temperature=0):
    """
    GPT에 프롬프트를 제공하고 응답을 받는 함수.

    Args:
        system_role: GPT 시스템 역할
        prompt: 프롬프트
        model: GPT 모델명
        temperature: 응답의 무작위성 설정 (0은 반복적이고 일관된 답변 생성)

    Returns:
        gpt_response: GPT 모델의 응답
    """
    messages = [{"role": "system", "content": system_role},]
    messages.append({"role": "user", "content":prompt})
    
    res = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )

    gpt_response = res.choices[0].message.content
    return gpt_response


positive_word = []
negative_word = []

def count_pn_word(user_input):
    """
    사용자의 말에서 긍정적 단어와 부정적 단어를 추출하는 함수.
    전역 변수 positive_word, negative_word에 단어를 추가함.

    Args:
        user_input: 사용자의 말
    
    Returns:
        None
    """
    system_role = """당신은 사람의 말로부터 심리를 분석하는 사람입니다.
                     당신의 임무는 UTTERANCE로부터 긍정적 단어와 부정적 단어를 추출하는 것입니다.
                     당신은 지침을 따라야 합니다: DATA_FORMAT."""
    data_format = {"긍정": ["단어1", "단어2", "단어3"], "부정": ["단어1", "단어2", "단어3"]}
    prompt = f'UTTERANCE: {user_input}\nDATA_FORMAT: {data_format}'
    response = chat_completion(system_role, prompt)
    json_response = eval(response)
    positive_word.extend(json_response.get("긍정", []))
    negative_word.extend(json_response.get("부정", []))


def daily_emotion(user_context: List[str], length: int, style: str):
    """
    하루 동안 느낀 기분을 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 마음 건강 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""
    print("*** 하루 동안 느낀 기분 파악 ***")
    print("챗봇: 안녕하세요 어르신~ 오늘 기분이 어떠신가요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def happiness(user_context: List[str], length: int, style: str):
    """
    행복감을 주는 요소를 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 마음 건강 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""
    print("*** 행복감을 주는 요소 파악 ***")
    print("챗봇: 오늘 하루 중 가장 행복했던 순간을 떠올려주실 수 있나요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)

    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def stress(user_context: List[str], length: int, style: str):
    """
    스트레스 요인을 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 마음 건강 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""
    print("*** 스트레스 요인을 파악 ***")
    print("챗봇: 안녕하세요 어르신~ 오늘 특별히 힘들었던 순간이나 걱정되었던 일이 있으셨나요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)

    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def main():
    daily_emotion(["70세", "여성"], 20, "친밀한 대화")
    happiness(["80세", "남성"], 20, "친밀한 대화")
    stress(["60세", "여성"], 20, "친밀한 대화")

    print("Positive word: ", positive_word)
    print("Negative word: ", negative_word)

if __name__ == "__main__":
    main()