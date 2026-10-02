#!/usr/bin/env python3
"""检测各语言目录下的文章是否真的是该语言（翻译漏掉、错放语言的页面）。"""
import os, re, sys
STOP = {
    "en": " the and is of to that with for are this ",
    "es": " el los las del una por para con es usted ",
    "pt": " não uma são também para com dos das você em do da que ",
    "fr": " le les des une est pour avec dans que ",
    "de": " der die das und ist nicht mit für ein eine ",
    "nl": " het een van en niet voor met dat zijn wordt ",
    "sv": " och är att det för som med inte en på ",
    "vi": " của và là các những được một cho trong không ",
    "ru": " и в не на что это как с для по ",
}
def score(text, lang):
    t = " " + re.sub(r"\s+", " ", text.lower()) + " "
    return sum(t.count(" %s " % w) for w in STOP[lang].split())
def script_ratio(text):
    han = len(re.findall(r"[一-鿿]", text)); kana = len(re.findall(r"[぀-ヿ]", text))
    hang = len(re.findall(r"[가-힯]", text)); lat = len(re.findall(r"[A-Za-z]", text))
    return han, kana, hang, lat
bad = []
for lang in "en zh ja ko es pt fr de nl sv vi ru".split():
    d = "docs/en" if lang == "en" else "%s/docs" % lang
    for dp, _, fs in os.walk(d):
        for f in fs:
            if not f.endswith(".md"): continue
            p = os.path.join(dp, f)
            t = re.sub(r"```.*?```|<!--.*?-->|\(.*?\)|`[^`]*`", " ", open(p, encoding="utf-8").read(), flags=re.S)
            han, kana, hang, lat = script_ratio(t)
            if lang in ("zh", "ja", "ko"):
                ok = {"zh": han > lat * 0.6 and kana < han * 0.05,
                      "ja": kana > 50, "ko": hang > lat * 0.5}[lang]
                guess = "zh" if han > kana and han > hang else "ja" if kana > hang else "ko"
            else:
                s = {l: score(t, l) for l in STOP}
                guess = max(s, key=s.get)
                ok = guess == lang or s[lang] >= 0.6 * s[guess]
            if not ok:
                bad.append((lang, guess, p))
for lang, guess, p in bad:
    print("  [%s 目录，像是 %s] %s" % (lang, guess, p))
print("疑似语言错误的页面：%d" % len(bad))
sys.exit(1 if bad else 0)
