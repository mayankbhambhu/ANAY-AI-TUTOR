# ANAY — Personalized AI Tutor

> Post-doctoral level tutoring powered by your own documents, Google Gemini, and a beautiful dark-mode UI.

![ANAY Preview](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-blue?style=flat-square) ![Stack](https://img.shields.io/badge/Stack-FastAPI%20%7C%20LangChain%20%7C%20ChromaDB-purple?style=flat-square) ![Frontend](https://img.shields.io/badge/Frontend-Vanilla%20HTML%2FJS-cyan?style=flat-square)

---

## What is ANAY?

ANAY is a local, privacy-first AI tutor that answers questions based on **your own PDFs**. It uses Retrieval-Augmented Generation (RAG) — meaning it reads your documents, stores them in a local vector database, and gives accurate, context-aware answers powered by Google Gemini.

**All sessions are private. No data leaves your machine except the API call to Gemini.**

---

## Features

- 🌌 **Stunning cosmic UI** — animated particle canvas, glassmorphism panels, dark mode
- 📄 **RAG pipeline** — answers grounded in your uploaded documents
- ⚡ **Two interfaces** — a polished HTML frontend (via FastAPI) and a quick Streamlit app
- 🧠 **Gemini 2.5 Flash** — fast, capable LLM for Q&A
- 🗄️ **ChromaDB** — fully local vector store, no cloud needed
- 🔒 **Privacy first** — your PDFs never leave your machine

---

## Project Structure

```
anay-ai-tutor/
│
├── index.html      # Main frontend UI (served via FastAPI or opened directly)
├── api.py          # FastAPI backend — serves /ask endpoint for the HTML frontend
├── app.py          # Streamlit app — alternative chat interface
├── ingest.py       # One-time script: reads your PDF and builds the vector DB
│
├── document.pdf    # ← YOUR PDF goes here (not committed to git)
├── .env            # ← Your API key goes here (not committed to git)
├── chroma_db/      # ← Auto-generated vector database (not committed to git)
│
├── requirements.txt
└── README.md
```

---

## Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/anay-ai-tutor.git
cd anay-ai-tutor
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Google Gemini API key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_api_key_here
```

> Get a free API key at [https://aistudio.google.com](https://aistudio.google.com)

### 5. Add your PDF

Place your document in the project root and name it `document.pdf`.

### 6. Ingest the PDF (builds the vector database)

```bash
python ingest.py
```

You only need to do this **once** (or whenever you change your PDF).

---

## Running the App

### Option A — HTML Frontend + FastAPI (Recommended)

```bash
uvicorn api:app --reload
```

Then open `index.html` directly in your browser. The frontend will talk to the FastAPI server at `http://127.0.0.1:8000`.

### Option B — Streamlit Interface

```bash
streamlit run app.py
```

Opens automatically at `http://localhost:8501`.

---

## How It Works

```
Your PDF
   ↓
ingest.py  →  Splits into chunks  →  Embeds with Gemini  →  Stores in ChromaDB
                                                                      ↓
User Question  →  api.py / app.py  →  Retrieves top 3 chunks  →  Gemini LLM  →  Answer
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Google Gemini Embedding-001 |
| Vector Store | ChromaDB (local) |
| RAG Framework | LangChain |
| Backend API | FastAPI + Uvicorn |
| Alt Interface | Streamlit |
| Frontend | Vanilla HTML / CSS / JS |

---

## Requirements

See `requirements.txt`. Key packages:

```
streamlit
langchain
langchain-google-genai
langchain-community
chromadb
pypdf
python-dotenv
fastapi
uvicorn
```

---

## Contributing

Pull requests are welcome! If you find a bug or want to add a feature (multi-PDF support, authentication, streaming responses), feel free to open an issue.

---


*Built with ❤️ using LangChain and a lot of CSS.*
