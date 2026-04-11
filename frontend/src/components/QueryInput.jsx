import React, { useState, useRef, useEffect } from "react";

export default function QueryInput({ onSend, disabled }) {
  const [query, setQuery] = useState("");
  const inputRef = useRef(null);

  // This "Watcher" waits for the AI to finish thinking
  useEffect(() => {
    if (!disabled && inputRef.current) {
      inputRef.current.focus();
    }
  }, [disabled]); // Triggers every time the loading/disabled state changes

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!query.trim() || disabled) return;

    onSend(query);
    setQuery("");
    // We don't focus here anymore; the useEffect above handles it once the AI replies
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="relative max-w-5xl mx-auto flex items-stretch"
    >
      <input
        ref={inputRef}
        autoFocus
        className="flex-1 bg-[#111] border border-[#00ff8844] py-4 px-6 outline-none focus:border-[#00ff88] transition-all text-sm text-[#00ff88] placeholder:opacity-20 disabled:opacity-50"
        placeholder={
          disabled ? "AI is typing..." : "Type query and hit ENTER..."
        }
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        disabled={disabled}
      />
      <button
        type="submit"
        disabled={disabled || !query.trim()}
        className="bg-[#00ff88] text-black px-8 text-[10px] md:text-xs font-bold uppercase hover:bg-white transition-colors disabled:opacity-50 border border-[#00ff88] whitespace-nowrap"
      >
        {disabled ? "THINKING..." : "EXECUTE"}
      </button>
    </form>
  );
}
