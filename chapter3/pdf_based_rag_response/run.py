from dotenv import load_dotenv

load_dotenv()
from intentservice import IntentService
from responseservice import ResponseService
from dataservice import DataService

# Example pdf
pdf = './2025_konkuk.pdf'

data_service = DataService()

# Drop all data from redis if needed
data_service.drop_redis_data()

# Load data from pdf to redis
data = data_service.pdf_to_embeddings(pdf)

data_service.load_data_to_redis(data)

intent_service = IntentService()
response_service = ResponseService()

# Question 
question = 'KU자유전공학부 단과대별 선발 정원을 각각 알려주고, 선발 방식에 대해 설명해줄래?'
# Get the intent
intents = intent_service.get_intent(question)
# Get the facts
facts = data_service.search_redis(intents)
# Get the answer
answer = response_service.generate_response(facts, question)
print(answer)
