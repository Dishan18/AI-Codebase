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

This project is an AI-powered developer tool that ingests a GitHub repository, processes its codebase, and enables intelligent querying using Retrieval-Augmented Generation (RAG) and multi-agent systems.

It converts raw code into structured, searchable knowledge and allows users to interact with repositories through natural language.

---

## Tech Stack

### Backend

* FastAPI
* Python

### AI / RAG

* Ollama (local LLM for development)
* Gemini API (for deployment)
* Sentence Transformers (embeddings)
* FAISS (vector database)

### Agent Framework

* LangChain (light orchestration)

### Dev Tools

* GitPython (repo cloning)
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
├── utils/
├── agents/
├── vectorstore/
├── repos/
├── app.py

frontend/

---

## Progress

### Completed (Day 1)

* Backend setup with FastAPI
* Virtual environment + dependency management
* Git setup with proper `.gitignore`
* Repo ingestion API (`/ingest-repo`)
* GitHub repo cloning (optimized with shallow clone)
* File filtering system
* Clean architecture (routes/services/utils)
* End-to-end ingestion pipeline

---

### Completed (Day 2)

* File reading system
* Chunking implementation (fixed-size + overlap)
* Metadata attachment (file path)
* Processing pipeline: files → chunks
* API updated to return chunk data
* Fixed Windows permission issue during repo deletion
* Improved filtering (README support)

---

### Completed (Day 3)

* Implemented embedding generation using sentence-transformers
* Built FAISS vector index for similarity search
* Enabled semantic search over code chunks
* Integrated embeddings and vector store into API
* Added in-memory storage for index + chunks

---

### In Progress

* Query system design
* LLM integration planning

---

### Remaining Objectives

#### Day 4 — Query + RAG

* Build `/query-repo` endpoint
* Retrieve relevant chunks using FAISS
* Pass context to LLM
* Generate grounded answers

---

#### Day 5 — Multi-Agent System

* Router agent
* Explainer agent
* Debug agent

---

#### Day 6 — Frontend

* Repo input UI
* Chat interface
* Result visualization

---

#### Day 7+ — Advanced Features

* AST-based parsing
* Dependency graphs
* Improved chunking (function-level)
* Multi-repo support

---

## Current Status

Day 3 complete — semantic retrieval system implemented.

---

## Next Step

Build query endpoint and integrate LLM for answer generation.
