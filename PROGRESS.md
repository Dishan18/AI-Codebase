# AI Codebase Explainer

## Project Name

AI Codebase Explainer (Multi-Agent + RAG + Memory)

---

## Goal

Build an AI system that:

* Understands any GitHub repository
* Answers natural language questions about code
* Explains, debugs, summarizes, and searches code intelligently

---

## Summary

An AI-powered developer assistant that ingests GitHub repositories, converts them into semantic embeddings, and enables intelligent querying using Retrieval-Augmented Generation (RAG), a multi-agent architecture, and short-term conversational memory.

---

## Tech Stack

### Backend

* FastAPI
* Python

### Frontend

* React (Vite)
* Tailwind CSS

### AI / RAG

* Ollama (local LLM - Mistral)
* Sentence Transformers (`all-MiniLM-L6-v2`)
* FAISS (vector search)

### Architecture

* Multi-Agent System
* Hybrid Router (rule-based + LLM fallback)
* Short-term Memory (last **3 interactions**, not 5)

---

## Project Structure

```text
backend/
├── routes/
│   └── repo.py
├── services/
│   ├── repo_service.py
│   ├── processing_service.py
│   ├── embedding_service.py
│   ├── vector_store.py
│   ├── store.py
│   ├── llm_service.py
├── agents/
│   ├── router_agent.py
│   ├── explainer_agent.py
│   ├── debug_agent.py
│   ├── summary_agent.py
│   ├── search_agent.py
├── utils/
│   ├── chunker.py
│   ├── file_filter.py
│   ├── file_reader.py
├── repos/
└── app.py

frontend/
├── src/
│   ├── components/
│   │   ├── RepoInput.jsx
│   │   ├── ChatWindow.jsx
│   │   ├── ChatMessage.jsx
│   │   ├── QueryInput.jsx
│   │   └── MessageBubble.jsx (unused)
│   ├── services/
│   │   └── api.js
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
├── index.html
```

---

## Progress

### Day 1 — Ingestion Pipeline

* Repo cloning (GitPython)
* File filtering (extensions, size limits, excluded dirs)
* Backend setup (FastAPI)
* Clean modular structure

---

### Day 2 — Processing Layer

* File reading (including `.ipynb` parsing)
* Chunking:

  * Code → line-based chunks
  * Text → paragraph-based chunks with overlap
* Metadata attachment (`file_path`, content)
* Chunk limiting per file (max 5 chunks per file)

---

### Day 3 — Semantic Layer

* Embedding generation (SentenceTransformers)
* Vector normalization (cosine similarity via L2)
* FAISS index (IndexFlatL2)
* Semantic retrieval pipeline integrated

---

### Day 4 — RAG System

* Query API (`/query-repo`)
* Top-K retrieval + deduplication by file
* Context construction for LLM
* Ollama integration (Mistral)
* Prompt engineering with:

  * strict context usage
  * fallback ("Not enough information")

---

### Day 5 — Multi-Agent + Memory

* Multi-Agent system:

  * Explainer
  * Debug
  * Summary
  * Search
* Hybrid router:

  * Rule-based classification (keywords + query length)
  * LLM fallback classification
* Search agent:

  * Direct substring match over retrieved chunks
* Memory:

  * Stores last **3 interactions**
  * Injected into LLM prompt

---

### Day 6 — Frontend

* Terminal-style UI (neon green, hacker aesthetic)
* Built with React + Tailwind
* Repo ingestion interface
* Chat-based interaction system
* Multi-agent response rendering:

  * LLM answers
  * Code search results
  * Collapsible source viewer
* Auto-scroll behavior
* Loading states ("AGENT_THINKING...")
* Session reset ("+ New Repo")
* Error handling (basic frontend fallback messages)

---

## Current Capabilities

* Explain code logic
* Debug issues using context
* Summarize repositories
* Search code snippets (keyword-based)
* Maintain short conversational context
* Interactive terminal-style UI

---

## Current Status

**Day 6 complete** — Full-stack system is operational and stable.

---

## Known Limitations

* Search agent is substring-based (not semantic)
* No persistent storage (FAISS in-memory only)
* LLM depends on local Ollama availability
* No authentication / private repo support
* Limited chunking intelligence (no AST yet)

---

## Next Step — Day 7 (Refinement & Polish)

* Persistent FAISS index (save/load from disk)
* Improve error handling:

  * empty repos
  * invalid URLs
  * LLM failures
* CORS restriction for production
* Improve retrieval quality (better chunking / ranking)

---

## Future Improvements

* Multi-repo querying
* AST-based chunking
* Hybrid search (semantic + keyword)
* Agent collaboration (agents calling each other)
* Streaming responses
* Export chat (Markdown / PDF)
* Deployment (Docker + cloud)

---