#!/usr/bin/env python3
"""Build Chinese registers from seeds + per-item state (no network)."""
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_en import CATS, ROOT, STATE, TYPES, item_state, save_json  # noqa: E402
from fetch_en import load_seeds  # noqa: E402

TARGET = {"book": (15, 25), "course": (10, 15), "docs": (8, 12), "practice": (10, 15), "paper": (45, 55)}


def size_mb(st):
    return round((st.get("bytes") or 0) / 1e6, 1)


def main():
    seeds = load_seeds()
    rows, fails = [], []
    prog = defaultdict(Counter)
    new = reused = 0
    years = Counter()
    paper_recent = paper_classic = 0
    for s in seeds:
        st = item_state(s["id"])
        status = st.get("status", "todo")
        if status != "ok":
            fails.append({
                "资料编号": s["id"], "子目录": f"{s['cat']} {CATS[s['cat']]}", "类型": TYPES[s["type"]],
                "标题": s["title"], "尝试来源": s.get("source", ""),
                "状态": "未尝试" if status == "todo" else "下载/核验失败",
                "原因": (st.get("error") or "")[:500], "访问日期": st.get("access_date", ""),
            })
            continue
        complete = s.get("complete", "完整")
        if complete == "完整":
            prog[s["cat"]][s["type"]] += 1
            prog["ALL"][s["type"]] += 1
        else:
            prog[s["cat"]][s["type"] + "_partial"] += 1
            prog["ALL"][s["type"] + "_partial"] += 1
        if st.get("reused_from"):
            reused += 1
        else:
            new += 1
        y = str(s.get("year") or "")[:4]
        if y.isdigit():
            years[y] += 1
        pw = (s.get("paper") or {}).get("window", "")
        if s["type"] == "paper":
            if pw == "近三年":
                paper_recent += 1
            else:
                paper_classic += 1
        info = st.get("info") or {}
        pages = info.get("pages") or info.get("chapters") or ""
        rows.append({
            "资料编号": s["id"],
            "子目录": f"{s['cat']} {CATS[s['cat']]}",
            "交叉子目录": "; ".join(f"{c} {CATS[c]}" for c in s.get("cross", [])),
            "类型": TYPES[s["type"]],
            "资料形态": s.get("material", ""),
            "标题": s["title"],
            "作者": s.get("authors", ""),
            "学校或机构": s.get("school", ""),
            "年份": s.get("year", ""),
            "版本": s.get("version", ""),
            "语言": "英文" if s.get("lang") == "en" else s.get("lang", ""),
            "层次": s.get("level", ""),
            "先修要求": s.get("prereq", ""),
            "主题": s.get("topics") or s.get("goal", ""),
            "原始来源": s.get("source", ""),
            "下载地址": st.get("download_url", "") or st.get("reused_from", ""),
            "本地路径": s["out"],
            "完整性状态": "完整（已核验）" if complete == "完整" else "部分资料（已核验，范围见说明）",
            "核验说明": st.get("verify", ""),
            "范围说明": s.get("scope", ""),
            "许可证": s.get("license", ""),
            "来源方式": f"已有复用（{st['reused_from']}）" if st.get("reused_from") else "新下载",
            "页数或文件": pages or info.get("files", ""),
            "大小MB": size_mb(st),
            "访问日期": st.get("access_date", ""),
            "时间窗口": pw,
            "经典保留理由": (s.get("paper") or {}).get("classic_reason", ""),
            "备注": s.get("note", ""),
        })

    def write(path, recs, fields=None):
        path = ROOT / path
        path.parent.mkdir(parents=True, exist_ok=True)
        fields = fields or (list(recs[0].keys()) if recs else ["空"])
        with open(path, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(recs)

    rows.sort(key=lambda r: r["资料编号"])
    write("catalog_cn.csv", rows)
    write("download_failures_cn.csv", fails,
          ["资料编号", "子目录", "类型", "标题", "尝试来源", "状态", "原因", "访问日期"])

    n_paper = paper_recent + paper_classic
    pct = f"{100*paper_recent/n_paper:.1f}%" if n_paper else "-"
    prog_rows = []
    rec_all = {
        "范围": "整库",
        "教材 完整/部分": f"{prog['ALL']['book']}/{prog['ALL']['book_partial']}",
        "教材目标": "15–25",
        "课程 完整/部分": f"{prog['ALL']['course']}/{prog['ALL']['course_partial']}",
        "课程目标": "10–15",
        "工具文档 完整/部分": f"{prog['ALL']['docs']}/{prog['ALL']['docs_partial']}",
        "工具文档目标": "8–12",
        "实践 完整/部分": f"{prog['ALL']['practice']}/{prog['ALL']['practice_partial']}",
        "实践目标": "10–15",
        "论文 已核验": n_paper,
        "论文近三年": paper_recent,
        "论文经典": paper_classic,
        "近三年占比": pct,
        "已有复用": reused,
        "新下载": new,
        "失败或未完成": len(fails),
        "状态": "见各子目录",
    }
    prog_rows.append(rec_all)
    for c, name in CATS.items():
        prog_rows.append({
            "范围": f"{c} {name}",
            "教材 完整/部分": f"{prog[c]['book']}/{prog[c]['book_partial']}",
            "教材目标": "整库合计",
            "课程 完整/部分": f"{prog[c]['course']}/{prog[c]['course_partial']}",
            "课程目标": "整库合计",
            "工具文档 完整/部分": f"{prog[c]['docs']}/{prog[c]['docs_partial']}",
            "工具文档目标": "整库合计",
            "实践 完整/部分": f"{prog[c]['practice']}/{prog[c]['practice_partial']}",
            "实践目标": "整库合计",
            "论文 已核验": prog[c]["paper"],
            "论文近三年": "", "论文经典": "", "近三年占比": "",
            "已有复用": "", "新下载": "",
            "失败或未完成": sum(1 for s in seeds if s["cat"] == c and item_state(s["id"]).get("status") != "ok"),
            "状态": "",
        })
    write("progress_cn.csv", prog_rows)

    def in_range(n, lo, hi):
        return lo <= n <= hi + 3  # small overflow ok

    summary = {
        "verified_items": len(rows),
        "complete": sum(r["完整性状态"].startswith("完整") for r in rows),
        "partial": sum(r["完整性状态"].startswith("部分") for r in rows),
        "new": new, "reused": reused, "failed_or_todo": len(fails),
        "by_type": dict(Counter(r["类型"] for r in rows)),
        "book": prog["ALL"]["book"], "course": prog["ALL"]["course"],
        "docs": prog["ALL"]["docs"] + prog["ALL"]["docs_partial"],
        "practice": prog["ALL"]["practice"] + prog["ALL"]["practice_partial"],
        "paper": n_paper, "paper_recent": paper_recent, "paper_classic": paper_classic,
        "paper_recent_pct": pct, "years": dict(sorted(years.items())),
        "bytes_mb": round(sum(r["大小MB"] for r in rows if isinstance(r["大小MB"], (int, float))), 1),
        "targets_met": {
            "book": in_range(prog["ALL"]["book"], *TARGET["book"]),
            "course": in_range(prog["ALL"]["course"], *TARGET["course"]),
            "docs": in_range(prog["ALL"]["docs"] + prog["ALL"]["docs_partial"], *TARGET["docs"]),
            "practice": in_range(prog["ALL"]["practice"] + prog["ALL"]["practice_partial"], *TARGET["practice"]),
            "paper": in_range(n_paper, *TARGET["paper"]),
        },
    }
    save_json(STATE / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
