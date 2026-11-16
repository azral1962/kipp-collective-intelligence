# KIPP Collective Academic Intelligence (KIPP-CAI)

**60+ students · 3 weeks · One collective learning system**

A collaborative, cross-course library of **academic prompts, reusable AI skills, workflows, knowledge, and problem-solving cases**. The project is an educational pilot for the Interpersonal & Public Communication (KIPP) course. Communication and collaborative learning come first; software is supporting infrastructure.

## Start in 5 minutes

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -e '.[dev]'
streamlit run app/streamlit_app.py
```

Run tests: `pytest -q`. Launch the catalogue without Ollama, database credentials or Telegram access. Sample records are explicitly illustrative.

## Repository map

- `00-project/` charter, roles, three-week milestones
- `01-knowledge/` taxonomy and knowledge examples
- `02-prompts/` reusable prompt patterns (Study, Research, Design, Implementation, Paper)
- `03-skills/` executable/reusable skills (Python, visualization, tables, presentations, video, documents)
- `04-workflows/` multi-step academic workflows
- `05-problem-solving/` problems, solutions, case studies, reflections
- `06-examples/` subject-specific examples
- `07-community/` forum guidelines, peer-review workflow
- `08-application/` integration notes and future backend
- `09-quality/` quality gates and evidence
- `10-showcase/` demo plan and final reports
- `app/` working Streamlit read-only catalogue
- `bot/` opt-in Telegram bot stub (does not collect messages automatically)
- `templates/` submission templates; `.github/` CI and issue/PR templates

## First week

1. Agree on the [Project Charter](00-project/project-charter.md), assign ten teams.
2. Open GitHub Issues from [`docs/BACKLOG.md`](docs/BACKLOG.md).
3. Contribute through branch → Pull Request → peer review → merge.
4. Curate prompt/skill packages and link evidence of tests.
5. Keep private student data and secrets outside this repository.

## Project policy

- Do not automatically publish Telegram discussions. Monitor only a group whose members have been informed of the bot and its data policy.
- Human reviewers approve academic content; AI responses must acknowledge insufficient evidence.
- Do not upload unpublished exam questions, copyrighted materials without permission, or API credentials.
- `main` is curated; use Pull Requests. Do not require paid AI accounts.

See [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md) and [AGENTS.md](AGENTS.md) before asking a coding agent to change the project.
