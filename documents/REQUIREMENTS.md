# Requirements / acceptance criteria

## P0 — Mandatory
- R1: Read prompt/skill/workflow entries from Markdown and YAML locally.
- R2: Search by title, code, description or tags and filter by category.
- R3: Display each entry's instructions, status, author placeholder, source and files.
- R4: Run without secrets, Telegram, cloud APIs, or Ollama.
- R5: Include documented contribution and cross-team review process.
- R6: Record the provenance and validation status of each published package.
- R7: Maintain safe content policy: no personal data in public repo; review AI outputs.

## P1 — Useful after P0
- R8: Add examples/assessment evidence view.
- R9: Telegram `/find` and `/ask` with explicit opt-in and allowed chat IDs.
- R10: Local Ollama RAG with source traceability and graceful fallback.
- R11: Admin moderation and audit log in private environment.

## Acceptance scenario
Given a clone without secrets, `pip install -e '.[dev]'` then `streamlit run app/streamlit_app.py` displays sample packages; `pytest -q` passes. A student can find ST-02 and see its template and status. No demo user information is real.
