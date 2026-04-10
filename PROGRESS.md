# AI Codebase Explainer

## Project Name

AI Codebase Explainer (Multi-Agent + RAG)

---

## Goal

Build an AI system that can:

* Understand any GitHub repository
* Explain code structure, logic, and relationships
* Answer natural language questions about the codebase

---

## Summary

AI-powered developer tool that ingests GitHub repositories and enables intelligent querying using Retrieval-Augmented Generation (RAG) and a multi-agent architecture.

Transforms raw code into structured semantic knowledge and allows natural language interaction with codebases.

---

## Tech Stack

### Backend

* FastAPI
* Python

### AI / RAG

* Ollama (local LLM)
* Sentence Transformers (embeddings)
* FAISS (vector database)

### Architecture

* Multi-Agent System (custom)

### Dev Tools

* GitPython
* VS Code
* Git/GitHub

---

## Project Structure

backend/
├── routes/
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
├── repos/
├── app.py

frontend/

---

## Progress

### Completed (Day 1)

* Repo ingestion pipeline
* GitHub cloning (optimized)
* File filtering
* Backend architecture

---

### Completed (Day 2)

* File reading
* Chunking (with overlap)
* Metadata attachment
* Processing pipeline

---

### Completed (Day 3)

* Embeddings generation
* FAISS vector index
* Semantic similarity search
* Backend integration

---

### Completed (Day 4)

* Query API
* Semantic retrieval
* LLM integration (Ollama)
* Prompt engineering
* Response optimization

---

### Completed (Day 5)

* Multi-agent architecture
* Hybrid router (rule + LLM classification)
* Explainer agent (code understanding)
* Debug agent (issue analysis)
* Summary agent (high-level overview)
* Code search agent (snippet retrieval)
* Query routing and specialization

---

### In Progress

* UI/UX design for frontend

---

### Remaining Objectives

#### Day 6 — Frontend

* Chat interface
* Repo input field
* Display answers + sources
* Improve UX

---

#### Day 7+ — Advanced Improvements

* Persistent vector storage
* Multi-repo support
* AST-based chunking
* Advanced agent reasoning

---

## Current Status

Day 5 complete — multi-agent RAG system with specialized reasoning implemented.

---

## Next Step

Build frontend interface for user interaction.
