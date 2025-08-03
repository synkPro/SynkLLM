from llm.processor import get_structured_output
from crud.handler import handle_request

def main():
    print("🤖 TaskBot is ready. Type your command:")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        parsed = get_structured_output(user_input)
        if not parsed:
            print("⚠️ Could not understand. Try again.")
            continue

        intent = parsed.get("intent")
        entity = parsed.get("entity")
        data = parsed.get("data", {})
        filters = parsed.get("filters", {})

        response = handle_request(intent, entity, data, filters)
        print("Response:", response)

if __name__ == "__main__":
    main()
