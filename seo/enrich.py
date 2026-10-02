#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给已有文章增补内容，而不重写原文。

enrich(path, title=..., description=..., tldr=[...], sections="...", replacements=[(old, new)])
  - title/description：写入 front-matter（搜索标题与描述）
  - tldr：要点列表，作为提示框插在第一个二级标题之前
  - sections：新增章节（Markdown），插在“延伸与关联”类章节之前；没有则插在文末来源说明之前
  - replacements：对原文做精确替换（修正错误），找不到原文会报错
"""
import re

TLDR_TITLE = {"en": "Key takeaways", "zh": "要点速览"}
ANCHORS = [r"^## Extensions? and Connections?\s*$", r"^## 延伸与关联\s*$", r"^## Related\b.*$"]


def _yaml(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


import os

DOCS_ROOTS = ("docs/en", "zh/docs", "ja/docs", "ko/docs", "es/docs", "fr/docs", "de/docs",
              "pt/docs", "ru/docs", "nl/docs", "sv/docs", "vi/docs")


def _docs_root(path):
    p = path.replace(os.sep, "/")
    for r in DOCS_ROOTS:
        i = p.find(r + "/")
        if i >= 0:
            return p[:i + len(r)]
    raise ValueError("无法判断 docs 根目录：%s" % path)


def resolve_links(path, text):
    """[[链接文字|目标文件名（不含 .md）]] -> 相对路径的 Markdown 链接。"""
    root = _docs_root(path)
    index = {}
    for dp, _, fs in os.walk(root):
        for f in fs:
            if f.endswith(".md"):
                index.setdefault(f[:-3], os.path.join(dp, f))
    def rep(m):
        label, stem = m.group(1), m.group(2).strip()
        if stem not in index:
            raise ValueError("%s: 链接目标不存在：%s" % (path, stem))
        rel = os.path.relpath(index[stem], os.path.dirname(path)).replace(os.sep, "/")
        return "[%s](%s)" % (label, rel)
    return re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", rep, text)


def enrich(path, title=None, description=None, tldr=None, sections=None,
           replacements=None, lang="en"):
    text = open(path, encoding="utf-8").read()
    if sections:
        sections = resolve_links(path, sections)
    if tldr:
        tldr = [resolve_links(path, t) for t in tldr]
    replacements = [(o, resolve_links(path, n)) for o, n in (replacements or [])]
    for old, new in replacements:
        if old not in text:
            raise ValueError("%s: 找不到要替换的原文：%r" % (path, old[:60]))
        text = text.replace(old, new, 1)

    body = text
    fm = ""
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4)
        fm, body = text[:end + 5], text[end + 5:]
    if title or description:
        lines = [l for l in fm.strip("-\n").split("\n") if l and not l.startswith(("title:", "description:"))]
        if title:
            lines.insert(0, "title: %s" % _yaml(title))
        if description:
            lines.insert(1 if title else 0, "description: %s" % _yaml(description))
        fm = "---\n%s\n---\n\n" % "\n".join(lines)
        body = body.lstrip("\n")

    if tldr and 'class="admonition abstract"' not in body and '!!! abstract' not in body:
        block = '!!! abstract "%s"\n\n%s\n\n' % (
            TLDR_TITLE.get(lang, TLDR_TITLE["en"]),
            "\n".join("    - %s" % t for t in tldr))
        m = re.search(r"^## ", body, re.M)
        pos = m.start() if m else len(body)
        body = body[:pos] + block + body[pos:]

    if sections:
        sec = sections.strip("\n") + "\n\n"
        pos = None
        for a in ANCHORS:
            m = re.search(a, body, re.M)
            if m:
                pos = m.start()
                break
        if pos is None:
            m = list(re.finditer(r"^---\s*$", body, re.M))
            pos = m[-1].start() if m else len(body)
        body = body[:pos] + sec + body[pos:]

    open(path, "w", encoding="utf-8").write(fm + body)
    return path
