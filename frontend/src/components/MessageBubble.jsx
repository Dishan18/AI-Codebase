export default function MessageBubble({ msg }) {
  const isUser = msg.role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-xl p-3 border text-sm whitespace-pre-wrap ${
          isUser
            ? "bg-green-500 text-black"
            : "border-green-700 bg-black text-green-400"
        }`}
      >
        {/* Main answer */}
        {msg.content && <div>{msg.content}</div>}

        {/* Sources */}
        {msg.sources && (
          <details className="mt-2">
            <summary className="cursor-pointer text-xs opacity-70">
              Sources
            </summary>
            {msg.sources.map((s, i) => (
              <pre key={i} className="text-xs mt-2 overflow-x-auto">
                {s.content}
              </pre>
            ))}
          </details>
        )}

        {/* Search results (IMPORTANT FIX) */}
        {msg.results && (
          <div className="mt-2 space-y-2">
            {msg.results.map((r, i) => (
              <pre key={i} className="text-xs overflow-x-auto">
                {r.snippet}
              </pre>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
