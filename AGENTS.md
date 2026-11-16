# Instructions for coding agents

## Mission
Create a sustainable, student-maintained learning commons for KIPP students, usable in later courses. Focus on communication, reproducible academic workflows, evidence and peer review; avoid overengineering.

## Three-week MVP
1. Browsable searchable prompt/skill/workflow catalogue, sourced from Markdown+YAML files.
2. Contributor metadata, version, verification status, documentation and examples.
3. Transparent review via GitHub Issues/Pull Requests.
4. An optional Telegram bot that answers only on request, retrieving from approved content.
5. An optional local AI provider (Ollama); never make cloud inference the silent default.

## Engineering rules
- FIRST inspect repository and read `docs/PROJECT_CONTEXT.md`, `docs/REQUIREMENTS.md`, `docs/ARCHITECTURE.md`.
- Propose a small plan with acceptance criteria before modifying multiple files.
- Keep app functional without Telegram token, Ollama, or PostgreSQL.
- Prefer small commits/PRs and Python 3.11+, type hints, pytest, Streamlit.
- Unit tests for content parsing, searching, validation; mock network integrations.
- Never invent experimental results, citations, or test outcomes.
- Do not store personal Telegram text, usernames or private transcripts in the public repository.
- No irreversible destructive operation, external publication or private data transfer without human approval.
- Mark AI-generated academic content as draft until human review.
- Any agentic code must document permission boundaries, inputs, outputs and failure modes.
- Update docs and tests with each new feature. Do not refactor unrelated files.

## Definition of done
Documented feature; tests passing; source/provenance recorded; peer review completed; demo reproducible; risks stated.
