import openai

openai.api_key = "{INSERT_MY_API_KEY}"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello world!"}
    ],
)

print(response['choices'][0]['message']['content'])