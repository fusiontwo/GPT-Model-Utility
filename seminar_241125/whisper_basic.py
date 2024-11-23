from dotenv import load_dotenv
load_dotenv()
import openai
import whisper
import os
import gradio as gr

openai.api_key = os.getenv("OPENAI_API_KEY")

model = whisper.load_model("base")

def transcribe(file):
    if not os.path.exists(file):
        return "파일을 찾을 수 없습니다."
    transcription = model.transcribe(file, language="ko")
    if not transcription:
        return "오디오 변환에 실패했습니다."

    return transcription["text"]

def generate_answer(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    return response["choices"][0]["message"]["content"]

prompts = {
    "START": "Classify the intent of the next input. \
            Is it: WRITE_EMAIL, QUESTION, OTHER ? Only answer one word.",
    "QUESTION": "If you can answer the question: ANSWER, \
                 if you need more information: MORE, \
                 if you cannot answer: OTHER. Only answer one word.",
    "ANSWER": "Now answer the question",
    "MORE": "Now ask for more information",
    "OTHER": "Now tell me you cannot answer the question or do the action",
    "WRITE_EMAIL": 'If the subject or recipient or message is missing, \
                    answer "MORE". Else if you have all the information, \
                    answer "ACTION_WRITE_EMAIL |\
                    subject:subject, recipient:recipient, message:message".',
}

actions = {
    "ACTION_WRITE_EMAIL": "The mail has been sent. \
    Now tell me the action is done in natural language."
}

def do_action(action):
    print("Doing action " + action)
    return ("I did the action " + action)

def discussion(messages, last_step):
    answer = generate_answer(messages)
    if answer in prompts.keys():
        messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": prompts[answer]})
        return discussion(messages, answer)
    elif answer in actions.keys():
        do_action(answer)
    else:
        if last_step != 'MORE':
            messages=[]
        last_step = 'END'
        return answer

def start(user_input):
    messages = [{"role": "user", "content": prompts["START"]}]
    messages.append({"role": "user", "content": user_input})
    return discussion(messages, "")

def start_chat(file):
    input = transcribe(file)
    return start(input)

gr.Interface(
    fn=start_chat,
    live=True,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
).launch()
