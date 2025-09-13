# 🧠 MCP Server (Model Compute Paradigm)

A modular, async FastAPI server that dynamically routes incoming ML tasks (e.g. chat, sentiment, recommender, summarization) to pluggable models via a YAML/JSON-backed model registry. Includes retry logic, streaming OpenAI support, async concurrency, Docker support, and unit testing with mocks.

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


🛠 Setup
📦 Install dependencies
git clone https://github.com/YOUR_USERNAME/mcp-server.git
cd mcp-server

# Optional: create virtualenv
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

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

✅ Roadmap
 Async FastAPI - Completed
 Model registry (YAML) - Completed
 Retry & streaming support - Completed
 Unit tests with mocks - Completed
 Docker support - Completed
 CI/CD GitHub Action - Pending
 OAuth/token-based auth - Pending
 HuggingFace model support - Pending
 WebSocket response streaming - Pending

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

📄 License
MIT

✨ Author
Built by Sriram Kumar Reddy Challa