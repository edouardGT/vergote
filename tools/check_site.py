"""Checks every page: local links, images (incl. srcset), in-page anchors, one <h1>, no duplicate ids.
Usage: python3 -m http.server 8793 (in the repo), then: python3 tools/check_site.py [http://127.0.0.1:8793/]"""
import html.parser
import pathlib
import re
import sys
import urllib.request

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8793/"
ROOT = pathlib.Path(__file__).resolve().parent.parent


class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        for k in ("href", "src"):
            v = a.get(k)
            if v and not v.startswith(("http", "mailto:", "tel:")):
                self.refs.append(v)
        for k in ("srcset", "imagesrcset"):
            if a.get(k):
                self.refs += [part.strip().split(" ")[0] for part in a[k].split(",")]


problems, seen = [], set()
pages = sorted(p.name for p in ROOT.glob("*.html"))
for name in pages:
    src = (ROOT / name).read_text(encoding="utf-8")
    p = Page()
    p.feed(src)
    for r in p.refs:
        if r.startswith("#"):
            if r[1:] and r[1:] not in p.ids:
                problems.append((name, "missing anchor", r))
            continue
        url = BASE + r.lstrip("/") if r.startswith("/") else BASE + ("" if r == "./" else r)
        if url in seen:
            continue
        seen.add(url)
        try:
            code = urllib.request.urlopen(url).status
        except Exception as e:  # noqa: BLE001
            code = str(e)
        if code != 200:
            problems.append((name, r, code))
    if src.count("<h1") != 1:
        problems.append((name, "h1 count", src.count("<h1")))
    ids = re.findall(r'\sid="([^"]+)"', src)
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        problems.append((name, "duplicate ids", dup))

print(f"checked {len(seen)} URLs on {len(pages)} pages; problems: {problems or 'none'}")
sys.exit(1 if problems else 0)
