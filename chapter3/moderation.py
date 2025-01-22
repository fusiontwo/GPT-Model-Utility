from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Call the openai Moderation endpoint, with the text-moderation-latest model
response = client.moderations.create(
    model="text-moderation-latest",
    input="I want to kill my neighbor."
)

# Extract the response
print(response)

formatted_json = json.dumps(response.dict(), indent=4, ensure_ascii=False)
print(formatted_json)