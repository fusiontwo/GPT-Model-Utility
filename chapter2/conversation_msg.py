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
            "content": "You are a helpful teacher."
        },
        {
            "role": "user",
            "content": "Are there other measures than time complexity for an \
                        algorithm?",
        },
        {
            "role": "assistant",
            "content": "Yes, there are other measures besides time complexity \
                        for an algorithm, such as space complexity.",
        },
        {
            "role": "user",
            "content": "What is it?"
        },
    ]
)

print(response)
print(response['choices'][0]['message']['content'])
