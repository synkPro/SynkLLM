import re
import json

def extract_json(text):
    text = text.strip()
    if text.startswith("```"):
        match = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
        if match:
            text = match.group(1).strip()
    return text

def safe_parse(text):
    try:
        return json.loads(extract_json(text))
    except json.JSONDecodeError:
        return None
