# AI Codebase Explainer - Frontend

## Overview
The frontend for the **AI Codebase Explainer** is a React-based web application providing a sleek, terminal-inspired interface for interacting with your code via AI. It connects to a Multi-Agent RAG (Retrieval-Augmented Generation) backend to summarize, explain, and debug GitHub repositories using local LLMs.

---

## 🛠 Tech Stack
* **Core:** [React (Vite)](https://vitejs.dev/)
* **Styling:** [Tailwind CSS](https://tailwindcss.com/)
* **Typography:** JetBrains Mono / Fira Code (Monospace)
* **API Communication:** Fetch API (to FastAPI backend)

---

## 🚀 Key Features
* **Futuristic Terminal UI:** High-contrast **#00ff88** neon accents on a **#0a0a0a** black background with subtle glow effects and blinking terminal cursors.
* **Repository Indexing:** Enter any public GitHub URL to trigger the backend RAG pipeline (cloning, chunking, and FAISS embedding).
* **Multi-Agent Chat:**
    * **Contextual Answers:** Direct explanations of codebase logic.
    * **Source Explorer:** Collapsible views for relevant source code segments provided by the Search Agent.
    * **Thinking Indicators:** Real-time visual feedback while the agent is processing queries.
* **Responsive Layout:** Fully optimized for both desktop development environments and mobile operability.
* **Session Reset:** A dedicated **+ New Repo** button to clear current context and switch projects instantly.

---

## 📦 Getting Started

### 1. Prerequisites
Ensure you have **Node.js** and **npm** installed on your system.

### 2. Installation
Navigate to the frontend directory and install the required dependencies:
```bash
cd frontend
npm install
```

### 3. Tailwind Configuration
Ensure your `tailwind.config.js` and `postcss.config.js` are in the root of the `frontend` folder to enable the utility-first styling.

### 4. Running the Development Server
```bash
npm run dev
```
Open **http://localhost:5173** in your browser to view the application.

---

## 📂 Project Structure
* **`src/components/`**: Modular UI components:
    * `RepoInput.jsx`: Logic for GitHub URL submission.
    * `ChatWindow.jsx`: Scrollable container for the conversation history.
    * `ChatMessage.jsx`: Renders user/AI messages and handles code snippet formatting.
    * `QueryInput.jsx`: Fixed bottom bar for command execution.
* **`src/services/api.js`**: Centralized API logic for communicating with the FastAPI server.
* **`src/App.jsx`**: Global state management (repo status, loading, messages) and layout shell.
* **`src/index.css`**: Custom Tailwind utilities and terminal animations (glows, custom scrollbars, cursors).

---

## 🔧 Backend Integration
By default, the frontend is configured to communicate with the backend at:
**`http://127.0.0.1:8000`**

It utilizes the following endpoints:
* `POST /ingest-repo`: Sends the repository URL for vector database processing.
* `POST /query-repo`: Sends queries and receives answers along with source code metadata.

---

## 📜 Design Principles
> **Authenticity:** The UI aims for a "hacker" aesthetic while maintaining modern usability standards like smooth scrolling, clear hierarchy, and intuitive feedback loops.