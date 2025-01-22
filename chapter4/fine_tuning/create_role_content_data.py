from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os
import pandas as pd
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_completion(prompt, model="gpt-4", temperature=0):
    res = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return res.choices[0].message.content.strip()

l_sector = ['Grocery Stores', 'Restaurants', 'Fast Food Restaurants', 'Pharmacies', 'Service Stations (Fuel)', 'Electronics Stores']
l_city = ['Brussels', 'Paris', 'Berlin']
l_size = ['small', 'medium', 'large']

f_prompt = """ 
Role: You are an expert content writer with extensive direct marketing experience. You have strong writing skills, creativity, adaptability to different tones and styles, and a deep understanding of audience needs and preferences for effective direct campaigns.
Context: You have to write a short message in maximum 2 sentences for a direct marketing campaign to sell a new e-commerce payment service to stores. 
The target stores have the three following characteristics:
- The sector of activity: {sector}
- The city where the stores are located: {city} 
- The size of the stores: {size}
Task: Write the short message for the direct marketing campaign. To write this message, use your skills defined in your role! It is very important that the messages you produce take into account the product you want to sell and the characteristics of the store you want to write to.
"""

data = []

for sector in l_sector:
    for city in l_city:
        for size in l_size:
            for i in range(3):
                prompt = f_prompt.format(sector=sector, city=city, size=size)
                response_txt = chat_completion(prompt, model='gpt-3.5-turbo', temperature=1)
                
                message = {
                    "messages": [
                        {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
                        {"role": "user", "content": prompt.strip()},
                        {"role": "assistant", "content": response_txt.strip()}
                    ]
                }
                data.append(message)
                print(message)  # LOG

jsonl_filename = "role_content_marketing_data.jsonl"
with open(jsonl_filename, "w", encoding="utf-8") as jsonl_file:
    for entry in data:
        jsonl_file.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"JSONL 파일 생성 완료: {jsonl_filename}")
