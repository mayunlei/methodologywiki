#!/usr/bin/env python3
"""修复“HTML 注释里的 mermaid 源码含 -->，导致注释提前结束、源码泄露到正文”的问题。

做法：找出独占一行的 <!-- 与 --> 配对的注释块（支持嵌套），如果块内含有行内 --> 或 mermaid
源码，就把 mermaid 源码另存为同目录的 .mmd 文件，原位置换成一行引用注释。
用法：python3 seo/fix_mermaid_comments.py [--dry-run] <目录...>
"""
import os, re, sys

def blocks(lines):
    stack, out = [], []
    for i, l in enumerate(lines):
        s = l.strip()
        if s == "<!--":
            stack.append(i)
        elif s == "-->" and stack:
            start = stack.pop()
            if not stack:
                out.append((start, i))
    return out

def extract_mermaid(body):
    m = re.search(r"```mermaid\s*\n(.*?)```", body, re.S)
    if m:
        return m.group(1).rstrip() + "\n"
    keep = [l for l in body.split("\n") if l.strip() not in ("<!--", "-->") and not l.strip().startswith("![")]
    return "\n".join(keep).strip() + "\n"

def fix(path, dry):
    lines = open(path, encoding="utf-8").read().split("\n")
    changed, n = False, 0
    for start, end in reversed(blocks(lines)):
        body = "\n".join(lines[start + 1:end])
        risky = re.search(r"\S\s*-->", body) or re.search(r"\b(graph|flowchart|subgraph|mermaid)\b", body)
        if not risky:
            continue
        n += 1
        stem = os.path.splitext(os.path.basename(path))[0]
        name = "%s-mermaid-src-%d.mmd" % (stem, n)
        if not dry:
            with open(os.path.join(os.path.dirname(path), name), "w", encoding="utf-8") as fh:
                fh.write(extract_mermaid(body))
        lines[start:end + 1] = ["<!-- mermaid 源文件：%s -->" % name]
        changed = True
    if changed and not dry:
        open(path, "w", encoding="utf-8").write("\n".join(lines))
    return n

if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    total = files = 0
    for root in [a for a in sys.argv[1:] if a != "--dry-run"]:
        for dp, _, fs in os.walk(root):
            if "/site" in dp: continue
            for f in fs:
                if f.endswith(".md"):
                    k = fix(os.path.join(dp, f), dry)
                    if k: files += 1; total += k
    print("%s：%d 个文件，%d 个注释块" % ("将处理" if dry else "已处理", files, total))
