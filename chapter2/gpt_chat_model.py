from dotenv import load_dotenv
import openai
import os

# Load OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set system message
messages = [
    {"role": "system", "content": "당신은 사용자 건강 데이터를 기반으로 정확하고 구체적인 조언을 제공하는 헬스케어 전문가입니다."},
]

print("\n음성채팅봇 시작 (종료하려면 '종료'라고 입력하세요.)\n")

while True:
    # Get user input
    user_input = input("사용자: ").strip()
    
    if user_input.strip().lower() == "종료":
        print("채팅을 종료합니다.")
        break

    # Add user input
    messages.append({"role": "user", "content": user_input})

    # Call ChatCompletion API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Add assistant's response
        assistant_response = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": assistant_response})

        # Print response
        print(f"\n음성채팅봇: {assistant_response}\n")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
