import React from "react";

export default function ChatMessage({ msg }) {
  const isAi = msg.role === "ai";

  const allSources = msg.results?.length ? msg.results : msg.sources || [];

  return (
    <div
      className={`flex ${isAi ? "justify-start" : "justify-end"} w-full mb-6`}
    >
      <div
        className={`max-w-[95%] md:max-w-[85%] p-4 rounded border ${
          isAi
            ? "bg-[#111] border-[#00ff8822]"
            : "bg-[#00ff8808] border-[#00ff8844]"
        }`}
      >
        <div className="flex items-center gap-2 mb-3 text-[9px] uppercase font-bold opacity-30 tracking-widest">
          <span>{isAi ? ">> AGENT_CORE" : ">> USER_SHELL"}</span>
          <div className="h-[1px] flex-1 bg-[#00ff88] opacity-20"></div>
        </div>
        <div className="text-sm leading-relaxed whitespace-pre-wrap font-mono">
          {msg.content}
          {isAi && (
            <span className="inline-block w-2 h-4 bg-[#00ff88] ml-1 cursor-blink align-middle" />
          )}
        </div>
        {allSources.length > 0 && (
          <div className="mt-4 border-t border-[#00ff8811] pt-4 space-y-2">
            <p className="text-[9px] uppercase opacity-40 mb-2">
              Retrieved Context:
            </p>
            {allSources.map((item, idx) => (
              <details
                key={idx}
                className="group border border-[#00ff8822] bg-black rounded overflow-hidden"
              >
                <summary className="cursor-pointer p-2 text-[10px] font-mono text-[#00ff88cc] hover:bg-[#00ff8811] flex justify-between items-center transition-colors">
                  <span>{item.file_path}</span>
                  <span className="opacity-30 group-open:rotate-180 transition-transform duration-200">
                    ▼
                  </span>
                </summary>
                <pre className="p-3 text-[11px] overflow-x-auto custom-scrollbar bg-[#050505] text-[#00ff8888] border-t border-[#00ff8811]">
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
