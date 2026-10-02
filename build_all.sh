#!/bin/bash
# Build and serve script for all language versions
# Usage:
#   bash build_all.sh          # Build only
#   bash build_all.sh serve    # Build and serve
#   bash build_all.sh -s       # Build and serve

set -e  # Exit on error

# Parse arguments
DO_SERVE=false
if [ "$1" = "serve" ] || [ "$1" = "-s" ]; then
    DO_SERVE=true
fi

echo "🚀 Building all language versions..."

# Initialize conda - try common installation locations
CONDA_INIT_SCRIPT=""
if [ -f "$HOME/anaconda3/etc/profile.d/conda.sh" ]; then
    CONDA_INIT_SCRIPT="$HOME/anaconda3/etc/profile.d/conda.sh"
elif [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
    CONDA_INIT_SCRIPT="$HOME/miniconda3/etc/profile.d/conda.sh"
elif [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
    CONDA_INIT_SCRIPT="/opt/anaconda3/etc/profile.d/conda.sh"
elif [ -f "/opt/miniconda3/etc/profile.d/conda.sh" ]; then
    CONDA_INIT_SCRIPT="/opt/miniconda3/etc/profile.d/conda.sh"
fi

if [ -n "$CONDA_INIT_SCRIPT" ]; then
    echo "🔧 Initializing conda from $CONDA_INIT_SCRIPT..."
    source "$CONDA_INIT_SCRIPT"
    conda activate py39pd
    echo "✅ Activated conda environment: py39pd"
else
    echo "⚠️  Conda not found in standard locations. Assuming mkdocs is in PATH..."
fi

# 与 CI 共用同一入口：12 种语言构建 + SEO 后处理（英文版构建配置在 en/mkdocs.yml）
bash seo/build_site.sh site

echo "🎉 All builds complete!"
echo "📂 Output in site/ directory"

# Serve if requested
if [ "$DO_SERVE" = true ]; then
    echo ""
    echo "🌐 Starting local server..."
    echo "📍 Access at: http://127.0.0.1:8000"
    echo "   Press Ctrl+C to stop"
    echo ""
    # Serve from the built site directory
    python -m http.server 8000 --directory site
fi
