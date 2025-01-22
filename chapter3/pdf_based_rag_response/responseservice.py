from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ResponseService():
     def __init__(self):
        pass
     
     def generate_response(self, facts, user_question):
         response = client.chat.completions.create(model="gpt-4o",
         messages=[
               {"role": "user", "content": 'Based on the FACTS, give an answer to the QUESTION.'+ 
                f'QUESTION: {user_question}. FACTS: {facts}'}
            ])

         # extract the response
         return (response.choices[0].message.content)