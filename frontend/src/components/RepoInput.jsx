import React, { useState } from "react";

export default function RepoInput({ onIngest, loading }) {
  const [url, setUrl] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault(); 
    if (!url.trim() || loading) return;
    onIngest(url);
  };

  return (
    <div className="w-full max-w-2xl p-6 md:p-8 terminal-card rounded-sm bg-[#0d0d0d]">
      <div className="mb-6 text-center md:text-left">
        <h2 className="text-xl font-bold mb-2 uppercase tracking-widest glow-text text-[#00ff88]">
          Connect Repository
        </h2>
        <p className="text-xs opacity-50 italic text-[#00ff88]">
          System requires a public GitHub URL.
        </p>
      </div>

      <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-0">
        <input
          type="text"
          placeholder="https://github.com/account/repository"
          className="flex-1 bg-black border border-[#00ff8844] p-4 text-sm focus:border-[#00ff88] outline-none text-[#00ff88] placeholder:opacity-20 transition-all"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          disabled={loading}
          autoFocus
        />
        <button
          type="submit"
          disabled={loading || !url.trim()}
          className="bg-[#00ff88] text-black px-8 py-4 text-xs font-bold uppercase hover:bg-white transition-all disabled:opacity-30 whitespace-nowrap border border-[#00ff88]"
        >
          {loading ? "INITIALIZING..." : "ENTER REPOSITORY"}
        </button>
      </form>
    </div>
  );
}
