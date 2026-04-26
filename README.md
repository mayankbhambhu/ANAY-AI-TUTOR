# ANAY — AI Tutor Platform

> Your AI-powered study partner. Ask anything, go deep, understand completely.

ANAY is a RAG-based (Retrieval-Augmented Generation) AI tutoring platform that lets you upload your own course material and chat with it. Ask questions naturally, get adaptive explanations, and follow the thread until you actually understand — not just recognise — the answer.

---

## What it does

- **RAG-powered Q&A** — your PDF documents are chunked, embedded, and stored in a local Chroma vector database. Every question retrieves the most relevant context before the LLM responds, keeping answers grounded in your material.
- **Gemini backend** — uses `gemini-2.5-flash` for generation and `gemini-embedding-001` for embeddings via Google's Generative AI API.
- **FastAPI server** — a lightweight REST API (`POST /ask`) bridges the HTML frontend to the LangChain inference chain.
- **Static frontend** — a fully self-contained multi-page site (Landing, Chat, About, Contact, 404) with no framework dependencies.

---

## Project structure

```
.
├── api.py          # FastAPI server — exposes POST /ask endpoint
├── ingest.py       # One-time script to build the Chroma vector DB from a PDF
├── document.pdf    # Your source material (not committed — add your own)
├── chroma_db/      # Auto-generated vector store (gitignored)
├── Landing.html    # Marketing / home page
├── index.html      # Chat interface
├── aboutus.html    # About page
├── contact.html    # Contact page
├── 404.html        # 404 error page
└── .env            # API keys (not committed — see setup below)
```

---

## Prerequisites

- Python 3.9+
- A [Google AI Studio](https://aistudio.google.com/) API key with access to Gemini models
- Your course material as a PDF named `document.pdf`

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/anay.git
cd anay
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
# AI / RAG libraries
pip install streamlit langchain langchain-google-genai langchain-community chromadb pypdf python-dotenv

# Backend server
pip install fastapi uvicorn
```

### 4. Add your API key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Add your PDF

Place your course material at the project root as `document.pdf`.

### 6. Build the vector database

This only needs to be run once (or whenever your PDF changes):

```bash
python3 ingest.py
```

This creates a `chroma_db/` folder containing the embedded document chunks.

### 7. Start the API server

```bash
uvicorn api:app --reload --reload-exclude "venv"
```

The server runs at `http://localhost:8000`. To kill any process already occupying port 8000:

```bash
lsof -ti:8000 | xargs kill -9
```

### 8. Open the frontend

Open `Landing.html` in your browser, or serve the HTML files with any static file server. The chat page (`index.html`) sends requests to `http://localhost:8000/ask`.

---

## How it works

```
User question
      │
      ▼
  FastAPI /ask
      │
      ▼
  Chroma retriever  ──►  top-3 relevant chunks from your PDF
      │
      ▼
  Gemini 2.5 Flash  ──►  answer grounded in retrieved context
      │
      ▼
  JSON response  ──►  rendered in the chat UI
```

The prompt keeps things focused: the model acts as a direct tutor, answers from the provided context, and doesn't pad responses with unnecessary caveats.

---

## API reference

### `POST /ask`

**Request body**
```json
{ "question": "What is an eigenvector?" }
```

**Response**
```json
{ "reply": "An eigenvector is a vector that..." }
```

---

## Gitignore recommendations

Add these to your `.gitignore`:

```
.env
chroma_db/
venv/
document.pdf
__pycache__/
*.pyc
```

---

## Tech stack

| Layer | Technology |
|---|---|
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Google `gemini-embedding-001` |
| Vector store | ChromaDB (local) |
| RAG framework | LangChain |
| Backend | FastAPI + Uvicorn |
| Frontend | Vanilla HTML/CSS/JS |

---

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you'd like to change.

---


