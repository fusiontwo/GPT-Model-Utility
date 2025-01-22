from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_completion(prompt, model="gpt-4o", temperature=0):
    res = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content":prompt}],
        temperature=temperature,
    )
    print(res.choices[0].message.content)

basic_prompt = "How much is 369 * 1235?"
cot_prompt = "How much is 369 * 1235 ? Let's think step by step."

print("[Basic prompt]\n")
chat_completion(basic_prompt)
print("\n[Cot prompt]\n")
chat_completion(cot_prompt)