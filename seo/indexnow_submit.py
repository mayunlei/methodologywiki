#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把站点全部 URL 通过 IndexNow 推送给 Bing / Yandex / Naver / Seznam。

IndexNow 会回源校验 https://<host>/<key>.txt，所以要在站点发布生效后再运行。
用法：python3 seo/indexnow_submit.py <构建产物目录> [--wait 180]
"""
import argparse, json, os, re, sys, time, urllib.error, urllib.request
from urllib.parse import unquote, urlparse

SEO_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "methodologywiki.com"
ENDPOINT = "https://api.indexnow.org/indexnow"


UA = "methodologywiki-indexnow/1.0 (+https://methodologywiki.com/)"


def opener():
    # 直连：不经过本机代理，避免代理不稳定导致推送失败。
    # Cloudflare 会拦截 Python 默认 User-Agent（403），需显式声明
    o = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    o.addheaders = [("User-Agent", UA)]
    return o


def site_urls(root):
    idx = open(os.path.join(root, "sitemap.xml"), encoding="utf-8").read()
    urls = []
    for sm in re.findall(r"<loc>([^<]+)</loc>", idx):
        f = os.path.join(root, unquote(urlparse(sm).path).lstrip("/"))
        urls += re.findall(r"<loc>([^<]+)</loc>", open(f, encoding="utf-8").read())
    return ["https://%s/" % HOST] + urls


def wait_key_live(key, wait):
    url = "https://%s/%s.txt" % (HOST, key)
    deadline = time.time() + wait
    while True:
        try:
            with opener().open(url + "?t=%d" % time.time(), timeout=15) as r:
                if r.read().decode().strip() == key:
                    return True
        except Exception:                                    # noqa: BLE001
            pass
        if time.time() > deadline:
            return False
        time.sleep(10)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--wait", type=int, default=180, help="等待密钥文件上线的秒数")
    args = ap.parse_args()
    key = open(os.path.join(SEO_DIR, "indexnow_key.txt"), encoding="utf-8").read().strip()
    if not wait_key_live(key, args.wait):
        sys.exit("密钥文件 https://%s/%s.txt 未上线，放弃推送" % (HOST, key))
    urls = site_urls(args.root)
    body = json.dumps({"host": HOST, "key": key,
                       "keyLocation": "https://%s/%s.txt" % (HOST, key),
                       "urlList": urls}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with opener().open(req, timeout=60) as r:
            print("IndexNow：已推送 %d 个 URL，HTTP %s" % (len(urls), r.status))
    except urllib.error.HTTPError as e:
        # 202 = 已接收待校验；422 = URL 与 host 不匹配；403 = 密钥校验失败
        print("IndexNow：HTTP %s %s" % (e.code, e.read()[:200].decode(errors="replace")))
        sys.exit(0 if e.code in (200, 202) else 1)


if __name__ == "__main__":
    main()
