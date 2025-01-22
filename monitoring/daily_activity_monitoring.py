from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os
from typing import List
from datetime import datetime

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


def current_meal():
    """
    현재 시간에 따라 아침, 점심, 저녁 문자열을 반환하는 함수.

    Args:
        None

    Returns: 
        meal: 현재 시간이 속하는 범주 (아침, 점심, 저녁)
    """
    current_time = datetime.now().time()

    if current_time.hour < 11:  # 00:00 ~ 10:59
        meal = "아침"
    elif current_time.hour < 17:  # 11:00 ~ 16:59
        meal = "점심"
    else:  # 17:00 ~ 23:59
        meal = "저녁"

    return meal


def meal_status(user_context: List[str], length: int, style: str):
    """
    현재 시간에 따라 아침, 점심, 저녁 식사 여부를 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     현재는 MEAL 식사 시간입니다.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    meal = current_meal()

    print("*** 식사 여부 파악 ***")
    print(f"챗봇: 안녕하세요 어르신~ {meal} 식사는 하셨나요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\nMEAL: {meal}'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def meal_amount(user_context: List[str], length: int, style: str):
    """
    현재 시간에 따라 아침, 점심, 저녁 식사량을 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     현재는 MEAL 식사 시간입니다.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    meal = current_meal()

    print("*** 식사 여부 파악 ***")
    print(f"챗봇: {meal} 식사는 알맞은 양으로 드셨나요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\nMEAL: {meal}'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def meal_time(user_context: List[str], length: int, style: str):
    """
    현재 시간에 따라 아침, 점심, 저녁 식사 시간을 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     현재는 MEAL 식사 시간입니다.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    meal = current_meal()

    print("*** 식사 시간 파악 ***")
    print(f"챗봇: {meal}은 식사 시간에 맞게 드셨나요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\nMEAL: {meal}'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def daily_activity(user_context: List[str], length: int, style: str):
    """
    오늘 수행한 주요 활동을 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    print("*** 하루 주요 활동 파악 ***")
    print(f"챗봇: 오늘은 무엇을 하셨나요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\n'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def goal_achievement(user_context: List[str], length: int, style: str):
    """
    오늘의 목표 달성 여부를 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    print("*** 오늘의 목표 달성 여부 파악 ***")
    print(f"챗봇: 오늘 하루의 목표를 이루셨나요? 목표를 이루는 데 어떤 점이 도움이 되셨나요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\n'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def next_day_plan(user_context: List[str], length: int, style: str):
    """
    내일 활동 계획을 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    print("*** 내일 활동 계획 파악 ***")
    print(f"챗봇: 내일은 어떤 활동을 해보고 싶으신가요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\n'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def relationship(user_context: List[str], length: int, style: str):
    """
    인간 관계(자주 만나는 사람)를 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    print("*** 인간 관계 (자주 만나는 사람) 파악 ***")
    print(f"챗봇: 요새 어떤 사람을 가장 자주 만나시나요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\n'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def sleep_quality_condition(user_context: List[str], length: int, style: str):
    """
    수면의 질과 사용자의 컨디션을 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    print("*** 수면의 질과 사용자의 컨디션 파악 ***")
    print(f"챗봇: 어젯밤 잘 주무셨나요? 기분이 어떠신가요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\n'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def sleep_influencing_factor(user_context: List[str], fitbit_sleep: str, length: int, style: str):
    """
    수면 데이터를 바탕으로 수면에 영향을 미치는 요인을 파악하는 함수.

    Args:
        user_context: 사용자 정보
        fitbit_sleep: Fitbit의 수면 데이터
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     사용자의 수면 데이터 FITBIT_SLEEP을 고려하십시오.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    print("*** 수면 데이터를 바탕으로 수면 영향 요인 파악 ***")
    print(f"챗봇: 오늘 수면 데이터를 고려했을 때, 잘 못 주무신 것 같네요. 무슨 일이 있으신가요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nFITBIT_SLEEP: {fitbit_sleep}\nLENGTH: {length}\nSTYLE: {style}\n'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def exercise_enjoy(user_context: List[str], length: int, style: str):
    """
    운동할 때 즐거운 점을 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    print("*** 운동할 때 즐거운 점 파악 ***")
    print(f"챗봇: 오늘 운동 중에 가장 즐거웠던 순간은 무엇인가요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\n'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def exercise_challenge(user_context: List[str], length: int, style: str):
    """
    운동할 때 힘든 점을 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    print("*** 운동할 때 힘든 점 파악 ***")
    print(f"챗봇: 오늘 운동을 하면서 특별히 힘들었던 점이 있으셨나요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\n'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def mission_failure_reason(user_context: List[str], length: int, style: str):
    """
    미션을 달성하지 못한 이유를 파악하는 함수.

    Args:
        user_context: 사용자 정보
        length: 응답 단어 수
        style: 응답 스타일

    Returns: 
        None
    """
    system_role = """당신은 노인을 위한 일일 활동 비서입니다.
                     당신의 임무는 USER_CONTEXT를 바탕으로 대화를 하는 것입니다.
                     미션 달성을 부드럽게 권유하고 동기 부여 해야 합니다.
                     당신은 지침을 따라야 합니다: LENGTH, STYLE.
                     사용자를 부르는 호칭은 '어르신'입니다."""

    print("*** 미션을 달성하지 못한 이유 파악 ***")
    print(f"챗봇: 일일 미션을 아직 안 하셨는데, 혹시 이유가 있으신가요?")
    
    print("어르신: ", end="")
    user_message = input()
    count_pn_word(user_message)
    
    prompt = f'{user_message}\nUSER_CONTEXT: {user_context}\nLENGTH: {length}\nSTYLE: {style}\n'
    response = chat_completion(system_role, prompt)
    print("챗봇: ", response)


def main():
    # 식사 패턴 파악
    meal_status(["70세", "여성"], 20, "친밀한 대화")
    meal_amount(["70세", "여성"], 20, "친밀한 대화")
    meal_time(["70세", "여성"], 20, "친밀한 대화")

    # 일상 생활 파악
    daily_activity(["85세", "남성"], 20, "친밀한 대화")
    goal_achievement(["85세", "남성"], 20, "친밀한 대화")
    next_day_plan(["85세", "남성"], 20, "친밀한 대화")
    relationship(["85세", "남성"], 20, "친밀한 대화")

    # 수면 상태 파악
    sleep_quality_condition(["85세", "남성"], 20, "친밀한 대화")
    sleep_influencing_factor(["85세", "남성", "불면증 환자"], "{수면 점수: 45점, deep: 1시간, light: 3시간, rem: 1시간, wake: 15분}", 20, "친밀한 대화")

    # 운동 소감 파악
    exercise_enjoy(["60세", "여성"], 20, "친밀한 대화")
    exercise_challenge(["60세", "여성"], 20, "친밀한 대화")

    # 데일리 미션 달성 파악
    mission_failure_reason(["75세", "남성"], 20, "친밀한 대화")

    # 긍정 / 부정 단어 목록
    print("Positive word: ", positive_word)
    print("Negative word: ", negative_word)

if __name__ == "__main__":
    main()