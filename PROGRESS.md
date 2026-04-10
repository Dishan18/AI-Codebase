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
│   ├── llm_service.py
├── utils/
├── agents/
├── repos/
├── app.py

frontend/

---

## Progress

### Completed (Day 1)

* Backend setup with FastAPI
* Virtual environment setup
* Git + `.gitignore` configuration
* Repo ingestion API
* Optimized GitHub cloning (shallow clone)
* File filtering system
* Clean architecture setup

---

### Completed (Day 2)

* File reading system
* Chunking implementation (fixed-size + overlap)
* Metadata attachment
* Processing pipeline (files → chunks)
* Fixed Windows permission issues
* Improved filtering (README support)

---

### Completed (Day 3)

* Embedding generation using sentence-transformers
* FAISS vector index implementation
* Semantic similarity search
* Integration into backend pipeline
* In-memory storage of embeddings + chunks

---

### Completed (Day 4)

* Query API (`/query-repo`)
* Semantic retrieval using FAISS
* Context construction from retrieved chunks
* LLM integration using Ollama
* Prompt engineering improvements
* Response quality optimization (top-k filtering, chunk trimming)

---

### In Progress

* Designing multi-agent architecture
* Planning query routing logic

---

### Remaining Objectives

#### Day 5 — Multi-Agent System

* Router agent (classify query type)
* Explainer agent (code understanding)
* Debug agent (error analysis)

---

#### Day 6 — Frontend

* Repo input UI
* Chat interface
* Display sources cleanly

---

#### Day 7+ — Advanced Improvements

* AST-based chunking (function-level understanding)
* Persistent vector storage
* Multi-repo support
* Improved prompt strategies

---

## Current Status

Day 4 complete — full RAG pipeline implemented with semantic retrieval and LLM-based answer generation.

---

## Next Step

Implement multi-agent system to improve reasoning and query handling.
