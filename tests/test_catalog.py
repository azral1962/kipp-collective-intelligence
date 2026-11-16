from pathlib import Path
from kipp.catalog import load_catalogue, search_catalogue


def test_catalogue_loads_examples():
    items = load_catalogue()
    assert {"ST-02", "PY-03"}.issubset({x["id"] for x in items})
    assert all(x["status"] == "draft" for x in items)


def test_search_by_code_and_category():
    items = load_catalogue()
    hits = search_catalogue(items, "ST-02", "study")
    assert len(hits) == 1
    assert hits[0]["name"] == "Socratic Tutor"
    assert search_catalogue(items, "ST-02", "python") == []


def test_metadata_has_existing_source_path():
    from kipp.catalog import ROOT
    for item in load_catalogue():
        assert (ROOT / item["path"]).is_dir()
