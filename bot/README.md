# Optional Telegram AI Forum Facilitator

This folder deliberately contains only an **opt-in** `/help` and `/find` skeleton for a specific allowed chat. It does not monitor/save messages, and it does not use the LLM yet.

1. Agree a privacy policy with group members and administrator.
2. Set token and allowed chat IDs in local `.env` (`.env.example` is safe to commit).
3. Install: `pip install -e '.[bot]'`.
4. Run: `python -m bot.telegram_bot` (after setting env vars).

Future `/ask`: local Ollama with citations to verified repository content; future `/summary`: only under explicit consent, retention, and moderator policy.
