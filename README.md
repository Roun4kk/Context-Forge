# ContextForge

> Hybrid Retrieval & Codebase Intelligence Platform

ContextForge is an AI-powered retrieval system designed to intelligently search, retrieve, and reason over documents and codebases using a hybrid retrieval pipeline combining semantic vector search and keyword-based ranking.

Instead of relying only on embeddings or only on keyword matching, ContextForge combines:

* Semantic Retrieval (SentenceTransformers + FAISS)
* BM25 Keyword Retrieval
* MMR (Maximal Marginal Relevance) Reranking
* Grounded LLM Response Generation

The goal is to evolve ContextForge into a scalable codebase intelligence and developer knowledge platform capable of understanding repositories, technical documentation, APIs, architecture flows, and large engineering systems.

---

# Features

## Current Features

### Hybrid Retrieval Pipeline

* Semantic vector search using SentenceTransformers
* BM25 keyword search using rank-bm25
* Hybrid score fusion
* Cosine similarity based retrieval with FAISS

### Intelligent Reranking

* MMR (Maximal Marginal Relevance) reranking
* Reduces redundant retrieval results
* Improves context diversity and coverage

### Grounded AI Response Generation

* LLM responses constrained using retrieved context
* Reduces hallucinations
* Retrieval-Augmented Generation (RAG) pipeline

### Metadata-Aware Chunking

* Structured chunk objects
* Chunk IDs and metadata tracking
* Source-aware retrieval

### FastAPI Backend

* Modular backend architecture
* REST APIs for ingestion and querying
* Extensible retrieval pipeline

### PDF Ingestion

* PDF upload support
* Text extraction
* Chunking and indexing
* Retrieval-ready ingestion flow

---

# Planned Features

## GitHub Repository Ingestion

* Upload GitHub repository links
* Clone repositories automatically
* Parse and index entire codebases

## AST-Aware Code Chunking

* Function-level chunking
* Class-level chunking
* Route-aware and module-aware indexing
* Language-specific parsers

## Multi-Step Retrieval

* Iterative retrieval orchestration
* Query decomposition
* Retrieval refinement
* Coverage-aware retrieval

## Advanced Reranking

* Cross-encoder reranking
* Query-aware reranking
* Dynamic retrieval depth

## Retrieval Analytics Dashboard

* Recall@K
* MRR
* nDCG
* Retrieval latency metrics
* Query trend analysis

## Frontend Workspace

* Interactive AI workspace
* Upload and query interface
* Source citations
* Retrieval visualization

## Dockerized Deployment

* Backend containerization
* Full-stack deployment support
* Cloud deployment workflows

---

# Architecture

```text
                User Query
                     │
                     ▼
           Hybrid Retrieval Layer
        ┌─────────────────────────┐
        │                         │
        ▼                         ▼
 Semantic Search            BM25 Search
 (FAISS + Embeddings)      (Keyword Search)
        │                         │
        └──────────┬──────────────┘
                   ▼
           Score Fusion Layer
                   ▼
             MMR Reranking
                   ▼
          Context Construction
                   ▼
         Grounded LLM Generation
                   ▼
              Final Response
```

---

# Tech Stack

## Backend

* FastAPI
* Python

## Retrieval & AI

* SentenceTransformers
* FAISS
* rank-bm25
* scikit-learn

## LLM Integration

* Groq API
* Llama 3

## Utilities

* NumPy
* NLTK
* PyMuPDF
* GitPython

---

# Project Structure

```text
contextforge/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── generation/
│   │   ├── ingestion/
│   │   ├── models/
│   │   ├── ranking/
│   │   ├── retrieval/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── .gitignore
└── README.md
```

---

# Retrieval Pipeline

```text
Document Upload
        │
        ▼
Text Extraction
        │
        ▼
Metadata-Aware Chunking
        │
        ▼
Embedding Generation
        │
        ▼
FAISS Vector Indexing
        │
        ├───────────────┐
        │               │
        ▼               ▼
Semantic Search     BM25 Search
        │               │
        └──────┬────────┘
               ▼
         Hybrid Fusion
               ▼
         MMR Reranking
               ▼
      Grounded LLM Output
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Roun4kk/Context-Forge.git
cd Context-Forge/backend
```

---

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

Create a `.env` file inside `backend/`

```env
GROQ_API_KEY=your_api_key_here
```

---

# Running the Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Upload PDF

```http
POST /upload
```

Uploads and indexes documents.

---

## Hybrid RAG Query

```http
GET /rag?query=your_query
```

Returns:

* Retrieved chunks
* Grounded AI-generated response

---

## Hybrid Search

```http
GET /search?query=your_query
```

Returns:

* Hybrid retrieval results
* Semantic + BM25 retrieval outputs

---

# Current Limitations

* In-memory vector storage
* No persistent indexing yet
* PDF-focused ingestion currently
* Chunking still being optimized
* Limited context orchestration

---

# Future Vision

ContextForge is being developed toward becoming:

> A developer-focused retrieval and reasoning system capable of understanding large codebases, engineering documentation, architecture flows, APIs, and technical systems using hybrid retrieval and multi-step AI reasoning.

The long-term goal is to support:

* Repository intelligence
* Codebase querying
* Architecture tracing
* Dependency-aware retrieval
* AI-assisted developer workflows

---

# Author

## Rounak Molpariya

* GitHub: [https://github.com/Roun4kk](https://github.com/Roun4kk)
* LinkedIn: [https://linkedin.com/in/roun4kk](https://linkedin.com/in/roun4kk)

---

# License

This project is currently under active development.
