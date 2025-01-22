from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def upload_file(upload_file):
    # Upload file
    client.files.create(
        file=open(upload_file, "rb"),
        purpose="fine-tune")

def delete_file(file):
    # Delete file
    client.files.delete(file)

def file_list():
    # Show uploaded file list
    file_list = client.files.list()
    print(file_list)

# Upload file & Show a list of files
upload_file("./chapter4/fine_tuning/role_content_marketing_data.jsonl")
file_list()

# Delete file
# delete_file("file-A43QCWmeWp2hQe46HtS24q")
# file_list()