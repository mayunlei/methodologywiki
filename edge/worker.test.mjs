import assert from "node:assert/strict";
import worker, { originRequest, route } from "./worker.js";
const B = "https://methodologywiki.com";
const cases = [
  ["http://methodologywiki.com/zh/", { redirect: B + "/zh/" }],
  ["http://methodologywiki.com/en/en/Foundations/x/?a=1", { redirect: "https://methodologywiki.com/en/Foundations/x/?a=1" }],
  [B + "/en/en/Foundations/learning_methods/Feynman-Technique-Tutorial-en/", { redirect: B + "/en/Foundations/learning_methods/Feynman-Technique-Tutorial-en/" }],
  [B + "/en/en", { redirect: B + "/en" }],
  [B + "/en/en/Problem%20Solving%20%26%20Decision%20Making/x/", { redirect: B + "/en/Problem%20Solving%20%26%20Decision%20Making/x/" }],
  [B + "/en/english-page/", null],     // 不能误伤以 /en/en 开头的其他路径
  [B + "/zh/", null],
];
const E = "/en/Problem%20Solving%20%26%20Decision%20Making";
cases.push(
  // 合并的重复文章：编码/未编码、带不带结尾斜杠、index.html 都要命中
  [B + E + "/problem_solving/Fishbone-Diagram-Tutorial-en/", { redirect: B + E + "/root_cause_analysis/Fishbone-Diagram-Tutorial-en/" }],
  [B + "/en/Problem%20Solving%20&%20Decision%20Making/problem_solving/Fishbone-Diagram-Tutorial-en", { redirect: B + E + "/root_cause_analysis/Fishbone-Diagram-Tutorial-en/" }],
  [B + "/zh/problem_solving/Five-Whys-Tutorial-zh/index.html", { redirect: B + "/zh/root_cause_analysis/5-Whys-Tutorial-zh/" }],
  [B + "/zh/problem_solving/Six-Thinking-Hats-Tutorial-zh/", { redirect: B + "/zh/ideation/Six-Thinking-Hats-Tutorial-zh/" }],
  // /en/en 旧地址 + 已合并文章：一次跳到最终地址
  ["http://methodologywiki.com/en/en" + E.slice(3) + "/problem_solving/Six-Thinking-Hats-Tutorial-en/", { redirect: B + E + "/ideation/Six-Thinking-Hats-Tutorial-en/" }],
  [B + "/zh/problem_solving/Problem-Solving-zh/", null],   // 同目录其他文章不受影响
);
for (const [u, want] of cases) {
  const got = route(u);
  if (want) assert.equal(got.redirect, want.redirect, u);
  else assert.ok(got.pass, "应直通: " + u);
}
assert.equal(route(B + "/zh/assets/stylesheets/main.342714a4.min.css").hashed, true);
assert.equal(route(B + "/zh/stylesheets/extra.css").hashed, false);
assert.equal(route(B + "/zh/stylesheets/extra.css").isStatic, true);
assert.equal(route(B + "/zh/").isStatic, false);
console.log("worker route 测试全部通过（%d 个用例 + 4 个缓存分类断言）", cases.length);

const article = new Request(B + "/zh/?q=SWOT", {
  method: "HEAD", headers: { "Accept-Language": "zh-CN" },
});
const origin = originRequest(article, false);
assert.equal(origin.method, "HEAD");
assert.equal(origin.headers.get("Accept-Language"), "zh-CN");
assert.equal(new URL(origin.url).pathname, "/zh/");
assert.equal(new URL(origin.url).searchParams.get("q"), "SWOT");
assert.equal(new URL(origin.url).searchParams.get("__mw_release"), "07a09019");
const asset = new Request(B + "/zh/stylesheets/extra.4c649c404ffd.css");
assert.equal(originRequest(asset, true), asset);

const realFetch = globalThis.fetch;
let forwarded;
globalThis.fetch = async (request, options) => {
  forwarded = { request, options };
  return new Response("ok");
};
try {
  const ctx = { passThroughOnException() {} };
  await worker.fetch(article, {}, ctx);
  assert.equal(forwarded.request.url, origin.url);
  assert.equal(forwarded.options.cf.cacheTtlByStatus["200-299"], 3600);
  await worker.fetch(asset, {}, ctx);
  assert.equal(forwarded.request, asset);
  const post = new Request(B + "/submit", { method: "POST", body: "example" });
  await worker.fetch(post, {}, ctx);
  assert.equal(forwarded.request, post);
  assert.equal(forwarded.options, undefined);
} finally {
  globalThis.fetch = realFetch;
}
console.log("worker release cache tests passed: query, headers, HEAD, assets and POST forwarding");
