# 1. shell에 'touch .env' 입력
# 2. OPENAI_API_KEY="{API_KEY}" 입력
# 3. pip install python-dotenv

from dotenv import load_dotenv
load_dotenv()
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello world!"}
    ],
)

print(response['choices'][0]['message']['content'])