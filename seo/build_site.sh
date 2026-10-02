#!/usr/bin/env bash
# 全语言构建 + SEO 后处理。CI（.github/workflows/deploy.yml）与本地共用这一个入口。
#   用法：bash seo/build_site.sh [输出目录，默认 _site]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-_site}"
case "$OUT" in /*) ;; *) OUT="$ROOT/$OUT" ;; esac

cd "$ROOT"

# 构建前检查会导致渲染错误的 Markdown 写法（列表前缺空行、--- 紧贴文字）
python3 seo/lint_markdown.py docs/en */docs || {
  echo "✗ Markdown 有渲染问题，运行 python3 seo/lint_markdown.py --fix docs/en */docs 修复后重试"; exit 1; }

rm -rf "$OUT"
mkdir -p "$OUT"

# 英文与其他语言同构：各自 <lang>/mkdocs.yml 构建到 /<lang>/
LANGS=(en zh es fr de pt nl ru vi sv ja ko)
for lang in "${LANGS[@]}"; do
  if [ -f "$lang/mkdocs.yml" ]; then
    echo "▶ building $lang"
    mkdocs build -q -f "$lang/mkdocs.yml" -d "$OUT/$lang"
  else
    echo "⚠ skip $lang (no $lang/mkdocs.yml)"
  fi
done

# GitHub Pages 需要：自定义域名 + 关闭 Jekyll
cp CNAME "$OUT/CNAME"
touch "$OUT/.nojekyll"
# 站点级 404：MkDocs 的 404 页使用绝对资源路径，可直接放到根目录
[ -f "$OUT/en/404.html" ] && cp "$OUT/en/404.html" "$OUT/404.html"

python3 seo/postprocess.py "$OUT"
echo "✔ site ready: $OUT"
