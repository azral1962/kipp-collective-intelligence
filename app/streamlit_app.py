"""Minimal KIPP catalogue interface with no backend dependency."""
from pathlib import Path
import sys

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kipp.catalog import load_catalogue, search_catalogue  # noqa: E402

st.set_page_config(page_title="KIPP Collective AI Library", page_icon="📚", layout="wide")
st.title("KIPP Collective Academic Intelligence")
st.caption("Prompts · Skills · Workflows · Knowledge · Collaboration")
st.info("Starter demo: sample packages are drafts. Human review is required before publication.")

items = load_catalogue()
categories = sorted({x["category"] for x in items})
search = st.text_input("Search prompt or skill", placeholder="e.g., Socratic Tutor, Python")
category = st.selectbox("Category", ["all", *categories])
visible = search_catalogue(items, search, category)

c1, c2, c3 = st.columns(3)
c1.metric("Catalogue packages", len(items))
c2.metric("Results", len(visible))
c3.metric("Verified packages", sum(x["status"] == "verified" for x in items))

for item in visible:
    with st.expander(f'{item["id"]} · {item["name"]} — {item["status"]}'):
        st.write(item["description"])
        st.caption(f'{item["kind"]} · {item["category"]} · v{item.get("version", "?")} · {item["path"]}')
        st.markdown(item["content"])

st.divider()
st.markdown("**How to contribute:** open a GitHub Issue, copy a template, submit a Pull Request and obtain an independent review.")
st.markdown("See `CONTRIBUTING.md`, `00-project/project-charter.md`, and `docs/BACKLOG.md`.")
