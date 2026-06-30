# 🤖 Autonomous AI Agent

An Autonomous AI Agent built using **FastAPI**, **Google Gemini 2.5 Flash**, and **Python**. The agent accepts a user request, generates an execution plan, autonomously executes the plan using AI, and produces a professionally formatted Microsoft Word document.

---

# 🚀 Features

- Autonomous task planning using Gemini AI
- AI-powered content generation
- FastAPI REST API
- Automatic Word document generation (.docx)
- Modular architecture
- Environment variable support
- Swagger API documentation
- Error handling and clean project structure

---

# 🛠️ Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Google Gemini 2.5 Flash
- Google GenAI SDK
- python-docx
- python-dotenv
- Pydantic

---

# 📁 Project Structure

```
AUTONOMOUS-AI-AGENT/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── document.py
│   ├── executor.py
│   ├── llm.py
│   ├── main.py
│   ├── models.py
│   ├── planner.py
│   └── tools.py
│
├── output/
│   └── generated_document.docx
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository-url>

cd autonomous-ai-agent
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Application will start at

```
http://127.0.0.1:8000
```

---

# 📘 Swagger API Documentation

Open

```
http://127.0.0.1:8000/docs
```

---

# 📤 API Endpoint

## POST /agent

### Sample Request

```json
{
  "request": "Create a business proposal for an AI Hospital Management System."
}
```

---

### Sample Response

```json
{
  "status": "success",
  "tasks": [
    "Understand user requirements",
    "Generate execution plan",
    "Generate proposal",
    "Create Word document"
  ],
  "document": "output/generated_document.docx",
  "response": "Business proposal generated successfully."
}
```

---

# 🔄 Workflow

```
User Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Planner Agent
      │
      ▼
Gemini AI
      │
      ▼
Execution Engine
      │
      ▼
Document Generator
      │
      ▼
Generated Word Document
```

---

# 📄 Generated Output

The generated proposal is automatically saved as

```
output/generated_document.docx
```

---

# 🧠 Autonomous Agent Architecture

### Planner

- Understands user request
- Breaks the task into executable steps

### Executor

- Executes generated plan
- Calls AI model
- Coordinates tool execution

### LLM Module

- Connects with Google Gemini
- Generates intelligent responses

### Tool Module

- Invokes document generation tool

### Document Generator

- Creates Microsoft Word document
- Saves output automatically

---

# 🧪 Testing

Swagger UI can be used for testing.

Example:

```
POST /agent
```

Sample prompt:

```
Create a business proposal for an AI Hospital Management System.
```

---

# 📦 Output

Example generated document:

```
output/generated_document.docx
```

---

# 🔒 Security

- API key stored securely using `.env`
- `.env` excluded from version control using `.gitignore`

---

# 📌 Future Improvements

- Multi-tool autonomous execution
- Memory-enabled AI agent
- Retrieval-Augmented Generation (RAG)
- Multi-agent collaboration
- PDF generation
- Database integration
- Authentication & Authorization
- Conversation history
- Docker deployment
- Cloud deployment

---

# 👩‍💻 Author

**Diksha Chikaraddi**

Entry-Level AI/ML Engineer | Python Developer | Generative AI Enthusiast

Skills:
- Python
- FastAPI
- Google Gemini
- Generative AI
- LangChain
- RAG
- Machine Learning
- REST APIs

---

# 📄 License

This project was developed as part of the **Fluid AI Python AI Engineer – Autonomous Agents Assessment**.