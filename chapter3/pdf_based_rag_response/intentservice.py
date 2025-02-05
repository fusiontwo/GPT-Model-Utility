from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class IntentService():
     def __init__(self):
        pass
     
     def get_intent(self, user_question: str):
         # call the openai ChatCompletion endpoint
         response = client.chat.completions.create(model="gpt-4o",
         messages=[
               {"role": "user", "content": f'Extract the keywords from the following question: {user_question}'+
                 'Do not answer anything else, only the keywords.'}
            ])

         # extract the response
         return (response.choices[0].message.content)