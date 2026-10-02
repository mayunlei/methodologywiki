// methodologywiki.com 边缘层（Cloudflare Worker）
//
// 1. http -> https 301（线上 http 原本直接返回 200，Google 收录了 http 地址，形成重复内容）
// 2. /en/en/* -> /en/* 301（英文版旧结构多套一层 en，已被收录的旧地址统一迁移）
// 3. 边缘缓存：源站是 GitHub Pages（max-age=600），Cloudflare 默认不缓存 HTML，
//    命中率只有约 2%，真实用户加载 P75 4s+。HTML 在边缘缓存 1 小时，
//    带内容哈希的静态资源缓存 30 天并允许浏览器长期缓存。
// 任何异常都回落到直连源站（passThroughOnException），不会因 Worker 出错导致站点不可用。

const HTML_EDGE_TTL = 3600;          // 1h：发布后最多 1 小时内全球生效
const ASSET_EDGE_TTL = 30 * 86400;   // 30d
const HASHED_ASSET = /\.[0-9a-f]{8,}\.min\.(css|js)$/i;  // mkdocs-material 产物：main.342714a4.min.css
const STATIC_EXT = /\.(css|js|png|jpe?g|gif|svg|webp|ico|woff2?|ttf|json|xml|txt)$/i;

export function route(urlString) {
  const url = new URL(urlString);
  let moved = false;
  if (url.protocol === "http:") {
    url.protocol = "https:";
    moved = true;
  }
  if (url.pathname === "/en/en" || url.pathname.startsWith("/en/en/")) {
    url.pathname = url.pathname.slice(3);   // 去掉多出来的一层 /en
    moved = true;
  }
  // 多项同时命中也只跳一次，直接到最终地址
  if (moved) return { redirect: url.toString() };
  return { pass: true, hashed: HASHED_ASSET.test(url.pathname),
           isStatic: STATIC_EXT.test(url.pathname) };
}

export default {
  async fetch(request, env, ctx) {
    ctx.passThroughOnException();
    const r = route(request.url);
    if (r.redirect) {
      return Response.redirect(r.redirect, 301);
    }
    if (request.method !== "GET" && request.method !== "HEAD") {
      return fetch(request);
    }
    const ttl = r.isStatic ? ASSET_EDGE_TTL : HTML_EDGE_TTL;
    const resp = await fetch(request, {
      cf: {
        cacheEverything: true,
        // 错误页只短暂缓存，避免把源站抖动放大
        cacheTtlByStatus: { "200-299": ttl, "301-308": 3600, "404": 300, "500-599": 0 },
      },
    });
    if (r.hashed && resp.ok) {
      const out = new Response(resp.body, resp);
      out.headers.set("Cache-Control", "public, max-age=31536000, immutable");
      return out;
    }
    return resp;
  },
};
