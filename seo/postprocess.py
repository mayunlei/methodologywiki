#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""多语言站点构建后的 SEO 后处理。

在所有语言各自 `mkdocs build` 完成之后、发布之前运行，对产物目录做：

  1. 根 sitemap.xml 改成 sitemap index，指向各语言 sitemap（原来是空 urlset）
  2. robots.txt（带 Sitemap 指令）
  3. 根 favicon.ico / apple-touch-icon.png（原来 404）
  4. 根 index.html 换成有内容的真首页（原来是 meta-refresh 跳转壳）
  5. 每页注入 hreflang alternate + x-default（按方法论 slug 跨语言对齐）
  6. 每页独立 meta description（原来 800+ 页共用同一条站点描述）
  7. 每页 og: / twitter: 社交卡片标签
  8. 每页 Article 结构化数据
  9. 移除指向 /overrides/stylesheets/extra.css 的失效引用

用法：python3 seo/postprocess.py <构建产物根目录> [--base-url https://methodologywiki.com]
"""
import argparse
import html
import json
import os
import re
import sys
from datetime import datetime, timezone
from urllib.parse import quote, unquote, urljoin, urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from related import ALIASES, HEADING, RELATED  # noqa: E402

LANG_META = {
    "en": ("English", "en_US", "English"),
    "zh": ("中文", "zh_CN", "Chinese"),
    "ja": ("日本語", "ja_JP", "Japanese"),
    "ko": ("한국어", "ko_KR", "Korean"),
    "es": ("Español", "es_ES", "Spanish"),
    "fr": ("Français", "fr_FR", "French"),
    "de": ("Deutsch", "de_DE", "German"),
    "pt": ("Português", "pt_BR", "Portuguese"),
    "ru": ("Русский", "ru_RU", "Russian"),
    "nl": ("Nederlands", "nl_NL", "Dutch"),
    "sv": ("Svenska", "sv_SE", "Swedish"),
    "vi": ("Tiếng Việt", "vi_VN", "Vietnamese"),
}
DEFAULT_LANG = "en"
BROKEN_CSS = re.compile(
    r'\s*<link[^>]+href="[^"]*overrides/stylesheets/extra\.css"[^>]*>', re.I)
RE_TITLE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
# minify 插件会去掉属性引号、调换属性顺序，所以按标签解析属性，不依赖写法
RE_LINK_TAG = re.compile(r"<link\b[^>]*>", re.I)
RE_META_TAG = re.compile(r"<meta\b[^>]*>", re.I)
RE_ATTR = re.compile(r"""([\w:-]+)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'>]+))""")


def tag_attrs(tag):
    out = {}
    for m in RE_ATTR.finditer(tag):
        val = next(g for g in (m.group(2), m.group(3), m.group(4)) if g is not None)
        out[m.group(1).lower()] = val
    return out


def find_canonical(body):
    for m in RE_LINK_TAG.finditer(body):
        a = tag_attrs(m.group(0))
        if a.get("rel", "").lower() == "canonical" and a.get("href"):
            return a["href"]
    return None


def find_description(body):
    """返回 (match, 解码后的内容)；没有则 (None, "")。"""
    for m in RE_META_TAG.finditer(body):
        a = tag_attrs(m.group(0))
        if a.get("name", "").lower() == "description":
            return m, html.unescape(a.get("content", "")).strip()
    return None, ""
RE_ARTICLE = re.compile(r"<article\b.*?</article>", re.S | re.I)
RE_TAG = re.compile(r"<[^>]+>")
RE_SCRIPTY = re.compile(r"<(script|style|nav|svg)\b.*?</\1>", re.S | re.I)
# 已注入标记，避免重复运行时叠加
MARK_OPEN, MARK_CLOSE = "<!-- seo:begin -->", "<!-- seo:end -->"
RE_MARK = re.compile(re.escape(MARK_OPEN) + ".*?" + re.escape(MARK_CLOSE), re.S)


def log(msg):
    print("[seo] %s" % msg, flush=True)


# ------------------------------------------------------------ slug 对齐

def slug_of(url, lang):
    """从 URL 末段取方法论 slug，去掉语言后缀，使各语言版本可互相对应。"""
    segs = [s for s in url.rstrip("/").split("/") if s]
    if not segs:
        return ""
    last = segs[-1]
    key = re.sub(r"-(%s|cn)$" % re.escape(lang), "", last, flags=re.I).lower()
    return ALIASES.get(key, key)


def read_sitemap(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", fh.read())


def url_to_file(root, url, base_url):
    path = unquote(urlparse(url).path)
    f = os.path.join(root, path.lstrip("/"))
    return os.path.join(f, "index.html") if path.endswith("/") else f


def parent_of(url):
    segs = [x for x in unquote(urlparse(url).path).split("/") if x]
    return segs[-2] if len(segs) >= 2 else ""


def resolve_duplicates(root, langs, base_url):
    """同一语言内同 slug 的多篇文章（同一方法论被放进两个分类）会互相抢排名。
    以英文版正文最长者所在分类为主版本，各语言统一；返回 {次版本URL: 主版本URL}。"""
    by = {}
    for lang in langs:
        for u in read_sitemap(os.path.join(root, lang, "sitemap.xml")):
            by.setdefault((lang, slug_of(u, lang)), []).append(u)
    size = lambda u: os.path.getsize(url_to_file(root, u, base_url)) \
        if os.path.exists(url_to_file(root, u, base_url)) else 0      # noqa: E731
    primary_parent = {}
    for (lang, slug), urls in by.items():
        if lang == DEFAULT_LANG and len(urls) > 1:
            primary_parent[slug] = parent_of(max(urls, key=size))
    redirect = {}
    for (lang, slug), urls in by.items():
        if len(urls) < 2:
            continue
        want = primary_parent.get(slug)
        prim = next((u for u in urls if parent_of(u) == want), None) or max(urls, key=size)
        for u in urls:
            if u != prim:
                redirect[u] = prim
    return redirect


def build_slug_map(root, langs, base_url, secondary=()):
    """slug -> {lang: url}；同时返回每种语言的 URL 列表。次版本不参与对齐。"""
    smap, per_lang = {}, {}
    for lang in langs:
        urls = read_sitemap(os.path.join(root, lang, "sitemap.xml"))
        per_lang[lang] = urls
        for u in urls:
            if not u.startswith(base_url) or u in secondary:
                continue
            key = slug_of(u, lang)
            # 语言首页（slug 就是语言代码本身）单独对齐
            if key == lang or key == base_url.rstrip("/").split("/")[-1]:
                key = "__home__"
            if key:
                smap.setdefault(key, {})[lang] = u
    return smap, per_lang


def drop_from_sitemaps(root, langs, secondary):
    """次版本页面 canonical 指向别处，不应再出现在 sitemap 里。"""
    removed = 0
    for lang in langs:
        f = os.path.join(root, lang, "sitemap.xml")
        if not os.path.exists(f):
            continue
        xml = open(f, encoding="utf-8").read()
        def keep(m):
            nonlocal removed
            loc = re.search(r"<loc>\s*([^<\s]+)", m.group(0))
            if loc and loc.group(1) in secondary:
                removed += 1
                return ""
            return m.group(0)
        new = re.sub(r"\s*<url>.*?</url>", keep, xml, flags=re.S)
        if new != xml:
            open(f, "w", encoding="utf-8").write(new)
            gz = f + ".gz"
            if os.path.exists(gz):
                import gzip
                with gzip.open(gz, "wb") as fh:
                    fh.write(new.encode("utf-8"))
    return removed


# ------------------------------------------------------------ 文本提取

# 只含中文、日文（不以空格分词）；韩文以空格分词，不能去空格
CJK = "\u3000-\u303f\u3040-\u30ff\u3400-\u9fff\uff00-\uffef"
RE_CJK_SPACE = re.compile(r"(?<=[%s])\s+|\s+(?=[%s])" % (CJK, CJK))
# 搜索结果摘要按像素截断：中日韩字符宽，约 80 字；拉丁文字约 155 字符
DESC_LIMIT = {"zh": 80, "ja": 80, "ko": 90}


def first_paragraph(body, limit=155):
    """从正文里取一段干净文字做 meta description。"""
    m = RE_ARTICLE.search(body)
    chunk = m.group(0) if m else body
    chunk = RE_SCRIPTY.sub(" ", chunk)
    # 跳过 h1 标题本身，从正文开始
    h1 = re.search(r"</h1>", chunk, re.I)
    if h1:
        chunk = chunk[h1.end():]
    text = html.unescape(RE_TAG.sub(" ", chunk))
    text = re.sub(r"[¶↩]|\s+", lambda m: "" if m.group(0) in "¶↩" else " ", text).strip()
    # 去标签时行内元素两侧会留空格，中日韩文本里这些空格是多余的
    text = RE_CJK_SPACE.sub("", text)
    if len(text) <= limit:
        return text
    cut = text[:limit]
    # 尽量在标点处断开，中英文都照顾
    for sep in ("。", "！", "？", ". ", "；", "; ", "，", ", ", " "):
        idx = cut.rfind(sep)
        if idx > limit * 0.5:
            return cut[:idx + len(sep)].strip().rstrip(",，;；")
    return cut.strip()


def page_title(body, site_name):
    m = RE_TITLE.search(body)
    if not m:
        return site_name
    t = html.unescape(m.group(1)).strip()
    # "波特五力模型 - 方法论智慧百科 : 成功之路" -> "波特五力模型"
    return t.split(" - ")[0].strip() or t


# ------------------------------------------------------------ 注入

def seo_block(lang, canonical, title, desc, alts, og_image, base_url, site_name,
              published=None):
    _, locale, lang_en = LANG_META.get(lang, ("", "en_US", "English"))
    e = lambda s: html.escape(s or "", quote=True)          # noqa: E731
    out = [MARK_OPEN]
    # 1. hreflang：只有确实存在对应页面的语言才列出，避免给搜索引擎错误信号
    for l2, url2 in sorted(alts.items()):
        out.append('<link rel="alternate" hreflang="%s" href="%s">' % (l2, e(url2)))
    if DEFAULT_LANG in alts:
        out.append('<link rel="alternate" hreflang="x-default" href="%s">'
                   % e(alts[DEFAULT_LANG]))
    # 2. 社交卡片
    out += [
        '<meta property="og:type" content="article">',
        '<meta property="og:site_name" content="%s">' % e(site_name),
        '<meta property="og:title" content="%s">' % e(title),
        '<meta property="og:description" content="%s">' % e(desc),
        '<meta property="og:url" content="%s">' % e(canonical),
        '<meta property="og:locale" content="%s">' % e(locale),
        '<meta property="og:image" content="%s">' % e(og_image),
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % e(title),
        '<meta name="twitter:description" content="%s">' % e(desc),
        '<meta name="twitter:image" content="%s">' % e(og_image),
    ]
    # 3. 结构化数据：教程页按 Article 标注
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "inLanguage": lang,
        "url": canonical,
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "image": og_image,
        "author": {"@type": "Organization", "name": "MethodologyWiki",
                   "url": base_url + "/"},
        "publisher": {"@type": "Organization", "name": "MethodologyWiki",
                      "url": base_url + "/",
                      "logo": {"@type": "ImageObject",
                               "url": base_url + "/apple-touch-icon.png"}},
        "isPartOf": {"@type": "WebSite", "name": site_name, "url": base_url + "/"},
    }
    if published:
        data["datePublished"] = published
    out.append('<script type="application/ld+json">%s</script>'
               % json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    out.append(MARK_CLOSE)
    return "\n".join(out)


RE_IMG_TAG = re.compile(r"<img\b[^>]*>", re.I)
IMG_EXT = re.compile(r"\.(png|jpe?g|gif|svg|webp)$", re.I)


def build_image_index(root):
    """文件名 -> 站内绝对路径，英文版优先（翻译页的流程图沿用英文版生成的图）。"""
    idx = {}
    for dp, _, fs in os.walk(root):
        for f in fs:
            if IMG_EXT.search(f):
                rel = "/" + os.path.relpath(os.path.join(dp, f), root).replace(os.sep, "/")
                if f not in idx or rel.startswith("/%s/" % DEFAULT_LANG):
                    idx[f] = rel
    return idx


def fix_images(body, page_url, root, base_url, img_index, stats):
    def repl(m):
        tag = m.group(0)
        a = tag_attrs(tag)
        src = a.get("src", "")
        if not src or src.startswith(("http:", "https:", "//", "data:")):
            return tag
        target = urljoin(page_url, html.unescape(src))
        if os.path.exists(url_to_file(root, target, base_url)):
            return tag
        name = os.path.basename(unquote(urlparse(target).path))
        # 翻译页常引用「本语言后缀」的图，实际只生成了英文版
        alt = re.sub(r"-[a-z]{2}-diagram\.png$", "-en-diagram.png", name)
        hit = img_index.get(name) or img_index.get(alt)
        if not hit:
            stats["img_missing"] += 1
            return tag
        stats["img_fixed"] += 1
        new_src = quote(hit, safe="/")
        return re.sub(r"""src\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+)""",
                      'src="%s"' % new_src, tag, count=1)
    return RE_IMG_TAG.sub(repl, body)


CARD_DESC_LIMIT = {"zh": 34, "ja": 34, "ko": 40}


def build_card_index(root, smap, base_url):
    """(lang, slug) -> (url, 标题, 短描述)，供「相关方法论」卡片使用。"""
    idx = {}
    for slug, by_lang in smap.items():
        if slug == "__home__":
            continue
        for lang, url in by_lang.items():
            f = url_to_file(root, url, base_url)
            if not os.path.exists(f):
                continue
            with open(f, encoding="utf-8", errors="ignore") as fh:
                body = fh.read()
            desc = first_paragraph(body, CARD_DESC_LIMIT.get(lang, 95))
            if desc and not re.search(r"[。！？.!?…]$", desc):
                desc = desc.rstrip("，、,;；：: ") + "…"
            # 卡片标题用 H1：front-matter 里的搜索标题较长，不适合做卡片标题
            h1 = re.search(r"<h1\b[^>]*>(.*?)</h1>", body, re.S | re.I)
            name = html.unescape(RE_TAG.sub("", h1.group(1))).replace("¶", "").strip() if h1 else ""
            idx[(lang, slug)] = (url, name or page_title(body, ""), desc)
    return idx


RE_RELATED = re.compile(r'<section class="mw-related".*?</section>', re.S)


def related_block(lang, slug, card_index):
    items = []
    for target in RELATED.get(slug, []):
        hit = card_index.get((lang, target))
        if hit:
            items.append(hit)
    if not items:
        return ""
    e = lambda x: html.escape(x or "", quote=True)        # noqa: E731
    lis = "".join(
        '<li><a href="%s"><strong>%s</strong><span>%s</span></a></li>'
        % (e(urlparse(u).path), e(t), e(d)) for u, t, d in items[:5])
    return ('<section class="mw-related" aria-labelledby="mw-related-h">'
            '<h2 id="mw-related-h">%s</h2><ul>%s</ul></section>'
            % (e(HEADING.get(lang, HEADING["en"])), lis))


def process_page(path, lang, smap, base_url, og_image, site_desc_by_lang, stats,
                 root=None, img_index=None, secondary=None, card_index=None):
    with open(path, encoding="utf-8", errors="ignore") as fh:
        body = fh.read()
    if "</head>" not in body:
        return
    original = body
    body = RE_MARK.sub("", body)                       # 幂等：先清掉上轮注入
    # 主题按 extra.alternate 给每页输出「本页 -> 各语言首页」的 hreflang，这是错误
    # 对应关系（页面应对应其他语言的同一篇文章）。统一移除，由下方按页对齐重新生成。
    body = re.sub(r"<link\b(?=[^>]*\bhreflang=)(?=[^>]*\balternate\b)[^>]*>\s*", "",
                  body, flags=re.I)
    body, n_css = BROKEN_CSS.subn("", body)            # 失效样式表引用
    stats["css_fixed"] += 1 if n_css else 0

    canonical = find_canonical(body)
    if not canonical:
        stats["no_canonical"] += 1
        return
    if img_index is not None:
        body = fix_images(body, canonical, root, base_url, img_index, stats)
    # 文末「相关方法论」：放在正文 article 内，跟随主题样式
    body = RE_RELATED.sub("", body)
    if card_index is not None and "</article>" in body:
        block = related_block(lang, slug_of(canonical, lang), card_index)
        if block:
            body = body.replace("</article>", block + "</article>", 1)
            stats["related"] += 1
    secondary = secondary or {}
    if canonical in secondary:
        # 次版本：canonical 改指主版本，不注入 hreflang（Google 会忽略非规范页的 hreflang）
        primary = secondary[canonical]
        body = re.sub(r"<link\b[^>]*\brel=[\"']?canonical[\"']?[^>]*>",
                      '<link rel="canonical" href="%s">' % html.escape(primary, quote=True),
                      body, count=1)
        stats["dup_canonicalized"] += 1
        if body != original:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(body)
        return
    key = slug_of(canonical, lang)
    if canonical.rstrip("/") == ("%s/%s" % (base_url, lang)):
        key = "__home__"
    alts = dict(smap.get(key, {}))
    if lang not in alts:
        alts[lang] = canonical

    site_name = ""
    mt = RE_TITLE.search(body)
    if mt:
        parts = html.unescape(mt.group(1)).split(" - ")
        site_name = parts[-1].strip() if len(parts) > 1 else parts[0].strip()
    title = page_title(body, site_name)

    site_desc = site_desc_by_lang.get(lang, "")
    md, cur_desc = find_description(body)
    # 全站共用同一条描述时，改成按正文生成的本页描述
    if not cur_desc or cur_desc == site_desc:
        new_desc = first_paragraph(body, DESC_LIMIT.get(lang, 155)) or site_desc
        if new_desc and new_desc != cur_desc:
            stats["desc_rewritten"] += 1
        if md:
            body = (body[:md.start()]
                    + '<meta name="description" content="%s">'
                      % html.escape(new_desc, quote=True)
                    + body[md.end():])
        else:
            body = body.replace("</head>",
                                '<meta name="description" content="%s">\n</head>'
                                % html.escape(new_desc, quote=True), 1)
        desc = new_desc
    else:
        desc = cur_desc

    block = seo_block(lang, canonical, title, desc, alts, og_image,
                      base_url, site_name)
    body = body.replace("</head>", block + "\n</head>", 1)
    if body != original:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)
        stats["pages"] += 1
        stats["hreflang"] += 1 if len(alts) > 1 else 0


# ------------------------------------------------------------ 根目录产物

def write_sitemap_index(root, langs, base_url, per_lang):
    """根 sitemap 原本是空 urlset，改成指向各语言 sitemap 的 index。"""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    items = []
    for lang in langs:
        if not per_lang.get(lang):
            continue
        items.append("  <sitemap>\n    <loc>%s/%s/sitemap.xml</loc>\n"
                     "    <lastmod>%s</lastmod>\n  </sitemap>"
                     % (base_url, lang, now))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(items) + "\n</sitemapindex>\n")
    with open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(xml)
    # 旧的空 sitemap.xml.gz 会盖掉新文件的可信度，直接删掉
    gz = os.path.join(root, "sitemap.xml.gz")
    if os.path.exists(gz):
        os.remove(gz)
    total = sum(len(v) for v in per_lang.values())
    log("sitemap index：%d 个语言 sitemap，合计 %d 个 URL" % (len(items), total))
    return total


SEO_DIR = os.path.dirname(os.path.abspath(__file__))


def read_secret(name):
    p = os.path.join(SEO_DIR, name)
    if os.path.exists(p):
        v = open(p, encoding="utf-8").read().strip()
        return v or None
    return None


def write_verification(root):
    """搜索引擎站点验证：
    - IndexNow（Bing/Yandex/Naver/Seznam）：根目录放 <key>.txt
    - Google Search Console（网址前缀方式）：首页 <meta name=google-site-verification>
      令牌放在 seo/google_site_verification.txt；用 DNS 方式验证则无需此文件"""
    # seo/root_files/ 下的文件原样放到站点根目录（Bing 的 BingSiteAuth.xml、
    # Google 的 googleXXXX.html 等文件验证方式）
    extra = os.path.join(SEO_DIR, "root_files")
    if os.path.isdir(extra):
        import shutil
        for name in sorted(os.listdir(extra)):
            if not name.startswith("."):
                shutil.copyfile(os.path.join(extra, name), os.path.join(root, name))
                log("根目录验证文件：%s" % name)
    key = read_secret("indexnow_key.txt")
    if key:
        with open(os.path.join(root, key + ".txt"), "w", encoding="utf-8") as fh:
            fh.write(key)
        log("IndexNow 密钥文件已写入根目录")
    return read_secret("google_site_verification.txt"), read_secret("bing_site_verification.txt")


def write_robots(root, base_url, verification=None):
    lines = ["User-agent: *", "Allow: /", ""]
    # 构建产物里的搜索页没有收录价值，避免浪费抓取预算
    lines += ["Disallow: /*/search/", "Disallow: /search/", ""]
    lines += ["Sitemap: %s/sitemap.xml" % base_url, ""]
    with open(os.path.join(root, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    log("robots.txt 已写入（含 Sitemap 指令）")


def write_icons(root):
    """根目录缺 favicon.ico / apple-touch-icon.png，各语言页面都在引用它们。"""
    made = []
    src = None
    for cand in ("assets/favicon.ico", "docs/favicon-32x32.png"):
        p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), cand)
        if os.path.exists(p):
            src = p
            break
    ico = os.path.join(root, "favicon.ico")
    if src and src.endswith(".ico") and not os.path.exists(ico):
        import shutil
        shutil.copyfile(src, ico)
        made.append("favicon.ico")
    try:
        from PIL import Image, ImageDraw
        apple = os.path.join(root, "apple-touch-icon.png")
        img = Image.new("RGB", (180, 180), (37, 106, 191))
        dr = ImageDraw.Draw(img)
        dr.rounded_rectangle([18, 18, 162, 162], radius=28, outline=(255, 255, 255), width=8)
        dr.line([(56, 124), (56, 60), (90, 104), (124, 60), (124, 124)],
                fill=(255, 255, 255), width=11, joint="curve")
        img.save(apple)
        made.append("apple-touch-icon.png")
        if not os.path.exists(ico):
            img.resize((64, 64)).save(ico, sizes=[(16, 16), (32, 32), (48, 48)])
            made.append("favicon.ico")
    except ImportError:
        log("未安装 Pillow，跳过 apple-touch-icon 生成")
    if made:
        log("根图标已补齐：%s" % ", ".join(made))


def write_og_image(root):
    """社交卡片默认图。没有 Pillow 时跳过，og:image 仍指向该路径由后续补。"""
    path = os.path.join(root, "assets", "og-cover.png")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "og-cover.png")
    if os.path.exists(src):
        import shutil
        os.makedirs(os.path.dirname(path), exist_ok=True)
        shutil.copyfile(src, path)
        log("社交卡片图：使用 seo/assets/og-cover.png")
        return
    if os.path.exists(path):
        return
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img = Image.new("RGB", (1200, 630), (12, 26, 46))
    dr = ImageDraw.Draw(img)
    dr.rectangle([0, 0, 1200, 8], fill=(37, 106, 191))
    for i, (x, y, r) in enumerate([(980, 120, 160), (1080, 420, 110)]):
        dr.ellipse([x - r, y - r, x + r, y + r], outline=(37, 106, 191), width=3)
    dr.text((80, 250), "Methodology Wiki", fill=(255, 255, 255))
    dr.text((80, 300), "methodologywiki.com", fill=(150, 170, 200))
    img.save(path)
    log("已生成默认社交卡片图 assets/og-cover.png")


HOME_TPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(site_name)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(base)s/">
<link rel="icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
%(alts)s
<meta property="og:type" content="website">
<meta property="og:title" content="%(site_name)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(base)s/">
<meta property="og:image" content="%(base)s/assets/og-cover.png">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">%(ld)s</script>
<style>
:root{color-scheme:light dark;--bg:#fcfcfb;--fg:#11161d;--mut:#5b6471;--line:#e4e6ea;--acc:#256abf}
@media (prefers-color-scheme:dark){:root{--bg:#0f1319;--fg:#eef1f5;--mut:#9aa4b2;--line:#232a34;--acc:#5e9bf0}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 "PingFang SC","Hiragino Sans GB",
 system-ui,-apple-system,"Segoe UI",sans-serif}
.wrap{max-width:960px;margin:0 auto;padding:64px 16px 80px}
h1{font-size:clamp(28px,5vw,40px);line-height:1.25;margin:0 0 14px;letter-spacing:-.02em}
.lede{color:var(--mut);font-size:17px;margin:0 0 36px;max-width:62ch}
h2{font-size:15px;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);
 margin:44px 0 16px;font-weight:600}
.langs{display:flex;flex-wrap:wrap;gap:10px}
.langs a{display:inline-block;padding:9px 16px;border:1px solid var(--line);border-radius:999px;
 color:var(--fg);text-decoration:none;font-size:15px}
.langs a:hover{border-color:var(--acc);color:var(--acc)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px 24px}
.grid a{color:var(--fg);text-decoration:none;padding:7px 0;border-bottom:1px solid var(--line);
 font-size:15px}
.grid a:hover{color:var(--acc)}
footer{margin-top:56px;padding-top:24px;border-top:1px solid var(--line);color:var(--mut);font-size:14px}
footer a{color:var(--mut)}
</style>
</head>
<body>
<div class="wrap">
<h1>%(site_name)s</h1>
<p class="lede">%(desc)s</p>
<h2>Languages</h2>
<div class="langs">%(lang_links)s</div>
<h2>Browse methodologies</h2>
<div class="grid">%(topic_links)s</div>
<footer>
<a href="/sitemap.xml">Sitemap</a> · <a href="%(repo)s">GitHub</a>
</footer>
</div>
</body>
</html>
"""


def write_home(root, langs, base_url, smap, per_lang, site_name, desc, repo,
               google_token=None, bing_token=None):
    """根页面原本是 meta-refresh 跳转壳，换成有内容、可被收录的真首页。"""
    alts = "\n".join('<link rel="alternate" hreflang="%s" href="%s/%s/">'
                     % (l, base_url, l) for l in langs if per_lang.get(l))
    alts += '\n<link rel="alternate" hreflang="x-default" href="%s/">' % base_url
    lang_links = "".join('<a href="/%s/" hreflang="%s">%s</a>'
                         % (l, l, html.escape(LANG_META.get(l, (l,))[0]))
                         for l in langs if per_lang.get(l))
    # 首页直接列出默认语言的全部条目，给爬虫一条完整的发现路径
    topics = []
    for key, by_lang in sorted(smap.items()):
        if key == "__home__":
            continue
        url = by_lang.get(DEFAULT_LANG) or next(iter(by_lang.values()))
        name = ""
        f = url_to_file(root, url, base_url)
        if os.path.exists(f):
            with open(f, encoding="utf-8", errors="ignore") as fh:
                name = page_title(fh.read(), "")
        if not name:
            name = url.rstrip("/").split("/")[-1].replace("-", " ")
        topics.append((name, url))
    topics.sort(key=lambda t: t[0].lower())
    topic_links = "".join('<a href="%s">%s</a>' % (html.escape(u, quote=True),
                                                   html.escape(n))
                          for n, u in topics)
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "WebSite",
        "name": site_name, "url": base_url + "/", "description": desc,
        "inLanguage": [l for l in langs if per_lang.get(l)],
        "potentialAction": {
            "@type": "SearchAction",
            "target": base_url + "/en/search/?q={search_term_string}",
            "query-input": "required name=search_term_string"},
    }, ensure_ascii=False, separators=(",", ":"))
    page = HOME_TPL % dict(site_name=html.escape(site_name), desc=html.escape(desc),
                           base=base_url, alts=alts, ld=ld, lang_links=lang_links,
                           topic_links=topic_links, repo=html.escape(repo))
    verify = ""
    if google_token:
        verify += '<meta name="google-site-verification" content="%s">\n' % html.escape(google_token, quote=True)
    if bing_token:
        verify += '<meta name="msvalidate.01" content="%s">\n' % html.escape(bing_token, quote=True)
    if verify:
        page = page.replace("</head>", verify + "</head>", 1)
        log("首页已注入站点验证 meta")
    with open(os.path.join(root, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    log("根首页已替换为真实内容页（%d 个条目入口，替代原 meta-refresh 跳转）" % len(topics))


# ------------------------------------------------------------ 入口

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", help="多语言构建产物根目录")
    ap.add_argument("--base-url", default="https://methodologywiki.com")
    ap.add_argument("--site-name", default="Wisdom Wiki of Methodologies : Way To Success")
    ap.add_argument("--repo", default="https://github.com/mayunlei/methodologywiki")
    ap.add_argument("--skip-pages", action="store_true", help="只生成根目录产物")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    base_url = args.base_url.rstrip("/")
    if not os.path.isdir(root):
        sys.exit("目录不存在: %s" % root)

    langs = [l for l in LANG_META if os.path.isdir(os.path.join(root, l))]
    langs.sort(key=lambda l: (l != DEFAULT_LANG, l))
    log("检测到语言版本：%s" % ", ".join(langs))

    secondary = resolve_duplicates(root, langs, base_url)
    smap, per_lang = build_slug_map(root, langs, base_url, secondary)
    log("跨语言对齐 slug：%d 个；同语言重复文章次版本 %d 个（canonical 归并到主版本）"
        % (len(smap), len(secondary)))
    img_index = build_image_index(root)
    card_index = build_card_index(root, smap, base_url)

    # 各语言的站点级描述，用来识别「全站共用描述」的页面
    site_desc_by_lang = {}
    for lang in langs:
        idx = os.path.join(root, lang, "index.html")
        if os.path.exists(idx):
            with open(idx, encoding="utf-8", errors="ignore") as fh:
                _, d = find_description(fh.read())
            if d:
                site_desc_by_lang[lang] = d

    og_image = base_url + "/assets/og-cover.png"
    stats = {"pages": 0, "desc_rewritten": 0, "hreflang": 0, "css_fixed": 0,
             "no_canonical": 0, "img_fixed": 0, "img_missing": 0, "dup_canonicalized": 0,
             "related": 0}
    if not args.skip_pages:
        for lang in langs:
            for dirpath, _, files in os.walk(os.path.join(root, lang)):
                for name in files:
                    if name.endswith(".html"):
                        process_page(os.path.join(dirpath, name), lang, smap,
                                     base_url, og_image, site_desc_by_lang, stats,
                                     root=root, img_index=img_index, secondary=secondary,
                                     card_index=card_index)
        log("处理页面 %d 个：重写描述 %d、注入 hreflang %d、修复失效样式引用 %d、"
            "无 canonical 跳过 %d"
            % (stats["pages"], stats["desc_rewritten"], stats["hreflang"],
               stats["css_fixed"], stats["no_canonical"]))
        log("图片：修复失效引用 %d 处，全站无源文件 %d 处；重复文章 canonical 归并 %d 页"
            % (stats["img_fixed"], stats["img_missing"], stats["dup_canonicalized"]))
        log("相关方法论互链：%d 页" % stats["related"])
        removed = drop_from_sitemaps(root, langs, secondary)
        per_lang = {l: [u for u in v if u not in secondary] for l, v in per_lang.items()}
        log("sitemap 移除次版本 %d 条" % removed)

    total = write_sitemap_index(root, langs, base_url, per_lang)
    write_robots(root, base_url)
    write_icons(root)
    write_og_image(root)
    desc = site_desc_by_lang.get(DEFAULT_LANG) or (
        "A knowledge base dedicated to systematically introducing, explaining, "
        "and applying various powerful methodologies.")
    google_token, bing_token = write_verification(root)
    write_home(root, langs, base_url, smap, per_lang, args.site_name, desc, args.repo,
               google_token, bing_token)
    log("完成。可提交 URL 总数 %d" % total)


if __name__ == "__main__":
    main()
