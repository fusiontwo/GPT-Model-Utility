# Q&A based on Fitbit data

from dotenv import load_dotenv
load_dotenv()
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",

    messages=[
        {
            "role": "system",
            "content": "You are a helpful health care expert."
        },
        {
            "role": "user",
            "content": "Kim Jin-soo is 80 years old this year and \
                        has high blood pressure. He is exercising 1,000 steps \
                        today and his heart rate is 85 bpm on average. \
                        Could you please take this into account and \
                        answer the following questions?",
        },
        {
            "role": "assistant",
            "content": "Yes, I will. What is the next question?",
        },
        {
            "role": "user",
            "content": "His deep sleep time is less than 2 hours. \
                        Recommend 3 habits for deep sleep and explain them in detail."
        },
    ]
)

print(response)
print(response['choices'][0]['message']['content'])
