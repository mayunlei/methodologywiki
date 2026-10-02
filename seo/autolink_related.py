#!/usr/bin/env python3
"""把英文文章“Extensions and Connections”小节里加粗的方法名，链接到本站对应页面。
只处理形如  *   **Name**: ...  /  1. **Name**: ...  的条目；已是链接的跳过。
用法：python3 seo/autolink_related.py [--dry-run]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from enrich import resolve_links

ROOT = "docs/en"
ALIASES = {  # 规范化名称 -> 文件名（不含 .md）
    "5 whys": "5-Whys-Tutorial-en", "five whys": "5-Whys-Tutorial-en",
    "ishikawa diagram": "Fishbone-Diagram-Tutorial-en", "cause and effect diagram": "Fishbone-Diagram-Tutorial-en",
    "mece": "Logic-Tree-Tutorial-en", "mece principle": "Logic-Tree-Tutorial-en", "issue tree": "Logic-Tree-Tutorial-en",
    "pareto principle": "Pareto-Analysis-Tutorial-en", "80/20 rule": "Pareto-Analysis-Tutorial-en",
    "minimum viable product": "MVP-Tutorial-en", "mvp": "MVP-Tutorial-en",
    "getting things done": "GTD-Tutorial-en", "gtd": "GTD-Tutorial-en",
    "tqm": "Total-Quality-Management-Tutorial-en", "okrs": "OKR-Tutorial-en",
    "kpis": "KPI-Tutorial-en", "key performance indicators": "KPI-Tutorial-en",
    "objectives and key results": "OKR-Tutorial-en", "smart principle": "SMART-Goals-Tutorial-en",
    "smart": "SMART-Goals-Tutorial-en", "mind map": "Mind-Mapping-Tutorial-en",
    "pestle": "PESTEL-Analysis-Tutorial-en", "pest analysis": "PESTEL-Analysis-Tutorial-en",
    "five forces": "Porters-Five-Forces-Tutorial-en", "lean": "Lean-Operations-Tutorial-en",
    "lean production": "Lean-Operations-Tutorial-en", "lean manufacturing": "Lean-Operations-Tutorial-en",
    "user personas": "User-Persona-Tutorial-en", "personas": "User-Persona-Tutorial-en",
    "customer journey map": "User-Journey-Map-Tutorial-en", "ab testing": "AB-Testing-Tutorial-en",
    "a/b testing": "AB-Testing-Tutorial-en", "agile development": "Agile-Tutorial-en",
    "systems thinking": "Iceberg-Model-Tutorial-en", "raci": "RACI-Matrix-Tutorial-en",
    "mixed methods research": "Mixed-Methods-Research-Tutorial-en", "devops": "intro-to-devops-en",
    "lean startup": "MVP-Tutorial-en", "the lean startup": "MVP-Tutorial-en",
    "lean and agile": "Agile-Tutorial-en",
}
DROP = re.compile(r"\b(the|model|analysis|method|methodology|technique|tutorial|framework|"
                  r"principle|diagram|matrix|thinking)\b")


def norm(s):
    s = re.sub(r"\(.*?\)", "", s.lower()).replace("’", "'").replace("'s", "")
    return re.sub(r"\s+", " ", s).strip(" :.-")


def key(s):
    return re.sub(r"\s+", " ", DROP.sub("", norm(s))).strip()


def build_index():
    idx = {}
    for dp, _, fs in os.walk(ROOT):
        for f in fs:
            if f.endswith(".md") and f != "index.md":
                t = open(os.path.join(dp, f), encoding="utf-8").read()
                m = re.search(r"^# (.+)$", t, re.M)
                if m:
                    idx.setdefault(key(m.group(1)), f[:-3])
                    idx.setdefault(norm(m.group(1)), f[:-3])
    for a, stem in ALIASES.items():
        idx[a] = stem
        idx.setdefault(key(a), stem)
    return idx


def main(dry):
    idx = build_index()
    total = files = 0
    sec_re = re.compile(r"^## Extensions? and Connections?\s*$(.*?)(?=^## |^---\s*$|\Z)", re.M | re.S)
    item_re = re.compile(r"^(\s*(?:[*+-]|\d+\.)\s+)\*\*(?!\[)([^*\n]+?)\*\*", re.M)
    for dp, _, fs in os.walk(ROOT):
        for f in fs:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            text = open(p, encoding="utf-8").read()
            m = sec_re.search(text)
            if not m:
                continue
            sec, n = m.group(1), 0
            def rep(mm):
                nonlocal n
                name = mm.group(2)
                stem = idx.get(norm(name)) or idx.get(key(name))
                if not stem or stem == f[:-3]:
                    return mm.group(0)
                n += 1
                return "%s**[[%s|%s]]**" % (mm.group(1), name, stem)
            new_sec = item_re.sub(rep, sec)
            if n:
                new = text[:m.start(1)] + resolve_links(p, new_sec) + text[m.end(1):]
                if not dry:
                    open(p, "w", encoding="utf-8").write(new)
                total += n; files += 1
    print("%s：%d 个文件，%d 个方法名加上链接" % ("将处理" if dry else "已处理", files, total))


if __name__ == "__main__":
    main("--dry-run" in sys.argv)
