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
├── routes/          # API endpoints
├── services/        # Core logic (repo ingestion, parsing)
├── utils/           # Helper functions (filtering, chunking)
├── agents/          # Multi-agent system (future)
├── vectorstore/     # FAISS / embeddings (future)
├── repos/           # Cloned repositories (ignored)
├── app.py           # FastAPI entry point

frontend/            # UI (to be built)

---

## Progress

### Completed (Day 1)

* Backend setup with FastAPI
* Virtual environment + dependency management
* Git setup with proper `.gitignore`
* Repo ingestion API (`/ingest-repo`)
* GitHub repo cloning (optimized with shallow clone)
* File filtering system (extensions, size, excluded dirs)
* Clean project architecture (routes/services/utils separation)
* End-to-end working pipeline:

  * Input: GitHub URL
  * Output: filtered file list

---

### In Progress

* Preparing for file content extraction
* Designing chunking strategy

---

### Remaining Objectives

#### Day 2 — Data Preparation

* Read file contents
* Implement chunking (function/file level)
* Attach metadata (file path, function name)

---

#### Day 3 — Embeddings + Vector Store

* Generate embeddings (Sentence Transformers)
* Store in FAISS
* Implement similarity search

---

#### Day 4 — RAG Pipeline

* Query → retrieve relevant chunks
* LLM response generation
* Context-grounded answers

---

#### Day 5 — Multi-Agent System

* Router agent (query classification)
* Explainer agent
* Debug / analysis agent

---

#### Day 6 — Frontend

* Repo input UI
* Chat interface
* File references display

---

#### Day 7+ — Advanced Features

* AST-based parsing (function-level understanding)
* Dependency graph generation
* Code search improvements
* Repo comparison

---

## Current Status

Day 1 complete — ingestion pipeline working and optimized.

---

## Next Step

Implement file reading and chunking to prepare data for embeddings.
