"""File-backed catalogue of prompts and skills. No external services required."""
from __future__ import annotations

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = ("02-prompts", "03-skills")
REQUIRED = {"id", "name", "category", "status", "description"}


def load_catalogue(root: Path = ROOT) -> list[dict]:
    """Load YAML metadata. Skip malformed entries and expose their errors in tests."""
    entries: list[dict] = []
    for dirname in DIRECTORIES:
        for path in sorted((root / dirname).rglob("metadata.yaml")):
            raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            if not isinstance(raw, dict) or not REQUIRED.issubset(raw):
                raise ValueError(f"Invalid metadata fields: {path}")
            item = dict(raw)
            item["kind"] = "Prompt" if dirname == "02-prompts" else "Skill"
            item["path"] = str(path.parent.relative_to(root))
            readme = path.parent / "README.md"
            skill = path.parent / "SKILL.md"
            prompt = path.parent / "prompt.md"
            preview = prompt if prompt.exists() else skill if skill.exists() else readme
            item["content"] = preview.read_text(encoding="utf-8") if preview.exists() else ""
            entries.append(item)
    return entries


def search_catalogue(items: list[dict], query: str = "", category: str = "all") -> list[dict]:
    q = query.casefold().strip()
    result = []
    for item in items:
        if category != "all" and item.get("category") != category:
            continue
        haystack = " ".join(str(item.get(key, "")) for key in ("id", "name", "description", "category", "tags"))
        if q in haystack.casefold():
            result.append(item)
    return result
