#!/usr/bin/env python3
"""合并上游规则 + 检查配置里所有链接是否可用。

用法:
    python3 scripts/build.py           # 合并规则并生成 STATUS.md
    python3 scripts/build.py --check   # 只检查链接，不改动 rules/

只依赖 Python 标准库。
"""
from __future__ import annotations

import concurrent.futures as cf
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
CONF = ROOT / "QuantumultX.conf"
SOURCES = ROOT / "scripts" / "sources.json"
STATUS = ROOT / "STATUS.md"
UA = "Mozilla/5.0 (quanx-merge-bot)"
SELF_PREFIX = "https://raw.githubusercontent.com/blacksheep81/quanx/"

# Surge / Loon / Clash 写法 -> Quantumult X 写法
TYPE_MAP = {
    "domain": "host",
    "host": "host",
    "domain-suffix": "host-suffix",
    "host-suffix": "host-suffix",
    "domain-keyword": "host-keyword",
    "host-keyword": "host-keyword",
    "domain-wildcard": "host-wildcard",
    "host-wildcard": "host-wildcard",
    "ip-cidr": "ip-cidr",
    "ip-cidr6": "ip6-cidr",
    "ip6-cidr": "ip6-cidr",
    "ip-asn": "ip-asn",
    "user-agent": "user-agent",
    "geoip": "geoip",
}
CASE_INSENSITIVE = {"host", "host-suffix", "host-keyword", "host-wildcard"}


def fetch(url: str, timeout: int = 30) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception:  # 网络错误 / 超时
        return 0, b""


def parse_rules(text: str) -> tuple[list[tuple[str, str]], int]:
    """返回 [(类型, 值)] 和 跳过的行数（AND/OR 等复合规则、无法识别的类型）。"""
    rules, skipped = [], 0
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", ";", "//", "payload:")):
            continue
        line = line.lstrip("- ").strip("'\"")
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 2:
            skipped += 1
            continue
        kind = TYPE_MAP.get(parts[0].lower())
        if not kind or not parts[1]:
            skipped += 1
            continue
        value = parts[1].lower() if kind in CASE_INSENSITIVE else parts[1]
        rules.append((kind, value))
    return rules, skipped


def build_output(path: str, spec: dict, now: str) -> dict:
    merged: dict[tuple[str, str], None] = {}
    report = {"path": path, "sources": [], "ok": True}
    for src in spec["sources"]:
        code, body = fetch(src["url"])
        text = body.decode("utf-8", "replace")
        looks_html = text.lstrip().lower().startswith(("<!doctype", "<html"))
        rules, skipped = parse_rules(text) if code == 200 and not looks_html else ([], 0)
        ok = code == 200 and not looks_html and len(rules) > 0
        before = len(merged)
        for r in rules:
            merged.setdefault(r, None)
        report["sources"].append({**src, "code": code, "ok": ok, "rules": len(rules),
                                  "new": len(merged) - before, "skipped": skipped})
        report["ok"] &= ok
    report["total"] = len(merged)

    out = ROOT / path
    if not report["ok"]:
        # 有上游失效时不覆盖旧文件，避免规则突然变少
        report["kept_old"] = out.exists()
        return report

    order = ["host", "host-suffix", "host-keyword", "host-wildcard", "user-agent",
             "ip-cidr", "ip6-cidr", "ip-asn", "geoip"]
    items = sorted(merged, key=lambda r: (order.index(r[0]), r[1]))
    head = [
        f"# NAME: {spec['title']}",
        f"# UPDATED: {now}",
        f"# TOTAL: {len(items)}",
        "# 本文件由 scripts/build.py 自动合并生成，请勿手动修改。来源：",
        *[f"#   - {s['name']}: {s['url']}" for s in spec["sources"]],
        "",
    ]
    body = [f"{k}, {v}, {spec['policy']}" for k, v in items]
    new_text = "\n".join(head + body) + "\n"
    # 内容没变就不改时间戳，避免每天产生无意义提交
    if out.exists():
        old_rules = [l for l in out.read_text("utf-8").splitlines() if l and not l.startswith("#")]
        if old_rules == body:
            return report
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(new_text, "utf-8")
    report["written"] = True
    return report


def conf_urls() -> list[str]:
    active = [l for l in CONF.read_text("utf-8").splitlines()
              if not l.lstrip().startswith(("#", ";", "//"))]
    urls = re.findall(r"https?://[^\s,]+", "\n".join(active))
    seen, result = set(), []
    for u in urls:
        u = u.split("#")[0]
        if u.startswith(SELF_PREFIX) or "ip-api.com" in u or "generate_204" in u:
            continue  # 本仓库文件在推送前还不存在；测试地址不是资源
        if u not in seen:
            seen.add(u)
            result.append(u)
    return result


def check_links(urls: list[str]) -> list[tuple[str, int]]:
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        codes = list(ex.map(lambda u: fetch(u)[0], urls))
    return list(zip(urls, codes))


def missing_local_resources() -> list[str]:
    urls = re.findall(r"https?://[^\s,]+", CONF.read_text("utf-8"))
    missing = []
    for url in urls:
        if not url.startswith(SELF_PREFIX):
            continue
        path = unquote(urlsplit(url).path).split("/", 4)
        if len(path) != 5 or path[3] != "main":
            continue
        target = (ROOT / path[4]).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():
            missing.append(path[4])
    return sorted(set(missing))


def main() -> int:
    only_check = "--check" in sys.argv
    tz = dt.timezone(dt.timedelta(hours=8))
    now = dt.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S (UTC+8)")
    reports = []
    if not only_check:
        spec = json.loads(SOURCES.read_text("utf-8"))
        for path, out in spec["outputs"].items():
            reports.append(build_output(path, out, now))

    missing = missing_local_resources()
    links = check_links(conf_urls())
    bad = [(u, c) for u, c in links if c != 200]

    lines = [f"# 链接健康状态\n", f"最近检查：{now}\n",
             f"配置文件引用的远程资源：**{len(links)}** 个，可用 **{len(links) - len(bad)}** 个，失效 **{len(bad)}** 个。\n"]
    if missing:
        lines += ["## 缺失的仓库资源\n", *[f"- {path}" for path in missing], ""]
    if bad:
        lines.append("## ❌ 失效链接\n")
        lines += [f"- `{c or '超时'}` {u}" for u, c in bad]
        lines.append("")
    if reports:
        lines.append("## 合并规则\n")
        for r in reports:
            flag = "✅" if r["ok"] else ("⚠️ 有来源失效，保留旧文件" if r.get("kept_old") else "❌")
            lines.append(f"### `{r['path']}` {flag} — 共 {r['total']} 条\n")
            lines.append("| 来源 | 状态 | 规则数 | 新增(去重后) | 跳过 |")
            lines.append("|---|---|---|---|---|")
            for s in r["sources"]:
                lines.append(f"| [{s['name']}]({s['url']}) | {'✅' if s['ok'] else '❌ ' + str(s['code'])} "
                             f"| {s['rules']} | {s['new']} | {s['skipped']} |")
            lines.append("")
    lines.append("## 全部链接\n")
    lines += [f"- {'✅' if c == 200 else '❌'} {u}" for u, c in links]
    STATUS.write_text("\n".join(lines) + "\n", "utf-8")

    print(f"links: {len(links)} total, {len(bad)} broken")
    for u, c in bad:
        print(f"  BROKEN {c} {u}")
    for r in reports:
        print(f"{r['path']}: {r['total']} rules, ok={r['ok']}, written={r.get('written', False)}")
    return int(bool(bad or missing or any(not r["ok"] for r in reports)))


if __name__ == "__main__":
    sys.exit(main())
