import os
import google.generativeai as genai
import json
import re

# Access the API key
genai.configure(api_key="AIzaSyDHMETZZJxn-M62u7DVO004g0c3BjOUUJE")

# Define the schema-aware prompt with few-shot examples
system_prompt = """
You are an assistant for managing tasks, events, and reminders.

You will receive user inputs and must extract structured information as JSON.

Schema:
- task: title (string), description (string), due_date (YYYY-MM-DD), priority (low/medium/high), status (pending/done)
- reminder: message (string), remind_at (YYYY-MM-DDTHH:MM)
- event: title (string), start_time (YYYY-MM-DDTHH:MM), end_time (YYYY-MM-DDTHH:MM), location (string)

Respond ONLY in JSON format like:
{
  "intent": "create_task",
  "entity": "task",
  "data": {
    "title": "Submit report",
    "due_date": "2025-08-02",
    "priority": "high"
  },
  "filters": {}
}

DO NOT include any explanation. Only return a JSON object.

Examples:

User: Remind me to pay the electricity bill at 6 PM today.
{
  "intent": "create_reminder",
  "entity": "reminder",
  "data": {
    "message": "pay the electricity bill",
    "remind_at": "2025-08-01T18:00"
  },
  "filters": {}
}

User: What are my tasks due tomorrow?
{
  "intent": "get_task",
  "entity": "task",
  "data": {},
  "filters": {
    "due_date": "2025-08-02"
  }
}

User: Schedule an event called Project Kickoff at 11 AM on Monday at conference room 2.
{
  "intent": "create_event",
  "entity": "event",
  "data": {
    "title": "Project Kickoff",
    "start_time": "2025-08-05T11:00",
    "end_time": "2025-08-05T12:00",
    "location": "conference room 2"
  },
  "filters": {}
}
"""

# Get user input
user_input = input("Your message to the assistant: ")

# Send to Gemini with few-shot setup
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[{"role": "user", "parts": [system_prompt]}])
response = chat.send_message(user_input)
raw_output = response.text.strip()

# Remove triple backticks if present
if raw_output.startswith("```"):
    # Extract content between ```json and ```
    match = re.search(r"```(?:json)?\s*(.*?)```", raw_output, re.DOTALL)
    if match:
        raw_output = match.group(1).strip()


# Parse and print structured JSON response
print("\nRaw LLM output:\n", response.text)
print("\nRaw LLM output:\n", raw_output)

try:
    structured = json.loads(raw_output)
    print("\n Structured JSON:")
    print(json.dumps(structured, indent=2))
except json.JSONDecodeError:
    print("\n Couldn't parse JSON. Here's the raw output:")
    print(raw_output)

