# 🧠 MCP Server (Model Compute Paradigm)

A modular, production-ready FastAPI server built to route and orchestrate multiple AI/LLM-powered models behind a unified, scalable interface. It supports **streaming chat**, **LLM-based routing**, and **multi-model pipelines** (like analyze → summarize → recommend) – all asynchronously and fully Dockerized.

---
## 🎯 Project Score (Production Readiness)

| Capability                      | Status     | Details                                                                      |
|-------------------------------|------------|-------------------------------------------------------------------------------|
| 🧠 Multi-Model Orchestration   | ✅ Complete | Dynamic routing between `chat`, `summarize`, `sentiment`, `recommend`        |
| 🤖 LLM-Based Task Router       | ✅ Complete | GPT-powered routing via `"auto"` task type                                   |
| 🔁 Async FastAPI + Concurrency | ✅ Complete | Async/await + concurrent task execution with simulated/model API delays      |
| 🔊 GPT Streaming Support       | ✅ Complete | `text/event-stream` chunked responses for chat endpoints                     |
| 🧪 Unit + Mocked API Tests     | ✅ Complete | Pytest-based test suite with mocked `run()` responses                        |
| 🐳 Dockerized + Clean Layout   | ✅ Complete | Python 3.13 base image, no Conda dependency, production-ready Dockerfile     |
| 📦 Metadata-Driven Registry    | ✅ Complete | Model metadata loaded from external YAML config                              |
| 🔐 Rate Limiting & Retry       | ⏳ In Progress | Handles 429 retry loop; rate limiting controls WIP                        |
| 🧪 CI + Docs                   | ⏳ Next     | GitHub Actions + Swagger/Redoc planned                                       |

---
## 🧩 Why This Project? (Motivation)

Modern ML/LLM deployments often involve:
- Multiple task types and model backends (OpenAI, HF, local, REST)
- Routing decisions based on input intent
- Combining outputs of multiple models (e.g., `summarize` + `recommend`)
- Handling 429 retries, async concurrency, streaming responses

🔧 However, building such an **LLM backend API server** that is:
- Async + concurrent
- Streamable
- Pluggable (via metadata)
- Testable
- Dockerized
… is **non-trivial** and not easily found in one single place.

---
## 💡 What We’ve Built (Solution)

This repo is a **production-ready PoC** of an MCP (Model-Compute Paradigm) architecture:

- ✅ **FastAPI-based microserver** to handle multiple tasks via `/task` endpoint
- ✅ Task router that can:
  - 🔁 Dispatch to specific model types (`chat`, `sentiment`, `summarize`, `recommend`)
  - 🤖 Use an LLM to infer which task to run (`auto`)
  - 🧠 Run multiple models in sequence (`analyze`)
- ✅ GPT streaming via `text/event-stream`
- ✅ Async/await enabled architecture for concurrency
- ✅ Clean modular code for easy extension
- ✅ Dockerized for deployment
- ✅ Tested using Pytest with mocking

---

## 🛠️ Use Cases

| Use Case                                | MCP Server Support                           |
|----------------------------------------|-----------------------------------------------|
| Build your own ChatGPT-style API       | ✅ `chat` task with streaming                  |
| Build intelligent task router           | ✅ `auto` task with GPT-powered intent parsing |
| Build AI pipelines (like RAG/RL)        | ✅ `analyze` task with sequential execution    |
| Swap between OpenAI/HuggingFace APIs   | ✅ Via `model_registry.yaml` config           |
| Add custom models (e.g., OCR, vision)   | ✅ Just add a new module + registry entry     |

---


## 🚀 Features

- ✅ **Async FastAPI** server
- 🧠 **Task-based Model Routing** (`chat`, `sentiment`, `recommender`, `summarize`)
- 📄 **Model Registry** from YAML/JSON
- 🔁 **Automatic Retry** and **Rate Limit Handling** for APIs
- 🔄 **Streaming Responses** for Chat
- 🧪 **Unit Tests + Mocked API Calls**
- 🐳 **Dockerized** for production deployment
- 📦 Modular structure, ready for CI/CD

---

## 🏗 Architecture Overview

```plaintext
               ┌────────────┐
               │  Frontend  │
               └─────┬──────┘
                     │
                     ▼
              ┌────────────┐        YAML/JSON
              │  FastAPI   │◄────┐ Model Registry
              │   Server   │     │
              └─────┬──────┘     ▼
     ┌──────────────┼──────────────┐
     │              │              │
     ▼              ▼              ▼
 [chat]         [sentiment]   [recommender]
  GPT-4         HF pipeline   stub logic / API

---
🛠 Setup
📦 Install dependencies
git clone https://github.com/YOUR_USERNAME/mcp-server.git
cd mcp-server
---
# Optional: create virtualenv
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
or
conda create -n <env_name>
conda activate <env_name>

pip install -r requirements.txt

▶️ Run the server
uvicorn app:app --reload

Access the docs at: http://localhost:8000/docs


🧪 Running Tests
pytest tests/

Unit tests mock external API calls using unittest.mock.AsyncMock.

🐳 Docker Support
🔨 Build image
docker build -t mcp-server .

🚀 Run container
docker run -p 8000:8000 mcp-server

🧰 Example API Request
curl -X POST http://localhost:8000/task \
  -H "Content-Type: application/json" \
  -d '{
        "type": "chat",
        "input": "What are the benefits of restorative yoga?"
      }'

🔍 Directory Structure
mcp/
├── app.py                  # FastAPI entry
├── models/                 # ML models (chat, sentiment, etc.)
├── agent/
│   ├── task_router.py      # Task router
│   └── model_registry.py   # Registry loader
├── registry/models.yaml    # YAML registry of model metadata
├── tests/                  # Unit tests
├── Dockerfile
├── requirements.txt
├── README.md
└── .env / .gitignore


🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

📄 License
MIT

✨ Author
Built by Sriram Kumar Reddy Challa
