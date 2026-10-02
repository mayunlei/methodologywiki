#!/usr/bin/env python3
"""构建产物 SEO 自检：sitemap 可达性、canonical 一致性、描述唯一性、
hreflang 互指、结构化数据合法性、站内相对链接与静态资源完整性。"""
import html, json, os, re, sys
from collections import Counter
from urllib.parse import unquote, urljoin, urlparse

sys.path.insert(0, os.path.dirname(__file__))
from postprocess import find_canonical, find_description, RE_LINK_TAG, tag_attrs  # noqa

root = os.path.abspath(sys.argv[1]); base = "https://methodologywiki.com"
fails, warns = [], []

def url_to_file(u):
    p = unquote(urlparse(u).path)
    f = os.path.join(root, p.lstrip("/"))
    return os.path.join(f, "index.html") if p.endswith("/") else f

# 1. sitemap index -> 各语言 sitemap -> 每个 URL 都有对应文件
idx = open(os.path.join(root, "sitemap.xml"), encoding="utf-8").read()
subs = re.findall(r"<loc>([^<]+)</loc>", idx)
all_urls = []
for sm in subs:
    xml = open(url_to_file(sm), encoding="utf-8").read()
    all_urls += re.findall(r"<loc>([^<]+)</loc>", xml)
missing = [u for u in all_urls if not os.path.exists(url_to_file(u))]
print("sitemap：%d 个子 sitemap，%d 个 URL，缺文件 %d" % (len(subs), len(all_urls), len(missing)))
if missing: fails.append("sitemap 中 %d 个 URL 无对应页面，如 %s" % (len(missing), missing[:2]))

# 2. 逐页检查
descs, n_pages, bad_canon, bad_ld, broken_href = Counter(), 0, [], 0, Counter()
hreflang_pairs = {}
for u in all_urls:
    f = url_to_file(u); s = open(f, encoding="utf-8", errors="ignore").read(); n_pages += 1
    c = find_canonical(s)
    if c != u: bad_canon.append((u, c))
    _, d = find_description(s); descs[d] += 1
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try: json.loads(m.group(1))
        except Exception: bad_ld += 1
    alts = {}
    for m in RE_LINK_TAG.finditer(s):
        a = tag_attrs(m.group(0))
        if a.get("rel") == "alternate" and a.get("hreflang"):
            alts[a["hreflang"]] = a["href"]
    hreflang_pairs[u] = alts
    # 站内相对资源/链接（css/js/img/页面）是否存在；脚本体内的字符串不算引用
    s = re.sub(r"<script\b(?![^>]*\bsrc=)[^>]*>.*?</script>", " ", s, flags=re.S | re.I)
    for m in re.finditer(r"""(?:href|src)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'>]+))""", s):
        h = html.unescape(next(g for g in m.groups() if g is not None))
        if h.startswith(("http", "//", "#", "mailto:", "data:", "javascript:")) or not h: continue
        t = urljoin(u, h.split("#")[0].split("?")[0])
        if not t.startswith(base): continue
        tf = url_to_file(t)
        if not os.path.exists(tf) and not os.path.exists(tf + "/index.html"):
            broken_href[unquote(urlparse(t).path)] += 1

# mermaid 源码泄露到正文（例如注释被源码里的 --> 提前结束）
leaks = []
for u in all_urls:
    body = open(url_to_file(u), encoding="utf-8", errors="ignore").read()
    art = body[body.find("<article"):body.find("</article>")]
    art = re.sub(r"<!--.*?-->|<pre\b.*?</pre>|<script\b.*?</script>", "", art, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", " ", art))
    if re.search(r"\b(graph (TD|LR|TB)|flowchart (TD|LR)|subgraph|classDef)\b|\w+ --> \w+", text):
        leaks.append(u)
print("mermaid 源码泄露到正文：%d 页" % len(leaks))
for u in leaks[:5]: print("   ", unquote(u.replace(base, "")))
if leaks: fails.append("%d 页正文里出现了 mermaid 源码" % len(leaks))

dup = {d: n for d, n in descs.items() if n > 1}
print("页面 %d：canonical 不一致 %d，重复描述 %d 组（涉及 %d 页），非法 JSON-LD %d"
      % (n_pages, len(bad_canon), len(dup), sum(dup.values()), bad_ld))
if bad_canon: fails.append("canonical 不一致 %d，如 %s" % (len(bad_canon), bad_canon[:2]))
if bad_ld: fails.append("非法 JSON-LD %d 个" % bad_ld)
if dup: warns.append("重复描述：%s" % [(d[:40], n) for d, n in list(dup.items())[:3]])

# 3. hreflang 互指：A 指向 B，则 B 也必须指回 A（Google 要求双向）
nonrecip = 0
for u, alts in hreflang_pairs.items():
    for lang, v in alts.items():
        if lang == "x-default" or v == u: continue
        back = hreflang_pairs.get(v, {})
        if u not in back.values(): nonrecip += 1
bad = [(u, l, v) for u, alts in hreflang_pairs.items() for l, v in alts.items()
       if l != "x-default" and v != u and u not in hreflang_pairs.get(v, {}).values()]
for u, l, v in bad[:4]:
    print("   非双向: %s\n        -[%s]-> %s\n        回指: %s" % (
        u.replace(base, ""), l, v.replace(base, ""),
        {k: x.replace(base, "") for k, x in hreflang_pairs.get(v, {}).items()} or "（目标页不在 sitemap 中）"))
print("hreflang：有标注页面 %d，非双向指向 %d"
      % (sum(1 for a in hreflang_pairs.values() if a), nonrecip))
if nonrecip: fails.append("hreflang 非双向 %d 处" % nonrecip)

print("站内失效引用：%d 种，共 %d 次" % (len(broken_href), sum(broken_href.values())))
for p, n in broken_href.most_common(8): print("   %5d  %s" % (n, p))

# 4. 根目录产物
for f in ("robots.txt", "favicon.ico", "apple-touch-icon.png", "index.html",
          "404.html", "CNAME", ".nojekyll", "assets/og-cover.png"):
    if not os.path.exists(os.path.join(root, f)): fails.append("根目录缺 %s" % f)
print("根目录产物：%s" % ("齐全" if not any("根目录缺" in x for x in fails) else "有缺失"))

print("\n结论：%s" % ("全部通过" if not fails else "失败 %d 项" % len(fails)))
for x in fails: print("  ✗", x)
for x in warns: print("  ! ", x)
sys.exit(1 if fails else 0)
