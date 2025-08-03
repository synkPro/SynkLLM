import google.generativeai as genai
import json
from utils.cleaner import safe_parse
import os

genai.configure(api_key="AIzaSyDHMETZZJxn-M62u7DVO004g0c3BjOUUJE")

with open("schema/schema.json") as f:
    SCHEMA = json.load(f)

with open("prompts/prompt.txt") as f:
    PROMPT_TEMPLATE = f.read()

formatted_schema = json.dumps(SCHEMA, indent=2)
SYSTEM_PROMPT = PROMPT_TEMPLATE.replace("{SCHEMA}", formatted_schema)
#SYSTEM_PROMPT += f"\n\nUser: {user_input}"


model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[{"role": "user", "parts": [SYSTEM_PROMPT]}])

def get_structured_output(user_input):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = chat.send_message(user_input)
    print("\nLLM Response:" + response.text)
    return safe_parse(response.text)
