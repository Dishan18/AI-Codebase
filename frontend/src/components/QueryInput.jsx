import React, { useState } from "react";

export default function QueryInput({ onSend, disabled }) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!query.trim() || disabled) return;
    onSend(query);
    setQuery("");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="relative max-w-5xl mx-auto flex items-stretch"
    >
      <input
        autoFocus
        className="flex-1 bg-[#111] border border-[#00ff8844] py-4 px-6 outline-none focus:border-[#00ff88] transition-all text-sm text-[#00ff88] placeholder:opacity-20"
        placeholder="Type query and hit ENTER..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        disabled={disabled}
      />
      <button
        type="submit"
        disabled={disabled || !query.trim()}
        className="bg-[#00ff88] text-black px-8 text-[10px] md:text-xs font-bold uppercase hover:bg-white transition-colors disabled:opacity-20 border border-[#00ff88] whitespace-nowrap"
      >
        {disabled ? "THINKING..." : "EXECUTE"}
      </button>
    </form>
  );
}
