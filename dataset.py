import json, re
from dataclasses import dataclass
from playwright.sync_api import Page

@dataclass
class QAItem:
    term: str
    definition: str

def extract_set_data(page: Page):
    scripts = page.query_selector_all("script")
    for s in scripts:
        txt = s.inner_text() or ""
        if "setPageData" in txt:
            m = re.search(r'setPageData\\"\s*:\\s*({.*?})\\s*,\\s*\"classes', txt)
            if m:
                try:
                    raw = m.group(1).replace('\\\"','"')
                    data = json.loads(raw)
                    items = []
                    for term in data.get("terms", []):
                        items.append(QAItem(term.get("word",""), term.get("definition","")))
                    return items
                except Exception:
                    continue
    return []
