# 📘 LLM-Based Smart Task Assistant

This project is a chatbot-based assistant that takes user input (in natural language), parses the prompt using Google's **Generative AI (Gemini)**, identifies the intent and data, and performs **CRUD operations** on a structured **database (DB)** for tasks, events, and reminders.

---

## ✅ Features

- Uses **Google Generative AI (Gemini)** to extract structured data from user prompts.
- Interprets and classifies user intent using a schema-aware prompt.
- Performs **Create / Read / Update / Delete** operations on a relational database (planned).
- Modular project structure with clearly separated concerns:
  - Prompt Templates
  - Schema (ER model)
  - LLM logic
  - CRUD handling (DB interaction)
  - API (to be implemented next)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd your-repo-folder
```

### 2. Set Up Python Virtual Environment

```bash
python3 -m venv llm-env
source llm-env/bin/activate
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

If you face a missing dependency error, install the missing package manually using `pip install`.

### 4. Set Your Google API Key

This project uses Google's Gemini model, which requires an API key.

**Options:**

**Recommended (Environment Variable):**

```bash
export GOOGLE_API_KEY="your_api_key"
```

Alternatively: Configure it directly in your `processor.py` (not recommended for production).

---

## 📁 Project Structure

```
your-project/
│
├── main.py                      # Entry point: receives user input, calls LLM, routes response
│
├── /schema/
│   └── schema.json              # Contains full DB schema (fields for task, reminder, event)
│
├── /prompts/
│   └── prompt.txt               # Base prompt template (with SCHEMA placeholder)
│
├── /llm/
│   ├── processor.py             # Handles Gemini setup, prompt formatting, and parsing response
│   └── prompt_builder.py        # Loads schema and builds full prompt
│
├── /handlers/
│   └── crud_handler.py          # Will contain DB CRUD logic (to be implemented)
│
├── /services/
│   └── api_service.py           # (To be written) REST or WebSocket API layer
│
├── /db/
│   └── db_connection.py         # (To be written) DB connection + ORM setup
│
└── requirements.txt             # Python dependencies
```

---

## 🚀 How It Works

### 📤 Flow of Input

1. User Input is taken by `main.py`.
2. Input is passed to the `llm.processor.get_structured_output()` method.
3. `prompt_builder.py` loads:
    - The schema from `schema/schema.json`
    - The base prompt from `prompts/prompt.txt`
    - Replaces `{SCHEMA}` with your actual schema in prompt.
4. Sends the complete prompt to Gemini.
5. Gemini returns structured JSON:

```json
{
  "intent": "create_task",
  "entity": "task",
  "data": { ... },
  "filters": { ... }
}
```

6. This is passed to `handlers/crud_handler.py`, which will:
    - Connect to the DB.
    - Execute the respective SQL/ORM-based CRUD action.
    - Output is printed or returned to the frontend (via future REST API).

---

## 🔄 CRUD Operations

CRUD operations will **not** use file-based storage.

Instead:

- They’ll connect to a relational DB (like SQLite, PostgreSQL).
- You’ll define ORM models that map to the schema in `schema.json`.
- The file-based fallback for CRUD has been implemented earlier but will not be used in the final system.

---

## 📌 To Be Implemented

**DB Layer:**
- Define ORM models (SQLAlchemy or Peewee).
- Setup DB connection in `/db/db_connection.py`.

**Handlers/CRUD:**
- In `crud_handler.py`, parse the intent, route to correct function.

**REST API or WebSocket:**
- In `/services/api_service.py`, implement:
    - `/chat` endpoint for POST requests (REST)
    - OR `/ws` WebSocket handler (if using live chat).

**Frontend Integration:**
- REST: Use `fetch()` or `axios` to send prompt to `/chat`.
- WebSocket: Use socket clients for real-time chat.

---

## 🧪 Example Prompt

User says:

> "Create a task to write report by 5 PM tomorrow."

Gemini responds:

```json
{
  "intent": "create_task",
  "entity": "task",
  "data": {
    "title": "write report",
    "due_date": "2025-08-04T17:00"
  },
  "filters": {}
}
```

This triggers the `create_task()` function in `crud_handler.py`, which saves the data to DB.

---

## ✅ Notes

- Make sure your `schema.json` matches your actual DB models.
- API key should not be hardcoded in production.
- Later, you can deploy this using FastAPI + Gunicorn + Nginx or any