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

# Simple question
prompt1 = "Give me a suggestion for the main course for today's lunch."

# Context + Task
prompt2 = """
Context: I do 2 hours of sport a day. I am vegetarian, and I don't like green 
vegetables. I am conscientious about eating healthily. 
Task: Give me a suggestion for a main course for today's lunch."""

# Context + Task(Request additional questions)
prompt3 = """
Context: I do 2 hours of sport a day. I am vegetarian and I don't like green 
vegetables. I am very careful to eat healthily.
Task: Give me a suggestion for a main course for today's lunch?
Do not perform the requested task! Instead, can you ask me questions about the 
context so that when I answer, you can perform the requested task more
efficiently?
"""

# Context + Task(Request table)
prompt4 = """
Context: I do 2 hours of sport a day. I am vegetarian, and I don't like green 
vegetables. I am conscientious about eating healthily.
Task: Give me a suggestion for a main course for today's lunch.
With this suggestion, I also want a table with two columns where each row 
contains an ingredient from the main course.
The first column in the table is the name of the ingredient.
The second column of the table is the number of grams of that ingredient needed 
for one person. Do not give the recipe for preparing the main course.
"""

# Role + Context + Task
prompt5 = """
Role: You are a nutritionist designing healthy diets for high-performance athletes. You take into account the nutrition needed for a good recovery.
Context: I do 2 hours of sport a day. I am vegetarian, and I don't like green vegetables. I am conscientious about eating healthily.
Task: Based on your expertise defined in your role. Give me a suggestion for a main course for today's lunch. 
With this suggestion, I also want a table with two columns where each row in the table contains an ingredient from the main course.
The first column in the table is the name of the ingredient.
The second column of the table is the number of grams of that ingredient needed for one person. 
Do not give the recipe for preparing the main course.
"""

for i in range(5):
    # globals(): Converts all global variables into a dictionary format 
    # It enables dynamic use of variable names.
    prompt = globals()[f"prompt{i+1}"]  
    print(f"[Prompt {i+1}]")
    chat_completion(prompt)