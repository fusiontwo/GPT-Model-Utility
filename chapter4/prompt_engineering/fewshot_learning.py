from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_completion(prompt, model="gpt-4", temperature=0):
    res = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content":prompt}],
        temperature=temperature,
    )
    print(res.choices[0].message.content)
	
prompt = """
I go home --> 😊 go 🏠
my dog is sad --> my 🐶 is 😞
I run fast --> 😊 run ⚡
I love my wife --> 😊 ❤️ my wife
the girl plays with the ball --> the 👧 🎮 with the 🏀
The boy writes a letter to a girl --> 
"""

chat_completion(prompt)