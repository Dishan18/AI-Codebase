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

### AI / RAG

* Ollama (local LLM)
* Sentence Transformers (embeddings)
* FAISS (vector search)

### Architecture

* Multi-Agent System
* Hybrid Router (rule + LLM fallback)
* Short-term Memory (last 5 interactions)

### Tools

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

### Day 1 — Ingestion Pipeline

* Repo cloning (GitPython)
* File filtering
* Backend setup (FastAPI)
* Clean project structure

---

### Day 2 — Processing Layer

* File reading system
* Chunking with overlap
* Metadata attachment
* Repo → chunks pipeline

---

### Day 3 — Semantic Layer

* Embedding generation
* FAISS index
* Semantic similarity search
* Integration into backend

---

### Day 4 — RAG System

* Query API
* Retrieval + context building
* LLM integration (Ollama)
* Prompt engineering
* Output quality optimization

---

### Day 5 — Multi-Agent + Memory

#### Multi-Agent System

* Router agent (intent classification)
* Explainer agent (code understanding)
* Debug agent (issue analysis)
* Summary agent (high-level overview)
* Search agent (code snippet retrieval)

---

#### Hybrid Routing

* Rule-based classification (fast)
* LLM fallback for complex queries
* Fixed routing priority bug (intent > length)

---

#### Memory System

* Short-term memory (last 5 Q/A pairs)
* Context-aware responses
* Integrated into LLM prompts

---

#### Quality Improvements

* Chunk trimming
* Top-k filtering
* Improved search matching (word-level)

---

## Current Capabilities

* Explain code logic
* Debug issues
* Summarize repositories
* Search code snippets
* Maintain conversational context

---

## Current Status

Day 5 complete — multi-agent RAG system with memory and improved routing.

---

## Next Step

Day 6 — Frontend

* Chat interface
* Repo input UI
* Display answers + sources

---

## Future Improvements

* Persistent vector storage
* Multi-repo support
* AST-based chunking
* Advanced agent collaboration
