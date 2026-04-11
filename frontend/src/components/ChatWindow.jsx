import React from "react";
import ChatMessage from "./ChatMessage";

export default function ChatWindow({ messages, loading }) {
  return (
    <div className="space-y-6 pb-24">
      {messages.length === 0 && (
        <div className="opacity-20 text-center py-20 text-[10px] tracking-[0.5em]">
          [ NO_DATA_IN_BUFFER ]
        </div>
      )}

      {messages.map((msg, i) => (
        <ChatMessage key={i} msg={msg} />
      ))}

      {loading && (
        <div className="flex items-center gap-2 text-xs opacity-70 italic animate-pulse">
          <span className="w-2 h-2 bg-[#00ff88] rounded-full"></span>
          AGENT_THINKING...
        </div>
      )}
    </div>
  );
}
