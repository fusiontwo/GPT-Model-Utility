from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_completion(prompt, model, temperature=0):
    res = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=temperature,
        stop="\n"
    )
    return res
    # return res.choices[0].message.content.strip()

response = chat_completion("Hotel, New York, small ->",
                "ft:gpt-3.5-turbo-0125:personal:marketing-data:Ap9vSrlW")

print(response)