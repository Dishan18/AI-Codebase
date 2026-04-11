import React from "react";

export default function ChatMessage({ msg }) {
  const isAi = msg.role === "ai";

  return (
    <div className={`flex ${isAi ? "justify-start" : "justify-end"} w-full`}>
      <div
        className={`max-w-[90%] md:max-w-[80%] p-4 rounded border ${
          isAi
            ? "bg-[#111] border-[#00ff8822]"
            : "bg-[#00ff8808] border-[#00ff8844]"
        }`}
      >
        <div className="flex items-center gap-2 mb-3 text-[9px] uppercase font-bold opacity-30">
          <span>{isAi ? ">> SYSTEM_LOG" : ">> USER_QUERY"}</span>
          <div className="h-[1px] flex-1 bg-[#00ff88] opacity-20"></div>
        </div>

        <div className="text-sm leading-relaxed whitespace-pre-wrap">
          {msg.content}
          {isAi && (
            <span className="inline-block w-2 h-4 bg-[#00ff88] ml-1 cursor-blink align-middle" />
          )}
        </div>

        {/* Snippet Explorer */}
        {(msg.results || msg.sources) && (
          <div className="mt-4 border-t border-[#00ff8811] pt-4 space-y-2">
            {(msg.results || msg.sources).map((item, idx) => (
              <details
                key={idx}
                className="group border border-[#00ff8822] bg-black rounded overflow-hidden"
              >
                <summary className="cursor-pointer p-2 text-[10px] font-mono text-[#00ff88cc] hover:bg-[#00ff8811]">
                  {item.file_path}
                </summary>
                <pre className="p-3 text-[11px] overflow-x-auto custom-scrollbar bg-[#050505] text-[#00ff8888]">
                  <code>{item.snippet || item.content}</code>
                </pre>
              </details>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
