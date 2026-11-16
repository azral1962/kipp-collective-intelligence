# Three-week implementation plan

| Week | Work | Exit criterion |
|---|---|---|
| 1 | Approve charter; assign teams; add templates; run catalogue; first prompt/skill drafts | Each team has issue, reviewer, and initial contribution |
| 2 | Cross-team testing; evidence logs; search improvements; optional bot proof of concept | First 5 prompts + 3 skills tested; catalogue usable |
| 3 | Complete minimum 10 tested prompts + 6 skills; integrated demo; usability test; handover | Documented MVP and student reflections |

## Engineering increments
1. Base file-backed catalogue and search — implemented starter.
2. YAML metadata checks + CI validation.
3. Cross-links among concepts, cases and workflows.
4. Controlled Telegram bot `/find` with privacy declaration.
5. Optional `/ask` via local Ollama, citation-first.
6. Optional `/summary` on explicitly retained conversation windows with announced consent.

## Scope discipline
No feature is done without an example, independent test, sources, and human review. Prefer working simpler tools to partially configured complex infrastructure.
