#!/usr/bin/env python3
"""检查 Python-Markdown 下会渲染错误的写法：
  1. 段落文字下一行直接开始列表（缺空行）-> 列表被并进段落，显示成一行纯文本
  2. 文字下一行是 ---                     -> 被解析成二级标题（setext），而不是分隔线
  3. 标题下一行直接开始列表/段落          -> 通常无害，不报
用法：python3 seo/lint_markdown.py [--fix] <目录...>
"""
import re, sys, os
LIST = re.compile(r"^(\s{0,3})([*+-]|\d+\.)\s+\S")
FENCE = re.compile(r"^\s*(```|~~~)")

def scan(path, fix=False):
    lines = open(path, encoding="utf-8").read().split("\n")
    out, issues, in_fence = [], [], False
    start = 0
    if lines and lines[0].strip() == "---":            # front-matter
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end:
            out.extend(lines[:end + 1]); start = end + 1
    for i in range(start, len(lines)):
        cur = lines[i]
        prev = out[-1] if out else ""
        if FENCE.match(cur):
            in_fence = not in_fence
        if not in_fence and prev.strip() and not prev.lstrip().startswith(("#", "|", ">", "<", "!")):
            prev_is_list = bool(LIST.match(prev)) or prev.startswith((" ", "\t"))
            if LIST.match(cur) and not prev_is_list and not cur.startswith(" "):
                issues.append((i + 1, "列表前缺空行"))
                if fix: out.append("")
            elif re.fullmatch(r"\s*-{3,}\s*", cur) and not LIST.match(prev):
                issues.append((i + 1, "--- 紧贴文字（会变成标题）"))
                if fix: out.append("")
        out.append(cur)
    if fix and issues:
        open(path, "w", encoding="utf-8").write("\n".join(out))
    return issues

if __name__ == "__main__":
    fix = "--fix" in sys.argv
    roots = [a for a in sys.argv[1:] if a != "--fix"]
    total, files = 0, 0
    for root in roots:
        for dp, _, fs in os.walk(root):
            if "/site" in dp: continue
            for f in fs:
                if f.endswith(".md"):
                    iss = scan(os.path.join(dp, f), fix)
                    if iss:
                        files += 1; total += len(iss)
    print("%s：%d 个文件，%d 处" % ("已修复" if fix else "发现问题", files, total))
    sys.exit(1 if total and not fix else 0)
