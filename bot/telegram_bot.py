"""Opt-in Telegram bot: commands only, no message retention or LLM access."""
from __future__ import annotations
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
from kipp.catalog import load_catalogue, search_catalogue

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
ALLOWED = {int(x.strip()) for x in os.getenv("TELEGRAM_ALLOWED_CHAT_IDS", "").split(",") if x.strip()}
dp = Dispatcher()


def permitted(message: Message) -> bool:
    return bool(ALLOWED) and message.chat.id in ALLOWED


@dp.message(Command("help"))
async def help_command(message: Message) -> None:
    if not permitted(message):
        return
    await message.answer("KIPP bot pilot: /find <keyword>. No chat messages are saved.")


@dp.message(Command("find"))
async def find_command(message: Message) -> None:
    if not permitted(message):
        return
    query = (message.text or "").partition(" ")[2].strip()
    hits = search_catalogue(load_catalogue(), query)[:5]
    if not query:
        await message.answer("Usage: /find <keyword>")
        return
    if not hits:
        await message.answer("No catalogue match. Ask peers or suggest a contribution.")
        return
    await message.answer("Matching draft packages:\n" + "\n".join(
        f'{x["id"]}: {x["name"]} [{x["status"]}]' for x in hits
    ))


async def main() -> None:
    if not TOKEN or not ALLOWED:
        raise SystemExit("Set TELEGRAM_BOT_TOKEN and TELEGRAM_ALLOWED_CHAT_IDS first")
    async with Bot(TOKEN) as bot:
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
