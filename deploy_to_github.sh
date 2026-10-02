#!/bin/bash
# 多语言站点发布到 GitHub Pages（gh-pages 分支）。
#   构建 → SEO 后处理 → 自检 → 发布；自检不通过不发布。
# 用法：./deploy_to_github.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
OUT="$ROOT/_site"

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "❌ 不在 git 仓库内"; exit 1
fi

if [ -f /opt/miniconda3/etc/profile.d/conda.sh ]; then
  # shellcheck disable=SC1091
  source /opt/miniconda3/etc/profile.d/conda.sh && conda activate py39pd
fi

echo "🔨 构建 12 种语言 + SEO 后处理"
bash seo/build_site.sh "$OUT"

echo "🔎 发布前自检"
python3 seo/verify_site.py "$OUT"

echo "🚀 发布到 gh-pages"
SRC_SHA=$(git rev-parse --short HEAD)
DIRTY=$([ -n "$(git status --porcelain -- docs en zh es fr de pt nl ru vi sv ja ko overrides seo 2>/dev/null)" ] && echo "+dirty" || echo "")
# ghp-import 随 mkdocs 一起安装：用产物目录生成一个提交并强制推送到 gh-pages
python3 -m ghp_import -n -p -f -b gh-pages -r origin \
  -m "Deploy ${SRC_SHA}${DIRTY}: multi-language site with SEO postprocess" "$OUT"

echo "✅ 已发布。GitHub Pages 通常 1~3 分钟内生效：https://methodologywiki.com/"

# 通知 Bing / Yandex / Naver / Seznam 重新抓取（等密钥文件上线后推送；失败不影响发布）
echo "📣 IndexNow 推送"
python3 seo/indexnow_submit.py "$OUT" --wait 240 || echo "⚠️  IndexNow 推送失败，可稍后手动执行：python3 seo/indexnow_submit.py _site"
