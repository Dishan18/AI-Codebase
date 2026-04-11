const BASE_URL = "http://127.0.0.1:8000";

export const ingestRepo = async (repo_url) => {
  const response = await fetch(`${BASE_URL}/ingest-repo`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ repo_url }),
  });
  if (!response.ok) throw new Error("Ingestion failed");
  return response.json();
};

export const queryRepo = async (query, top_k = 15) => {
  const response = await fetch(`${BASE_URL}/query-repo`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query, top_k }),
  });
  if (!response.ok) throw new Error("Query failed");
  return response.json();
};
