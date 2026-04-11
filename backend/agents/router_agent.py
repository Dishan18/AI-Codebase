from services.llm_service import generate_answer
from agents.search_agent import code_search
from agents.explainer_agent import explain
from agents.debug_agent import debug
from agents.summary_agent import summarize

KEYWORDS_DEBUG = {"error", "bug", "fix", "exception", "traceback", "fail"}
KEYWORDS_EXPLAIN = {"how", "what", "explain", "why", "working"}
KEYWORDS_SUMMARY = {"summary", "overview"}

def rule_classify(query: str):
    q = query.lower()
    if any(k in q for k in KEYWORDS_DEBUG):
        return "debug"
    if any(k in q for k in KEYWORDS_EXPLAIN):
        return "explain"
    if any(k in q for k in KEYWORDS_SUMMARY):
        return "summary"
    if len(q.split()) <= 2:
        return "search"
    return None

def llm_classify(query: str):
    prompt = f"Classify the query into one of: explain, debug, summary, search. Return only one word.\n\nQuery: {query}"
    resp = generate_answer(prompt, []).strip().lower()
    for k in ["debug", "summary", "search", "explain"]:
        if k in resp:
            return k
    return "explain"

def classify_query(query: str):
    r = rule_classify(query)
    return r if r else llm_classify(query)

def route_query(query, context_chunks, history):
    intent = classify_query(query)
    if intent == "search":
        return code_search(query, context_chunks)
    if intent == "debug":
        return debug(query, context_chunks, history)
    if intent == "summary":
        return summarize(query, context_chunks, history)
    
    return explain(query, context_chunks, history)