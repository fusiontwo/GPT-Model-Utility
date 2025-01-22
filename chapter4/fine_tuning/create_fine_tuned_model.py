from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Fine-tuning
def create_fine_tuned_model():
    client.fine_tuning.jobs.create(
        training_file="file-LN7kmVrVMd57a4Ryv8ACeA",
        model="gpt-3.5-turbo",
        # validation_file="",
        suffix="marketing-data"
    )

# Show List of Fine-tuning task 
def fined_tuned_list():
    fined_tuned_list = client.fine_tuning.jobs.list()
    print(fined_tuned_list)

# Stop Fine-tuning task
def stop_fine_tuning(finetuing_id):
    client.fine_tuning.jobs.cancel(finetuing_id)

# Delete Fine-tuned model
def delete_fine_tuning(finetuing_id):
    client.models.delete(finetuing_id)

# Fine-tuning & Show List of Fine-tuning task 
# create_fine_tuned_model()
fined_tuned_list()

# # Stop Fine-tuning task & Show List of Fine-tuning task 
# stop_fine_tuning("")
# fined_tuned_list()

# Delete Fine-tuned model & Show List of Fine-tuning task 
# delete_fine_tuning("")
# fined_tuned_list()