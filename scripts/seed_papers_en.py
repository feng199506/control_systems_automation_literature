#!/usr/bin/env python3
"""Build paper seeds from a curated arXiv id list (metadata via arXiv API)."""
import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import sys
from pathlib import Path as _P
sys.path.insert(0, str(_P(__file__).resolve().parent))
from common_en import UA, WINDOW_START  # noqa: E402

SEEDS = Path(__file__).resolve().parent / "seeds"
ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

# (arxiv_id, cat, cross, window, classic_reason, topics, order)
# window: 近三年 | 经典/较早
CURATED = [
    ("2606.01959", "02", [], "近三年", "", "PID、抗饱和、调参", 1),
    ("2409.00538", "02", [], "近三年", "", "PID 调参、元启发式综述", 2),
    ("2610.20248", "02", ["05"], "近三年", "", "频率响应、IQC、数据驱动鲁棒", 3),
    ("2412.13082", "03", ["05"], "近三年", "", "多面体控制、状态反馈、不变集", 1),
    ("2608.22204", "03", ["05"], "近三年", "", "对抗控制、可扩展性、非线性", 2),
    ("2610.36773", "03", ["05"], "近三年", "", "控制不变性、多面体、计算复杂性", 3),
    ("2512.06315", "04", ["06"], "近三年", "", "控制导向系统辨识综述", 1),
    ("2506.03650", "04", [], "近三年", "", "辨识采样、噪声、闭环", 2),
    ("2605.11460", "04", [], "近三年", "", "系统辨识、区间神经网络、不确定性", 3),
    ("2404.18267", "04", ["03"], "近三年", "", "网络化算子、连续稳定性、辨识", 4),
    ("2501.17544", "04", ["02"], "近三年", "", "零极点辨识、动态特性", 5),
    ("2512.20354", "04", [], "近三年", "", "多速率 EKF 教程、状态估计", 6),
    ("2609.27506", "04", [], "近三年", "", "Kalman、共形预测、置信域", 7),
    ("2605.02306", "04", [], "近三年", "", "贝叶斯滤波、自然梯度", 8),
    ("2510.24228", "04", [], "近三年", "", "UKF、联合/对偶估计", 9),
    ("2610.31295", "05", [], "近三年", "", "MPC 综述、预测模型、约束", 1),
    ("2608.17902", "05", [], "近三年", "", "自适应 MPC 综述", 2),
    ("2606.06642", "05", [], "近三年", "", "非线性 MPC、离散化方法综述", 3),
    ("2604.21030", "05", ["06"], "近三年", "", "强化学习与 MPC 结合综述", 4),
    ("2511.17865", "05", ["07"], "近三年", "", "制造过程生成式 MPC 综述", 5),
    ("2605.05575", "05", ["03"], "近三年", "", "不变集 MPC、可行性", 6),
    ("2405.01753", "05", [], "近三年", "", "反馈线性化 MPC、输入约束", 7),
    ("2507.23139", "05", ["03"], "近三年", "", "鲁棒控制、提升线性化", 8),
    ("2604.07644", "05", [], "近三年", "", "鲁棒非线性 MPC、可达性、安全", 9),
    ("2505.00210", "05", ["07"], "近三年", "", "制造过程自适应控制、生成模型综述", 10),
    ("2403.17142", "05", [], "近三年", "", "MRAC、随机浅层网络逼近", 11),
    ("2408.13271", "05", ["06"], "近三年", "", "控制障碍函数 CBF 综述、安全约束", 12),
    ("2610.23809", "05", [], "近三年", "", "Lyapunov 指数、稳定性综述", 13),
    ("2610.17604", "05", [], "近三年", "", "Lyapunov 证书、稳定性迁移", 14),
    ("2610.05689", "05", ["06"], "近三年", "", "不变集、Lyapunov、可信控制", 15),
    ("2511.15044", "06", ["03"], "近三年", "", "数据驱动网络控制", 1),
    ("2609.37683", "06", ["04"], "近三年", "", "数据驱动控制、在线激励设计", 2),
    ("2610.27599", "06", ["03"], "近三年", "", "数据驱动最小能量控制、有限样本", 3),
    ("2610.05724", "06", ["03"], "近三年", "", "量化数据驱动镇定", 4),
    ("2609.28883", "06", ["03"], "近三年", "", "直接/间接数据驱动、平衡流形先验", 5),
    ("2407.11069", "06", [], "近三年", "", "联邦学习与控制综述", 6),
    ("2610.08112", "06", ["05"], "近三年", "", "强化学习与 NMPC 比较", 7),
    ("2610.28160", "07", [], "近三年", "", "PLC 编程、工厂感知智能体", 1),
    ("2610.28675", "07", [], "近三年", "", "LLM 生成 PLC 程序评测", 2),
    ("2610.02982", "07", ["09"], "近三年", "", "PLC 程序闭环仿真基准", 3),
    ("2609.38528", "07", [], "近三年", "", "工控系统审计、联锁/不可恢复故障", 4),
    ("2610.34095", "03", ["04"], "近三年", "", "Markov 跳变系统最优线性滤波、数字控制", 4),
    ("2610.34895", "03", [], "近三年", "", "随机互联系统、采样/抽象", 5),
    # classics
    ("1811.05890", "06", ["05"], "经典/较早",
     "DeePC 奠基论文，数据使能预测控制的标准出处", "DeePC、行为方法、数据驱动 MPC", 8),
    ("1910.06691", "05", ["06"], "经典/较早",
     "学习型 MPC 与安全学习的权威综述，后续安全约束文献普遍引用", "学习型 MPC、安全学习", 16),
    ("1906.04679", "06", ["05"], "经典/较早",
     "带稳定性与鲁棒保证的数据驱动 MPC 代表作", "数据驱动 MPC、鲁棒性", 9),
    ("2211.12016", "06", ["04"], "经典/较早",
     "直接与间接数据驱动控制的桥梁论文，Willems 引理与辨识的对照", "直接/间接数据驱动、Willems 引理", 10),
    ("1806.09460", "06", ["05"], "经典/较早",
     "从控制视角系统梳理强化学习的经典教程", "强化学习、LQR、策略梯度", 11),
    ("2301.06073", "07", ["06"], "经典/较早",
     "过程控制中机器学习方法的综述，工业应用入口（略早于三年窗口）", "过程控制、机器学习", 5),
    ("2305.02066", "05", ["03"], "经典/较早",
     "非线性 ODE 反步法模块化设计综述，Lyapunov 设计代表", "反步法、非线性、Lyapunov", 17),
]


def arxiv_batch(ids):
    out = {}
    for i in range(0, len(ids), 80):
        chunk = ids[i:i + 80]
        url = ("https://export.arxiv.org/api/query?max_results=200&id_list=" + ",".join(chunk))
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/atom+xml"})
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read()
        for e in ET.fromstring(body).findall("a:entry", ATOM):
            abs_url = e.findtext("a:id", "", ATOM)
            vid = abs_url.rsplit("/abs/", 1)[-1]
            base = vid.rsplit("v", 1)[0] if "v" in vid.split("/")[-1] else vid
            # keep with version stripped: 1811.05890
            key = __import__("re").sub(r"v\d+$", "", vid)
            out[key] = {
                "title": " ".join(e.findtext("a:title", "", ATOM).split()),
                "authors": [a.findtext("a:name", "", ATOM) for a in e.findall("a:author", ATOM)],
                "published": (e.findtext("a:published", "", ATOM) or "")[:10],
                "abstract": " ".join(e.findtext("a:summary", "", ATOM).split()),
                "doi": e.findtext("arxiv:doi", "", ATOM),
                "comment": e.findtext("arxiv:comment", "", ATOM),
                "latest": vid,
            }
        time.sleep(3.5)
    return out


def words(title):
    stop = {"the", "and", "for", "with", "from", "into", "a", "an", "of", "in", "on", "to"}
    return [w for w in __import__("re").findall(r"[A-Za-z]{3,}", title) if w.lower() not in stop][:6]


def main():
    ids = [c[0] for c in CURATED]
    meta = arxiv_batch(ids)
    papers = []
    missing = []
    for i, (ax, cat, cross, window, reason, topics, order) in enumerate(CURATED, 1):
        m = meta.get(ax)
        if not m:
            missing.append(ax)
            continue
        year = m["published"][:4]
        pid = f"CS{cat}P{order:02d}"
        # unique-ify if collision
        used = {p["id"] for p in papers}
        if pid in used:
            k = 1
            while f"{pid}{chr(96+k)}" in used or f"{pid}_{k}" in used:
                k += 1
            pid = f"{pid}_{k}"
        title_words = words(m["title"])
        papers.append({
            "id": pid, "cat": cat, "cross": cross, "type": "paper",
            "material": "论文/综述/学术教程",
            "title": m["title"],
            "authors": "; ".join(m["authors"][:12]),
            "school": "",
            "year": year, "version": f"arXiv:{m['latest']}",
            "lang": "en",
            "level": "研究生" if window.startswith("近") else "研究生（经典）",
            "prereq": "对应子目录教材与课程",
            "topics": topics,
            "source": f"https://arxiv.org/abs/{ax}",
            "license": "arXiv 预印本（以论文页声明为准）",
            "goal": topics,
            "order": order,
            "out": f"{ {'01':'01_foundations','02':'02_classical_control','03':'03_modern_control','04':'04_estimation_identification','05':'05_advanced_control','06':'06_learning_control','07':'07_industrial_automation','08':'08_hardware_realtime','09':'09_simulation_practice'}[cat] }/papers/{year}_{m['authors'][0].split()[-1]}_{ax.replace('.','')}_en.pdf",
            "get": {"kind": "pdf", "urls": [f"https://arxiv.org/pdf/{m['latest']}.pdf", f"https://arxiv.org/pdf/{ax}.pdf"]},
            "expect": {"title_words": title_words, "min_pages": 5, "min_ratio": 0.5},
            "complete": "完整", "scope": "", "note": reason,
            "use": "精读/按需", "stack": "",
            "paper": {
                "first_public": m["published"], "venue": "arXiv",
                "window": window, "classic_reason": reason, "arxiv": ax, "doi": m.get("doi") or "",
            },
        })
    # fix duplicate ids properly
    seen = {}
    for p in papers:
        if p["id"] in seen:
            seen[p["id"]] += 1
            p["id"] = p["id"] + f"x{seen[p['id']]}"
        else:
            seen[p["id"]] = 1
    SEEDS.mkdir(parents=True, exist_ok=True)
    (SEEDS / "P_papers_en.json").write_text(json.dumps(papers, ensure_ascii=False, indent=1), encoding="utf-8")
    n_recent = sum(1 for p in papers if p["paper"]["window"] == "近三年")
    print(f"papers {len(papers)} recent {n_recent} ({100*n_recent/max(len(papers),1):.1f}%) missing {missing}")


if __name__ == "__main__":
    main()
