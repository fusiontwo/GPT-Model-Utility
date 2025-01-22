from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read the transcript from the file
with open("chapter3/transcript.txt", "r") as f:
    transcript = f.read()

# Call the openai ChatCompletion endpoint, with the ChatGPT model
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user",
               "content": f"다음 비디오 스크립트를 요약해줘.: \n{transcript}"}])


print(response.choices[0].message.content)