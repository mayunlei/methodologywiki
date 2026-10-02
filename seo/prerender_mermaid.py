#!/usr/bin/env python3
"""把正文里未注释的 ```mermaid 代码块预渲染为 PNG（避免读者浏览器从 CDN 加载 mermaid 再渲染）。
源码另存为同目录 <文件名>-mermaid-live-N.mmd，代码块替换为图片引用。
用法：python3 seo/prerender_mermaid.py <目录...>
"""
import os, re, subprocess, sys, tempfile, json

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FENCE = re.compile(r"^([ \t]*)```mermaid[ \t]*\n(.*?)^[ \t]*```[ \t]*$", re.M | re.S)


def render(src, out_png):
    with tempfile.TemporaryDirectory() as td:
        mmd = os.path.join(td, "in.mmd")
        cfg = os.path.join(td, "pptr.json")
        open(mmd, "w", encoding="utf-8").write(src)
        json.dump({"executablePath": CHROME, "args": ["--no-sandbox", "--no-proxy-server"]}, open(cfg, "w"))
        r = subprocess.run(["mmdc", "-i", mmd, "-o", out_png, "-b", "white", "-s", "2",
                            "-p", cfg], capture_output=True, text=True, timeout=120)
        return r.returncode == 0 and os.path.exists(out_png), (r.stderr or r.stdout)[-300:]


def sanitize(src):
    """节点文字里的英文直引号会让 mermaid 解析失败：换成弯引号（成对交替）。
    冒号、分号在标签里也可能出错，一并换成全角形式。"""
    out, opening = [], True
    for line in src.split("\n"):
        # 只改 (...) / [...] / {...} 标签内部的字符
        def fix_label(m):
            nonlocal opening
            inner = m.group(2)
            chars = []
            for ch in inner:
                if ch == '"':
                    chars.append("“" if opening else "”"); opening = not opening
                else:
                    chars.append(ch)
            inner = "".join(chars).replace(";", "；")
            return m.group(1) + inner + m.group(3)
        line = re.sub(r"(\()([^()]*?)(\))", fix_label, line)
        line = re.sub(r"(\[)([^\[\]]*?)(\])", fix_label, line)
        out.append(line)
    return "\n".join(out)


def alt_text(src, stem):
    m = re.search(r"subgraph\s+[\"']?([^\"'\n]+?)[\"']?\s*$", src, re.M)
    return (m.group(1).strip() if m else stem.replace("-", " "))


def process(path):
    text = open(path, encoding="utf-8").read()
    # 只处理不在 HTML 注释里的代码块
    comments = [(m.start(), m.end()) for m in re.finditer(r"<!--.*?-->", text, re.S)]
    in_comment = lambda pos: any(a <= pos < b for a, b in comments)
    stem = os.path.splitext(os.path.basename(path))[0]
    d = os.path.dirname(path)
    out, last, n, ok, fail = [], 0, 0, 0, []
    for m in FENCE.finditer(text):
        if in_comment(m.start()):
            continue
        n += 1
        indent, src = m.group(1), m.group(2)
        base = "%s-mermaid-live-%d" % (stem, n)
        png = os.path.join(d, base + ".png")
        good, err = render(src, png)
        if not good:
            src = sanitize(src)
            good, err = render(src, png)
        if not good:
            fail.append((n, err.strip().split("\n")[-1][:120]))
            continue
        open(os.path.join(d, base + ".mmd"), "w", encoding="utf-8").write(src)
        out.append(text[last:m.start()])
        out.append("%s![%s](./%s.png)\n\n%s<!-- mermaid 源文件：%s.mmd -->" % (
            indent, alt_text(src, stem), base, indent, base))
        last = m.end()
        ok += 1
    if ok:
        out.append(text[last:])
        open(path, "w", encoding="utf-8").write("".join(out))
    return ok, fail


if __name__ == "__main__":
    tot_ok, tot_fail = 0, []
    for root in sys.argv[1:]:
        for dp, _, fs in os.walk(root):
            if "/site" in dp:
                continue
            for f in sorted(fs):
                if f.endswith(".md"):
                    p = os.path.join(dp, f)
                    if "```mermaid" not in open(p, encoding="utf-8").read():
                        continue
                    ok, fail = process(p)
                    tot_ok += ok
                    tot_fail += [(p, n, e) for n, e in fail]
                    if ok or fail:
                        print("  %-60s 成功 %d%s" % (p[-60:], ok, ("，失败 %d" % len(fail)) if fail else ""), flush=True)
    print("预渲染完成：成功 %d，失败 %d" % (tot_ok, len(tot_fail)))
    for p, n, e in tot_fail:
        print("  ✗ %s #%d：%s" % (p, n, e))
