import React, { useState, useRef, useEffect } from "react";
import RepoInput from "./components/RepoInput";
import ChatWindow from "./components/ChatWindow";
import QueryInput from "./components/QueryInput";
import { ingestRepo, queryRepo } from "./services/api";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [repoReady, setRepoReady] = useState(false);
  const chatEndRef = useRef(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  const ingest = async (url) => {
    setLoading(true);
    try {
      await ingestRepo(url);
      setMessages([
        {
          role: "ai",
          content: `SYSTEM_STATUS: Repository [${url}] indexed successfully.`,
        },
      ]);
      setRepoReady(true);
    } catch (e) {
      setMessages([{ role: "ai", content: "ERROR: Ingestion failed." }]);
    }
    setLoading(false);
  };

  const ask = async (q) => {
    if (!q.trim()) return;
    setMessages((m) => [...m, { role: "user", content: q }]);
    setLoading(true);
    try {
      const res = await queryRepo(q);
      let displayContent = "";
      if (res.answer && typeof res.answer === "string" && res.answer.trim() !== "") {
        displayContent = res.answer;
      }
      else if (res.results && res.results.length > 0) {
        displayContent = res.results
          .map((r) => `// File: ${r.file_path}\n${r.content || r.snippet}`)
          .join("\n\n---\n\n");
      }
      else {
        displayContent =
          "SYSTEM_ERROR: No relevant context found in vector database.";
      }
      setMessages((m) => [
        ...m,
        {
          role: "ai",
          content: displayContent,
          sources: res.sources || [],
          results: res.results || [],
        },
      ]);
    } catch (err) {
      setMessages((m) => [
        ...m,
        {
          role: "ai",
          content:
            "CRITICAL_FAILURE: Backend unreachable or internal server error.",
        },
      ]);
    }

    setLoading(false);
  };

  const handleReset = () => {
    if (window.confirm("Start fresh with a new repository?")) {
      window.location.reload();
    }
  };

  useEffect(() => {
    if (repoReady) {
      document.title = "AI Explainer | Active Session";
    } else {
      document.title = "AI Codebase Explainer";
    }
  }, [repoReady]);

  return (
    <div className="h-screen flex flex-col bg-[#0a0a0a] text-[#00ff88] font-mono selection:bg-[#00ff88] selection:text-black overflow-hidden">
      <header className="p-4 md:p-6 border-b border-[#00ff8822] bg-[#0d0d0d] flex justify-between items-center">
        <div>
          <h1 className="text-xl md:text-2xl font-bold tracking-tighter uppercase glow-text text-[#00ff88]">
            AI Codebase Explainer
          </h1>
          <p className="text-[10px] opacity-40 tracking-[0.2em] uppercase">
            Multi-Agent RAG System
          </p>
        </div>

        {repoReady && (
          <button
            onClick={handleReset}
            className="px-4 py-2 border border-[#ff4444] text-[#ff4444] text-[10px] font-bold uppercase hover:bg-[#ff444422] transition-all"
          >
            + New Repo
          </button>
        )}
      </header>
      <main className="flex-1 overflow-hidden flex flex-col px-4 md:px-8">
        {!repoReady ? (
          <div className="flex-1 flex items-center justify-center">
            <RepoInput onIngest={ingest} loading={loading} />
          </div>
        ) : (
          <div className="flex-1 overflow-y-auto custom-scrollbar py-6">
            <ChatWindow messages={messages} loading={loading} />
            <div ref={chatEndRef} />
          </div>
        )}
      </main>
      {repoReady && (
        <footer className="p-4 md:p-6 border-t border-[#00ff8822] bg-[#0d0d0d]">
          <QueryInput onSend={ask} disabled={loading} />
        </footer>
      )}
    </div>
  );
}
