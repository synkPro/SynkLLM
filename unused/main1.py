from google.cloud import aiplatform
import json

# 1. Load schema from a JSON config file
def load_schema(file_path="schema_config.json"):
    with open(file_path, "r") as f:
        return json.load(f)

# 2. Generate prompt from schema
def generate_prompt(schema):
    prompt = "You are a helpful assistant for managing tasks, events, and reminders.\n"
    prompt += "Based on the following schema, convert user input into structured JSON.\n\n"
    for entity, definition in schema.items():
        prompt += f"Entity: {entity}\n"
        for field, value in definition['fields'].items():
            if isinstance(value, list):
                prompt += f"  - {field}: one of {value}\n"
            else:
                prompt += f"  - {field}: {value}\n"
        prompt += "\n"

    prompt += """
Return output in this format:
{
  "intent": "<get_<entity> | create_<entity> | update_<entity> | delete_<entity>>",
  "entity": "<task | event | reminder>",
  "data": { ... },      // For create/update
  "filters": { ... }    // For read/delete
}
"""
    return prompt

# 3. Send prompt + user input to Gemini model
def call_gemini(system_prompt, user_input, project, location="us-central1", model="gemini-1.5-pro-preview-0409"):
    aiplatform.init(project=project, location=location)

    model = aiplatform.LanguageModel(model=model)

    response = model.predict(
        instances=[
            {
                "messages": [
                    {"author": "system", "content": system_prompt},
                    {"author": "user", "content": user_input}
                ]
            }
        ],
        parameters={
            "temperature": 0.4,
            "maxOutputTokens": 1024,
        }
    )

    return response.predictions[0]["candidates"][0]["content"]

# 4. Run everything
if __name__ == "__main__":
    PROJECT_ID = "your-gcp-project-id"  # 🔁 Change this

    schema = load_schema("schema_config.json")
    prompt = generate_prompt(schema)

    user_question = input("Ask something to your assistant: ")
    output = call_gemini(prompt, user_question, project=PROJECT_ID)

    print("\nLLM Response:")
    print(output)
