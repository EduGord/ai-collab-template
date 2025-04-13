# ✅ org-agent Checklist

## 🧭 Purpose
Manages project knowledge and organization through semantic classification, retrieval, summarization, and indexing.

---

## 📚 Knowledge Ingestion
- [ ] Auto-tag and classify every document added to `docs/`, `features/`, and `plans/`
- [ ] Extract and store metadata in `memory/org-index.json`
- [ ] Build semantic search vectors for long-form and multi-format content

---

## 🧠 Semantic Retrieval
- [ ] Respond to `knowledge-query-issued` triggers with top-ranked matches
- [ ] Use relevance, recency, and source context to weight search results
- [ ] Present query results with summaries, tags, and confidence score

---

## 🧾 Summarization
- [ ] Detect new or updated long-form content
- [ ] Generate section-level summaries and store alongside document metadata
- [ ] Append document overview to `memory/summary-cache.json`

---

## 🔁 Adaptive Indexing
- [ ] Track usage patterns and access frequency
- [ ] Adjust semantic weights for hot documents or stale categories
- [ ] Flag under-referenced documents for potential archival

---

## 🔂 Integration
- [ ] Bootstrap via `task-design-org-agent-spec` and `task-semantic-retrieval-index`
- [ ] Output results to `org-knowledge-agent-bootstrap` linked plan
- [ ] Enable downstream agents (`insight-agent`, `planner-agent`) to reuse knowledge artifacts

---

## 🧬 Lifecycle Awareness
- [ ] Phase `init`: scan and classify all documents
- [ ] Phase `active`: ingest and answer queries in real time
- [ ] Phase `reflecting`: output indexing strategy update
- [ ] Phase `archived`: freeze and export document taxonomy
