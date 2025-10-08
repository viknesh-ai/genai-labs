# viknesh-genai-labs

Project-as-course: a single FastAPI + GenAI codebase that progressively implements 100 FastAPI concepts.
Phases: API versioning → OpenAI integrations → RAG → Multimodal → Deployment.

## How to run (dev)
1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. uvicorn app.main:app --reload
