"""Shared helpers for control_systems_automation_literature.

Downloaded content is untrusted: written under STAGING / the library tree and never
imported or executed. Run every script with `python3 -I`.
"""
import fcntl
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
STATE = ROOT / "state"
ITEMS = STATE / "items"
CACHE = Path(os.environ.get("CSA_CACHE", "/root/.cache/csa_lit"))
STAGING = CACHE / "staging"
PYLIB = CACHE / "pylib"
LOCK_DIR = Path("/tmp/lmm_ratelimit")
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0.0.0 Safari/537.36")
UA_ALT = ("Mozilla/5.0 (compatible; control_systems_automation_literature/1.0; "
          "personal literature collection, low request rate)")
ACCESS_DATE = time.strftime("%Y-%m-%d", time.gmtime())
SEARCH_DATE = "2026-10-30"
WINDOW_START, WINDOW_END = "2023-10-30", "2026-10-30"

INTERVAL = {"arxiv.org": 4.0, "export.arxiv.org": 4.0, "api.github.com": 2.0,
            "api.crossref.org": 1.5, "ocw.mit.edu": 2.0}
RTD_HOSTS = ("readthedocs.io", "python-control.readthedocs.io", "www.do-mpc.com",
             "open62541.org", "docs.scipy.org", "docs.octave.org")

CATS = {
    "01": "数学与信号基础",
    "02": "经典控制",
    "03": "现代控制",
    "04": "估计与系统辨识",
    "05": "进阶控制",
    "06": "学习与数据驱动控制",
    "07": "工业自动化",
    "08": "硬件与实时系统",
    "09": "仿真与工程实践",
}
TYPES = {
    "book": "教材/参考书",
    "course": "大学课程/讲义",
    "docs": "官方工具文档",
    "practice": "实验及实践案例",
    "paper": "论文/综述/学术教程",
}


def interval_for(key):
    if key in INTERVAL:
        return INTERVAL[key]
    return 8.0 if key.endswith(RTD_HOSTS) else 1.2


def host_key(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    return "arxiv.org" if host.endswith("arxiv.org") else host


def wait(key, interval):
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOCK_DIR / re.sub(r"[^A-Za-z0-9._-]", "_", key), "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        raw = f.read().strip()
        try:
            last = float(raw) if raw else 0.0
        except ValueError:
            last = 0.0
        delay = interval - (time.time() - last)
        if delay > 0:
            time.sleep(min(delay, interval))
        f.seek(0)
        f.truncate()
        f.write(str(time.time()))


def http(url, method="GET", timeout=120, tries=4, headers=None, dest=None, max_bytes=None):
    key = host_key(url)
    err = ""
    for attempt in range(tries):
        wait(key, interval_for(key))
        try:
            h = {"User-Agent": UA, "Accept": "*/*", **(headers or {})}
            req = urllib.request.Request(url, headers=h, method=method)
            try:
                resp = urllib.request.urlopen(req, timeout=timeout)
            except (ssl.SSLError, urllib.error.URLError) as e:
                reason = str(getattr(e, "reason", e))
                if isinstance(e, ssl.SSLError) or "SSL" in reason or "CERTIFICATE" in reason:
                    resp = urllib.request.urlopen(req, timeout=timeout, context=ssl._create_unverified_context())
                else:
                    raise
            with resp as r:
                info = {"status": r.status, "url": r.geturl(), "ctype": r.headers.get("Content-Type", ""),
                        "length": r.headers.get("Content-Length"), "err": "",
                        "last_modified": r.headers.get("Last-Modified", "")}
                if method == "HEAD":
                    info["body"] = None
                    return info
                if dest:
                    n = 0
                    tmp = Path(str(dest) + ".part")
                    tmp.parent.mkdir(parents=True, exist_ok=True)
                    with open(tmp, "wb") as out:
                        while True:
                            chunk = r.read(1 << 20)
                            if not chunk:
                                break
                            n += len(chunk)
                            if max_bytes and n > max_bytes:
                                raise ValueError(f"exceeds max_bytes {max_bytes}")
                            out.write(chunk)
                    os.replace(tmp, dest)
                    info["body"] = None
                    info["bytes"] = n
                else:
                    info["body"] = r.read()
                return info
        except urllib.error.HTTPError as e:
            err = f"HTTP {e.code}"
            if e.code == 429:
                ra = e.headers.get("Retry-After", "") if e.headers else ""
                time.sleep(min(int(ra), 600) if ra.isdigit() else 60 * (attempt + 1))
                continue
            if e.code in (500, 502, 503, 504):
                time.sleep(5 * (attempt + 1))
                continue
            return {"status": e.code, "body": None, "url": url, "ctype": "", "length": None, "err": err}
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
            time.sleep(3 * (attempt + 1))
    return {"status": 0, "body": None, "url": url, "ctype": "", "length": None, "err": err}


def load_json(path, default=None):
    p = Path(path)
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding="utf-8"))


def save_json(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, p)


def item_state(item_id):
    return load_json(ITEMS / f"{item_id}.json", {})


def save_item_state(item_id, st):
    save_json(ITEMS / f"{item_id}.json", st)


def norm_words(s):
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return [w for w in s.split() if len(w) > 2 and w not in {"the", "and", "for", "with", "from", "into"}]


def use_pypdf():
    if str(PYLIB) not in sys.path:
        sys.path.insert(0, str(PYLIB))
    import pypdf  # noqa: E402
    import logging
    logging.getLogger("pypdf").setLevel(logging.ERROR)
    return pypdf
