#!/usr/bin/env python3
"""Write seed JSON for books, courses, tools, and practice (no papers)."""
import json
from pathlib import Path

SEEDS = Path(__file__).resolve().parent / "seeds"
IPM = "/root/industrial_process_monitoring_literature"
AI = "/root/ai_undergraduate_graduate_curriculum_literature"
PS = "/root/probability_statistics_curriculum_literature"


def reuse(path, source):
    return {"kind": "reuse"}, {"path": path, "source": source}


def item(**kw):
    rec = dict(kw)
    rec.setdefault("lang", "en")
    rec.setdefault("cross", [])
    rec.setdefault("complete", "完整")
    rec.setdefault("scope", "")
    rec.setdefault("note", "")
    rec.setdefault("use", "通读")
    rec.setdefault("stack", "")
    rec.setdefault("school", rec.get("authors", ""))
    rec.setdefault("expect", {})
    rec.setdefault("paper", {})
    return rec


books, courses, tools, practice = [], [], [], []

# ---------- 01 foundations books ----------
books.append(item(
    id="CS01B01", cat="01", type="book", material="教材/参考书",
    title="Elementary Differential Equations with Boundary Value Problems (Free Edition 1.01)",
    authors="William F. Trench", school="Trinity University",
    year="2013", version="Free Edition 1.01 (December 2013)",
    level="本科基础", prereq="微积分（含偏导数）",
    topics="常微分方程、线性系统、Laplace 变换、边值问题",
    source="https://digitalcommons.trinity.edu/mono/9/",
    license="CC BY-NC-SA 3.0",
    goal="控制所需的微分方程与 Laplace 变换基础",
    order=1, out="01_foundations/books/Trench_ElementaryDifferentialEquationsBVP_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://digitalcommons.trinity.edu/cgi/viewcontent.cgi?article=1008&context=mono",
        "http://ramanujan.math.trinity.edu/wtrench/texts/TRENCH_FREE_DIFFEQN_BVP.PDF",
        "https://digitalcommons.trinity.edu/cgi/viewcontent.cgi?article=1007&context=mono",
    ]},
    expect={"title_words": ["Elementary", "Differential", "Equations"], "min_pages": 400},
))
books.append(item(
    id="CS01B02", cat="01", type="book", material="教材/参考书",
    title="Linear Algebra (4th edition)",
    authors="Jim Hefferon", school="University of Vermont / Saint Michael's College",
    year="2020", version="Fourth edition（作者站点当前 PDF）",
    level="本科基础", prereq="一学期微积分",
    topics="线性方程组、向量空间、线性映射、行列式、特征值",
    source="https://hefferon.net/linearalgebra/",
    license="GFDL / 作者声明 Free",
    goal="控制状态空间所需的本科线性代数",
    order=2, out="01_foundations/books/Hefferon_LinearAlgebra_4thEd_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://jheffero.w3.uvm.edu/linearalgebra/book.pdf",
        "https://hefferon.net/linearalgebra/book.pdf",
        "http://joshua.smcvt.edu/linearalgebra/book.pdf",
    ]},
    expect={"title_words": ["Linear", "Algebra", "Hefferon"], "min_pages": 400},
))
g, r = reuse(f"{PS}/books/BoydVandenberghe_IntroductionAppliedLinearAlgebra_2018_en.pdf",
             "https://web.stanford.edu/~boyd/vmls/")
books.append(item(
    id="CS01B03", cat="01", type="book", material="教材/参考书",
    title="Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares",
    authors="Stephen Boyd; Lieven Vandenberghe", school="Stanford University / UCLA",
    year="2018", version="Cambridge 2018（作者公开 PDF）",
    level="本科基础", prereq="微积分",
    topics="向量、矩阵、最小二乘、约束最小二乘、动态系统初步",
    source="https://web.stanford.edu/~boyd/vmls/",
    license="作者/Cambridge 公开教学 PDF",
    goal="把线性代数接到最小二乘、辨识与状态估计",
    order=3, out="01_foundations/books/BoydVandenberghe_IntroductionAppliedLinearAlgebra_2018_en.pdf",
    get=g, reuse=r,
    expect={"title_words": ["Applied", "Linear", "Algebra"], "min_pages": 400},
    note="已有复用：probability_statistics_curriculum_literature",
))
books.append(item(
    id="CS01B04", cat="01", type="book", material="教材/参考书",
    title="Structure and Interpretation of Signals and Systems (2nd ed., v2.04)",
    authors="Edward A. Lee; Pravin Varaiya", school="UC Berkeley",
    year="2011", version="Second Edition Version 2.04",
    level="本科基础", prereq="微积分",
    topics="信号、系统、状态、频率域、采样、反馈与控制导引",
    source="https://ptolemy.berkeley.edu/books/leevaraiya/",
    license="作者站点公开 PDF（版权作者保留）",
    goal="信号与系统（含离散时间与计算观点），衔接传递函数与采样",
    order=4, out="01_foundations/books/LeeVaraiya_StructureInterpretationSignalsSystems_2ndEd_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://ptolemy.berkeley.edu/books/leevaraiya/releases/LeeVaraiya_DigitalV2_04.pdf",
        "https://leevaraiya.org/releases/LeeVaraiya_DigitalV2_04.pdf",
    ]},
    expect={"title_words": ["Structure", "Interpretation", "Signals", "Systems"], "min_pages": 400},
))
books.append(item(
    id="CS01B05", cat="01", type="book", material="教材/参考书",
    title="The Scientist and Engineer's Guide to Digital Signal Processing",
    authors="Steven W. Smith", school="California Technical Publishing",
    year="1997", version="作者站点完整电子版",
    level="本科基础", prereq="微积分、基础电路或编程",
    topics="离散信号、卷积、DFT/FFT、滤波器、采样与重建",
    source="https://www.dspguide.com/pdfbook.htm",
    license="作者公开电子版（版权作者保留，允许个人使用）",
    goal="数字信号处理与 Z 域直觉，服务离散控制与数据采集",
    order=5, out="01_foundations/books/Smith_ScientistEngineersGuideDSP_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://www.dspguide.com/pdfbook.pdf",
        "http://www.dspguide.com/pdfbook.pdf",
    ]},
    expect={"title_words": ["Digital", "Signal", "Processing"], "min_pages": 400},
))

# ---------- 02 classical books ----------
g, r = reuse(f"{IPM}/books/Astrom_FeedbackSystems_2ndEd_v3.1.5_en.pdf", "https://fbswiki.org/")
books.append(item(
    id="CS02B01", cat="02", type="book", material="教材/参考书", cross=["03"],
    title="Feedback Systems: An Introduction for Scientists and Engineers (2nd ed.)",
    authors="Karl Johan Åström; Richard M. Murray",
    school="Lund University / Caltech",
    year="2021", version="第 2 版 v3.1.5（2020-07-24 公开稿）",
    level="本科进阶", prereq="微分方程、线性代数、Laplace 变换",
    topics="反馈、传递函数、稳定性、PID、状态空间、观测器",
    source="https://fbswiki.org/",
    license="作者公开 PDF（Princeton University Press）",
    goal="经典与现代控制的主线教材，覆盖反馈、PID 与状态空间入门",
    order=1, out="02_classical_control/books/Astrom_FeedbackSystems_2ndEd_v3.1.5_en.pdf",
    get=g, reuse=r,
    expect={"title_words": ["Feedback", "Systems"], "min_pages": 400},
    note="已有复用：industrial_process_monitoring_literature 14-004",
))
g, r = reuse(f"{IPM}/books/Doyle_FeedbackControlTheory_1990_en.pdf",
             "http://www.control.utoronto.ca/people/profs/francis/dft.pdf")
books.append(item(
    id="CS02B02", cat="02", type="book", material="教材/参考书", cross=["05"],
    title="Feedback Control Theory",
    authors="John Doyle; Bruce Francis; Allen Tannenbaum",
    school="Caltech / University of Toronto",
    year="1990", version="Macmillan 1990（作者公开电子版）",
    level="研究生", prereq="经典控制、复变函数",
    topics="回路成形、鲁棒性、灵敏度、H∞ 入门",
    source="http://www.control.utoronto.ca/people/profs/francis/",
    license="作者主页公开 PDF",
    goal="频率域鲁棒反馈设计的经典短教材",
    order=2, out="02_classical_control/books/Doyle_FeedbackControlTheory_1990_en.pdf",
    get=g, reuse=r,
    expect={"title_words": ["Feedback", "Control", "Theory"], "min_pages": 150},
    note="已有复用：industrial_process_monitoring_literature 14-009",
))
books.append(item(
    id="CS02B03", cat="02", type="book", material="教材/参考书", cross=["08"],
    title="Operational Amplifiers: Theory and Practice",
    authors="James K. Roberge", school="MIT",
    year="1975", version="MIT OCW 公开电子版（版权已归作者并授权 OCW）",
    level="本科进阶", prereq="电路、Laplace 变换",
    topics="模拟反馈、稳定性、补偿、运算放大器应用",
    source="https://ocw.mit.edu/courses/res-6-010-electronic-feedback-systems-spring-2013/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="用运放理解反馈、稳定性与补偿，衔接硬件实现",
    order=3, out="02_classical_control/books/Roberge_OperationalAmplifiersTheoryPractice_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://ocw.mit.edu/courses/res-6-010-electronic-feedback-systems-spring-2013/resources/mitres_6-010s13_comchaptrs_pdf/MITRES_6-010S13_comchaptrs.pdf",
        "https://ocw.mit.edu/courses/res-6-010-electronic-feedback-systems-spring-2013/MITRES_6-010S13_opamp.pdf",
    ], "max_mb": 80},
    expect={"title_words": ["Operational", "Amplifiers"], "min_pages": 300, "allow_scan": True},
))

# ---------- 03 modern ----------
books.append(item(
    id="CS03B01", cat="03", type="book", material="教材/参考书", cross=["05"],
    title="Mathematical Control Theory: Deterministic Finite Dimensional Systems (2nd ed.)",
    authors="Eduardo D. Sontag", school="Rutgers University",
    year="1998", version="Springer TAM 6, Second Edition（作者站点公开）",
    level="研究生", prereq="线性代数、微分方程、实分析入门",
    topics="能控性、能观性、反馈镇定、观测器、最优性、Lyapunov",
    source="https://sontaglab.org/mct.html",
    license="Springer 版权；作者获准在站点公开",
    goal="现代控制的严格数学教材",
    order=1, out="03_modern_control/books/Sontag_MathematicalControlTheory_2ndEd_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://sontaglab.org/FTPDIR/sontag_mathematical_control_theory_springer98.pdf",
        "http://www.sontaglab.org/FTPDIR/sontag_mathematical_control_theory_springer98.pdf",
    ]},
    expect={"title_words": ["Mathematical", "Control", "Theory"], "min_pages": 400, "allow_scan": True},
))

# ---------- 04 estimation ----------
g, r = reuse(f"{IPM}/books/Sarkka_BayesianFilteringSmoothing_2ndEd_en.pdf",
             "https://users.aalto.fi/~ssarkka/")
books.append(item(
    id="CS04B01", cat="04", type="book", material="教材/参考书",
    title="Bayesian Filtering and Smoothing (2nd ed.)",
    authors="Simo Särkkä; Lennart Svensson", school="Aalto University / Chalmers",
    year="2023", version="第 2 版作者官网在线版",
    level="研究生", prereq="概率、线性系统、状态空间",
    topics="Kalman 滤波、平滑、EKF/UKF、粒子滤波、贝叶斯状态估计",
    source="https://users.aalto.fi/~ssarkka/",
    license="作者官网免费在线版",
    goal="状态估计与 Kalman 滤波系统教材",
    order=1, out="04_estimation_identification/books/Sarkka_BayesianFilteringSmoothing_2ndEd_en.pdf",
    get=g, reuse=r,
    expect={"title_words": ["Bayesian", "Filtering"], "min_pages": 300},
    note="已有复用：industrial_process_monitoring_literature 14-006",
))
g, r = reuse(f"{IPM}/books/Pillonetto_RegularizedSystemIdentification_2022_en.pdf",
             "https://link.springer.com/book/10.1007/978-3-030-95860-2")
books.append(item(
    id="CS04B02", cat="04", type="book", material="教材/参考书",
    title="Regularized System Identification: Learning Dynamic Models from Data",
    authors="Gianluigi Pillonetto; Tianshi Chen; Alessandro Chiuso; Giuseppe De Nicolao; Lennart Ljung",
    school="University of Padova / Linköping University 等",
    year="2022", version="Springer 开放获取 2022",
    level="研究生", prereq="线性系统、最小二乘、概率",
    topics="正则化辨识、核方法、从数据学习动态模型",
    source="https://link.springer.com/book/10.1007/978-3-030-95860-2",
    license="CC BY（Springer OA）",
    goal="系统辨识从经典 PEM 走到正则化/核方法",
    order=2, out="04_estimation_identification/books/Pillonetto_RegularizedSystemIdentification_2022_en.pdf",
    get=g, reuse=r,
    expect={"title_words": ["Regularized", "System", "Identification"], "min_pages": 250},
    note="已有复用：industrial_process_monitoring_literature 14-021",
))

# ---------- 05 advanced ----------
g, r = reuse(f"{AI}/books/Liberzon_CalculusOfVariationsOptimalControl_2011_en.pdf",
             "http://liberzon.csl.illinois.edu/teaching/cvoc.pdf")
books.append(item(
    id="CS05B01", cat="05", type="book", material="教材/参考书",
    title="Calculus of Variations and Optimal Control Theory: A Concise Introduction",
    authors="Daniel Liberzon", school="University of Illinois Urbana-Champaign",
    year="2012", version="Princeton 2012（作者公开教学 PDF，2011 稿）",
    level="研究生", prereq="线性系统、多元微积分",
    topics="变分法、Pontryagin 极大值原理、LQR、动态规划",
    source="http://liberzon.csl.illinois.edu/teaching/cvoc.html",
    license="作者公开教学 PDF",
    goal="最优控制理论入门（LQR 的变分/PMP 基础）",
    order=1, out="05_advanced_control/books/Liberzon_CalculusOfVariationsOptimalControl_2011_en.pdf",
    get=g, reuse=r,
    expect={"title_words": ["Calculus", "Variations", "Optimal", "Control"], "min_pages": 200},
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
))
books.append(item(
    id="CS05B02", cat="05", type="book", material="教材/参考书", cross=["04"],
    title="Optimization-Based Control",
    authors="Richard M. Murray", school="Caltech",
    year="2023", version="v2.3h / 完整稿（站点当前完整 PDF）",
    level="本科高年级/研究生", prereq="Feedback Systems（Åström & Murray）",
    topics="轨迹生成、最优控制、滚动时域、Kalman、传感器融合",
    source="https://fbswiki.org/wiki/index.php/OBC",
    license="Caltech 版权，作者公开个人使用稿",
    goal="把 LQR/MPC/Kalman 接到 python-control 实现",
    order=2, out="05_advanced_control/books/Murray_OptimizationBasedControl_en.pdf",
    get={"kind": "pdf", "urls": [
        "http://www.cds.caltech.edu/~murray/books/AM08/pdf/obc-complete_12Mar2023.pdf",
        "http://www.cds.caltech.edu/~murray/books/AM08/pdf/obc-complete_23Feb2022.pdf",
        "https://www.cds.caltech.edu/~murray/books/AM08/pdf/obc-complete_23Feb2022.pdf",
    ]},
    expect={"title_words": ["Optimization", "Based", "Control"], "min_pages": 150},
))
g, r = reuse(f"{IPM}/books/Rawlings_ModelPredictiveControl_2ndEd_en.pdf",
             "https://sites.engineering.ucsb.edu/~jbraw/mpc/")
books.append(item(
    id="CS05B03", cat="05", type="book", material="教材/参考书",
    title="Model Predictive Control: Theory, Computation, and Design (2nd ed.)",
    authors="James B. Rawlings; David Q. Mayne; Moritz M. Diehl",
    school="UCSB / Imperial College / University of Freiburg",
    year="2017", version="第 2 版第 5 次印刷（作者官网 PDF）",
    level="研究生", prereq="状态空间、优化、离散系统",
    topics="MPC 稳定性、约束、计算、滚动时域估计",
    source="https://sites.engineering.ucsb.edu/~jbraw/mpc/",
    license="作者官网免费 PDF",
    goal="MPC 理论与计算的权威教材",
    order=3, out="05_advanced_control/books/Rawlings_ModelPredictiveControl_2ndEd_en.pdf",
    get=g, reuse=r,
    expect={"title_words": ["Model", "Predictive", "Control"], "min_pages": 500},
    note="已有复用：industrial_process_monitoring_literature 14-005",
))
books.append(item(
    id="CS05B04", cat="05", type="book", material="教材/参考书",
    title="Predictive Control for Linear and Hybrid Systems",
    authors="Francesco Borrelli; Alberto Bemporad; Manfred Morari",
    school="UC Berkeley / IMT Lucca / ETH Zurich",
    year="2017", version="Cambridge 2017（作者实验室公开 PDF）",
    level="研究生", prereq="线性系统、凸优化、约束控制",
    topics="线性/混杂 MPC、显式 MPC、多参数规划、实时实现",
    source="https://cse.lab.imtlucca.it/~bemporad/publications/papers/BBMbook.pdf",
    license="Cambridge 版权；作者实验室公开 PDF",
    goal="与 Rawlings 互补的 MPC 教材，侧重显式与混杂系统",
    order=4, out="05_advanced_control/books/BorrelliBemporadMorari_PredictiveControlLinearHybrid_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://cse.lab.imtlucca.it/~bemporad/publications/papers/BBMbook.pdf",
        "http://cse.lab.imtlucca.it/~bemporad/publications/papers/BBMbook.pdf",
    ]},
    expect={"title_words": ["Predictive", "Control", "Linear", "Hybrid"], "min_pages": 300},
))
g, r = reuse(f"{PS}/books/BoydVandenberghe_ConvexOptimization_2004_en.pdf",
             "https://web.stanford.edu/~boyd/cvxbook/")
books.append(item(
    id="CS05B05", cat="05", type="book", material="教材/参考书",
    title="Convex Optimization",
    authors="Stephen Boyd; Lieven Vandenberghe", school="Stanford / UCLA",
    year="2004", version="Cambridge 2004（作者公开 PDF）",
    level="研究生", prereq="线性代数、多元微积分",
    topics="凸集、凸函数、对偶、QP/SDP，MPC 与 LQR 计算基础",
    source="https://web.stanford.edu/~boyd/cvxbook/",
    license="作者公开 PDF",
    goal="最优控制/MPC 所需的凸优化语言",
    order=5, out="05_advanced_control/books/BoydVandenberghe_ConvexOptimization_2004_en.pdf",
    get=g, reuse=r,
    expect={"title_words": ["Convex", "Optimization"], "min_pages": 500},
    note="已有复用：probability_statistics_curriculum_literature",
))

# ---------- 06 learning ----------
g, r = reuse(f"{IPM}/books/Brunton_DataDrivenScienceEngineering_en.pdf", "http://databookuw.com/")
books.append(item(
    id="CS06B01", cat="06", type="book", material="教材/参考书", cross=["04"],
    title="Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control",
    authors="Steven L. Brunton; J. Nathan Kutz", school="University of Washington",
    year="2019", version="作者官网 PDF",
    level="本科高年级/研究生", prereq="线性代数、微分方程、基础控制",
    topics="SVD、DMD、SINDy、数据驱动控制",
    source="http://databookuw.com/",
    license="作者官网公开 PDF",
    goal="数据驱动动力学与控制的入门专著",
    order=1, out="06_learning_control/books/Brunton_DataDrivenScienceEngineering_en.pdf",
    get=g, reuse=r,
    expect={"title_words": ["Data-Driven", "Science", "Engineering"], "min_pages": 400},
    note="已有复用：industrial_process_monitoring_literature 14-007",
))

# ---------- 08 hardware book ----------
books.append(item(
    id="CS08B01", cat="08", type="book", material="教材/参考书",
    title="Embedded Controllers Using C and Arduino (2nd ed.)",
    authors="James M. Fiore", school="Mohawk Valley Community College",
    year="2018", version="2nd edition, Open Textbook",
    level="本科基础", prereq="C 语言入门、基本电路",
    topics="嵌入式 C、Arduino、定时器、中断、传感器接口",
    source="https://www.dissidents.com/resources/EmbeddedControllers.htm",
    license="CC BY-NC-SA",
    goal="控制工程师所需的嵌入式与传感器接口入门",
    order=1, out="08_hardware_realtime/books/Fiore_EmbeddedControllersUsingCArduino_2ndEd_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://www.dissidents.com/resources/EmbeddedControllers.pdf",
        "https://open.umn.edu/opentextbooks/formats/1121",
        "https://www.mvcc.edu/jfiore/embeddedcontrollers.pdf",
    ]},
    expect={"title_words": ["Embedded", "Controllers"], "min_pages": 100},
))

# ---------- courses ----------
g, r = reuse(f"{PS}/courses/MIT_1803_2010Spring_OCW_en.zip",
             "https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/")
courses.append(item(
    id="CS01C01", cat="01", type="course", material="OCW 官方课程包",
    title="18.03 Differential Equations (Spring 2010)",
    authors="Haynes Miller", school="MIT OpenCourseWare",
    year="2010", version="Spring 2010",
    level="本科基础", prereq="单变量微积分",
    topics="ODE、Laplace 变换、线性系统",
    source="https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="控制数学先修：微分方程与 Laplace",
    order=1, out="01_foundations/courses/MIT_1803_2010Spring_OCW_en.zip",
    get=g, reuse=r, note="已有复用：probability_statistics_curriculum_literature",
))
g, r = reuse(f"{AI}/courses/MIT_1806SC_2011Fall_OCWCoursePackage_en.zip",
             "https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/")
courses.append(item(
    id="CS01C02", cat="01", type="course", material="OCW 官方课程包",
    title="18.06SC Linear Algebra (Fall 2011)",
    authors="Gilbert Strang", school="MIT OpenCourseWare",
    year="2011", version="Fall 2011 Scholar 版",
    level="本科基础", prereq="多元微积分",
    topics="矩阵、子空间、最小二乘、特征值、SVD",
    source="https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="控制与估计所需线性代数完整课程",
    order=2, out="01_foundations/courses/MIT_1806SC_2011Fall_OCWCoursePackage_en.zip",
    get=g, reuse=r, note="已有复用：ai_undergraduate_graduate_curriculum_literature",
))
g, r = reuse(f"{AI}/courses/MIT_6003_2011Fall_OCWCoursePackage_en.zip",
             "https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/")
courses.append(item(
    id="CS01C03", cat="01", type="course", material="OCW 官方课程包",
    title="6.003 Signals and Systems (Fall 2011)",
    authors="Dennis Freeman", school="MIT OpenCourseWare",
    year="2011", version="Fall 2011",
    level="本科基础", prereq="微分方程、复变初步",
    topics="卷积、Fourier、Laplace、Z 变换、采样、反馈导引",
    source="https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="信号与系统完整课程，含 Z 变换与采样",
    order=3, out="01_foundations/courses/MIT_6003_2011Fall_OCWCoursePackage_en.zip",
    get=g, reuse=r, note="已有复用：ai_undergraduate_graduate_curriculum_literature",
))
courses.append(item(
    id="CS02C01", cat="02", type="course", material="OCW 官方课程包", cross=["09"],
    title="2.004 Dynamics and Control II (Spring 2008)",
    authors="Derek Rowell", school="MIT OpenCourseWare",
    year="2008", version="Spring 2008",
    level="本科", prereq="动力学、微分方程",
    topics="建模、传递函数、根轨迹、Bode、实验室电机控制",
    source="https://ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="经典控制本科课，含完整实验讲义",
    order=1, out="02_classical_control/courses/MIT_2004_2008Spring_OCWCoursePackage_en.zip",
    get={"kind": "file", "urls": [
        "https://ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/2.004-spring-2008.zip",
        "https://ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/resources/mit2_004s08_full.zip",
    ], "max_mb": 800},
    expect={"min_docs": 10, "link_check": False, "must_have": [r"2\.004|dynamics|control"]},
))
courses.append(item(
    id="CS02C02", cat="02", type="course", material="OCW 官方课程包", cross=["03", "09"],
    title="2.14 Analysis and Design of Feedback Control Systems (Spring 2014)",
    authors="David Trumper", school="MIT OpenCourseWare",
    year="2014", version="Spring 2014",
    level="本科进阶", prereq="动态系统、Laplace",
    topics="根轨迹、回路成形、PID、描述函数、状态空间、数字控制、伺服实验",
    source="https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="反馈设计完整课程（频率域+状态空间+数字+实验）",
    order=2, out="02_classical_control/courses/MIT_214_2014Spring_OCWCoursePackage_en.zip",
    get={"kind": "file", "urls": [
        "https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/2.14-spring-2014.zip",
    ], "max_mb": 800},
    expect={"min_docs": 10, "link_check": False},
))
g, r = reuse(f"{IPM}/university_materials/MIT_1630_2010Fall_OCWCoursePackage_en.zip",
             "https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/")
courses.append(item(
    id="CS02C03", cat="02", type="course", material="OCW 官方课程包", cross=["03"],
    title="16.30 Feedback Control Systems (Fall 2010)",
    authors="Jonathan P. How; Emilio Frazzoli", school="MIT OpenCourseWare",
    year="2010", version="Fall 2010",
    level="本科高年级", prereq="线性系统或飞行力学",
    topics="状态反馈、观测器、频率域、数字实现",
    source="https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="状态空间反馈与观测器设计课程",
    order=3, out="02_classical_control/courses/MIT_1630_2010Fall_OCWCoursePackage_en.zip",
    get=g, reuse=r, note="已有复用：industrial_process_monitoring_literature 13-014",
))
g, r = reuse(f"{IPM}/university_materials/MIT_6241J_2011Spring_OCWCoursePackage_en.zip",
             "https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/")
courses.append(item(
    id="CS03C01", cat="03", type="course", material="OCW 官方课程包",
    title="6.241J Dynamic Systems and Control (Spring 2011)",
    authors="Mohammed Dahleh; Munther A. Dahleh; George Verghese",
    school="MIT OpenCourseWare",
    year="2011", version="Spring 2011",
    level="研究生", prereq="线性代数、信号与系统",
    topics="线性动态系统、能控能观、鲁棒性、状态空间",
    source="https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="现代控制研究生核心课",
    order=1, out="03_modern_control/courses/MIT_6241J_2011Spring_OCWCoursePackage_en.zip",
    get=g, reuse=r, note="已有复用：industrial_process_monitoring_literature 13-008",
))
g, r = reuse(f"{IPM}/university_materials/Stanford_EE263_2026Summer_LectureSlides_en",
             "https://ee263.stanford.edu/lectures.html")
courses.append(item(
    id="CS03C02", cat="03", type="course", material="完整课件包",
    title="EE263 Introduction to Linear Dynamical Systems",
    authors="Stephen Boyd（课程页）", school="Stanford University",
    year="2026", version="Summer 2026 讲义全集",
    level="研究生", prereq="线性代数",
    topics="最小二乘、SVD、线性动态系统、MMSE",
    source="https://ee263.stanford.edu/lectures.html",
    license="课程官网公开讲义",
    goal="线性动态系统与最小二乘，衔接辨识与估计",
    order=2, out="03_modern_control/courses/Stanford_EE263_2026Summer_LectureSlides_en",
    get=g, reuse=r, note="已有复用：industrial_process_monitoring_literature 13-017",
))
g, r = reuse(f"{IPM}/university_materials/Stanford_EE363_2026Spring_LectureSlides_en",
             "https://ee363.stanford.edu/lectures.html")
courses.append(item(
    id="CS05C01", cat="05", type="course", material="完整课件包", cross=["03", "04"],
    title="EE363 Linear Dynamical Systems",
    authors="Stephen Boyd", school="Stanford University",
    year="2026", version="Spring 2026 全部讲次 PDF",
    level="研究生", prereq="EE263",
    topics="LQR、Kalman 滤波、能观性、线性二次估计",
    source="https://ee363.stanford.edu/lectures.html",
    license="课程官网公开讲义",
    goal="LQR 与 Kalman 滤波的标准研究生课件",
    order=1, out="05_advanced_control/courses/Stanford_EE363_2026Spring_LectureSlides_en",
    get=g, reuse=r, note="已有复用：industrial_process_monitoring_literature 13-018",
))
g, r = reuse(f"{IPM}/university_materials/MIT_6435_2005Spring_OCWCoursePackage_en.zip",
             "https://ocw.mit.edu/courses/6-435-system-identification-spring-2005/")
courses.append(item(
    id="CS04C01", cat="04", type="course", material="OCW 官方课程包",
    title="6.435 System Identification (Spring 2005)",
    authors="Munther A. Dahleh", school="MIT OpenCourseWare",
    year="2005", version="Spring 2005",
    level="研究生", prereq="线性系统、概率",
    topics="预测误差法、子空间辨识、实验设计",
    source="https://ocw.mit.edu/courses/6-435-system-identification-spring-2005/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="系统辨识完整课程",
    order=1, out="04_estimation_identification/courses/MIT_6435_2005Spring_OCWCoursePackage_en.zip",
    get=g, reuse=r, note="已有复用：industrial_process_monitoring_literature 13-005",
))
g, r = reuse(f"{IPM}/university_materials/UCCS_ECE5550_AppliedKalmanFiltering_LectureNotes_en",
             "http://mocha-java.uccs.edu/ECE5550/")
courses.append(item(
    id="CS04C02", cat="04", type="course", material="完整文字讲义",
    title="ECE5550 Applied Kalman Filtering",
    authors="Gregory L. Plett", school="University of Colorado Colorado Springs",
    year="2020", version="课程站点 Notes00–Notes0A",
    level="研究生", prereq="线性系统、概率",
    topics="Kalman、EKF、UKF、实现问题",
    source="http://mocha-java.uccs.edu/ECE5550/",
    license="课程官网公开讲义",
    goal="应用 Kalman 滤波完整讲义",
    order=2, out="04_estimation_identification/courses/UCCS_ECE5550_AppliedKalmanFiltering_LectureNotes_en",
    get=g, reuse=r, note="已有复用：industrial_process_monitoring_literature",
))
g, r = reuse(f"{AI}/courses/MIT_6231_2015Fall_OCWCoursePackage_en.zip",
             "https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/")
courses.append(item(
    id="CS05C02", cat="05", type="course", material="OCW 官方课程包",
    title="6.231 Dynamic Programming and Stochastic Control (Fall 2015)",
    authors="Dimitri Bertsekas", school="MIT OpenCourseWare",
    year="2015", version="Fall 2015",
    level="研究生", prereq="概率、高等微积分",
    topics="动态规划、随机控制、近似 DP",
    source="https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="最优控制/随机控制的动态规划课程",
    order=2, out="05_advanced_control/courses/MIT_6231_2015Fall_OCWCoursePackage_en.zip",
    get=g, reuse=r, note="已有复用：ai_undergraduate_graduate_curriculum_literature",
))
g, r = reuse(f"{IPM}/university_materials/BYU_ProcessDynamicsControl_Online_HTML_en.zip",
             "https://apmonitor.com/pdc/")
courses.append(item(
    id="CS07C01", cat="07", type="course", material="官方 HTML 离线包", cross=["02", "09"],
    title="Process Dynamics and Control (BYU / APMonitor)",
    authors="John Hedengren", school="Brigham Young University",
    year="2024", version="课程站点离线包（源库已核验）",
    level="本科/工程", prereq="微分方程、化工或机械过程基础",
    topics="FOPDT、PID、串级、前馈、状态空间、过程控制实验",
    source="https://apmonitor.com/pdc/",
    license="课程官网公开",
    goal="工业过程控制完整课程（建模到 PID 与实验）",
    order=1, out="07_industrial_automation/courses/BYU_ProcessDynamicsControl_Online_HTML_en.zip",
    get=g, reuse=r, note="已有复用：industrial_process_monitoring_literature",
))
g, r = reuse(f"{IPM}/university_materials/UCCS_ECE5560_SystemIdentification_LectureNotes_en",
             "http://mocha-java.uccs.edu/ECE5560/")
courses.append(item(
    id="CS04C03", cat="04", type="course", material="完整文字讲义",
    title="ECE5560 System Identification",
    authors="Gregory L. Plett", school="University of Colorado Colorado Springs",
    year="2020", version="课程站点全部 Notes",
    level="研究生", prereq="线性系统、最小二乘",
    topics="最小二乘、实验激励、参数估计、辨识实践",
    source="http://mocha-java.uccs.edu/ECE5560/",
    license="课程官网公开讲义",
    goal="系统辨识应用讲义，与 6.435 互补",
    order=3, out="04_estimation_identification/courses/UCCS_ECE5560_SystemIdentification_LectureNotes_en",
    get=g, reuse=r, note="已有复用：industrial_process_monitoring_literature",
))

# ---------- tools ----------
tools.append(item(
    id="CS09T01", cat="09", type="docs", material="官方 HTML 离线包", tool="MATLAB Control System Toolbox",
    title="Control System Toolbox — Getting Started (MathWorks 公开文档)",
    authors="MathWorks", school="MathWorks",
    year="2026", version="检索日公开 HTML（R2026 站点当前版）",
    level="本科/工程", prereq="传递函数基础",
    topics="tf/ss 对象、阶跃响应、Bode、PID 调参器入门",
    source="https://www.mathworks.com/help/control/",
    license="MathWorks 公开文档（软件本体不下载）",
    goal="官方 Control System Toolbox 入门文档离线包",
    order=1, out="09_simulation_practice/tools/MathWorks_ControlSystemToolbox_GettingStarted_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://www.mathworks.com/help/control/getting-started-with-control-system-toolbox.html",
        "https://www.mathworks.com/help/control/gs/control-system-toolbox.html",
        "https://www.mathworks.com/help/control/index.html",
    ], "domains": ["www.mathworks.com"], "include": ["/help/control"],
        "level": "2", "quota_mb": 80, "timeout": 1800, "wait": 0.4},
    expect={"min_docs": 5, "link_check": False, "entry": ""},
    complete="部分", scope="仅保存 Getting Started / 索引及一级链接，不含整站 Toolbox 参考",
    note="不下载 MATLAB/Simulink 软件本体",
))
tools.append(item(
    id="CS09T02", cat="09", type="docs", material="官方 HTML 离线包", tool="MATLAB System Identification Toolbox",
    title="System Identification Toolbox — Getting Started (MathWorks 公开文档)",
    authors="MathWorks", school="MathWorks",
    year="2026", version="检索日公开 HTML",
    level="本科高年级/工程", prereq="传递函数、最小二乘",
    topics="iddata、PEM、模型验证、系统辨识工作流",
    source="https://www.mathworks.com/help/ident/",
    license="MathWorks 公开文档",
    goal="官方 System Identification Toolbox 入门文档",
    order=2, out="09_simulation_practice/tools/MathWorks_SystemIdentificationToolbox_GettingStarted_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://www.mathworks.com/help/ident/getting-started-with-system-identification-toolbox.html",
        "https://www.mathworks.com/help/ident/index.html",
    ], "domains": ["www.mathworks.com"], "include": ["/help/ident"],
        "level": "2", "quota_mb": 80, "timeout": 1800, "wait": 0.4},
    expect={"min_docs": 5, "link_check": False},
    complete="部分", scope="仅保存 Getting Started / 索引及一级链接",
))
tools.append(item(
    id="CS09T03", cat="09", type="docs", material="官方 PDF", tool="GNU Octave",
    title="GNU Octave Manual (current stable PDF)",
    authors="John W. Eaton et al.", school="GNU Project",
    year="2025", version="docs.octave.org 当前 octave.pdf",
    level="本科", prereq="基础编程",
    topics="Octave 语言、绘图、求解器；配合 control 包做经典控制计算",
    source="https://docs.octave.org/octave.pdf",
    license="GFDL",
    goal="MATLAB 语法兼容的开源计算环境官方手册",
    order=3, out="09_simulation_practice/tools/GNUOctave_Manual_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://docs.octave.org/octave.pdf",
        "https://octave.org/doc/octave.pdf",
    ], "max_mb": 80},
    expect={"title_words": ["GNU", "Octave"], "min_pages": 200},
))
tools.append(item(
    id="CS09T04", cat="09", type="docs", material="官方 HTML 离线包", tool="python-control",
    title="Python Control Systems Library User Guide",
    authors="python-control developers (Murray et al.)", school="python-control.org",
    year="2025", version="readthedocs stable",
    level="本科/工程", prereq="Python、经典控制概念",
    topics="tf/ss、Bode/Nyquist、根轨迹、LQR、python-control 与 FBS 配套",
    source="https://python-control.readthedocs.io/en/stable/",
    license="BSD-3-Clause（库）；文档随仓库",
    goal="开源控制计算库完整用户指南",
    order=4, out="09_simulation_practice/tools/python_control_UserGuide_html_en.tar",
    get={"kind": "mirror", "start": "https://python-control.readthedocs.io/en/stable/",
         "domains": ["python-control.readthedocs.io"], "level": "3", "quota_mb": 80, "wait": 0.5},
    expect={"min_docs": 10, "link_check": False},
))
tools.append(item(
    id="CS09T05", cat="09", type="docs", material="官方 HTML 离线包", tool="SciPy.signal",
    title="SciPy Signal Processing Tutorial and API (signal)",
    authors="SciPy developers", school="NumFOCUS / SciPy",
    year="2025", version="docs.scipy.org 当前稳定版 signal 教程+API",
    level="本科/工程", prereq="Python、NumPy",
    topics="lti、bode、dlsim、滤波器、连续/离散系统",
    source="https://docs.scipy.org/doc/scipy/tutorial/signal.html",
    license="BSD",
    goal="SciPy.signal 中与控制相关的官方教程与参考",
    order=5, out="09_simulation_practice/tools/SciPy_signal_docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://docs.scipy.org/doc/scipy/tutorial/signal.html",
        "https://docs.scipy.org/doc/scipy/reference/signal.html",
    ], "domains": ["docs.scipy.org"], "include": ["/doc/scipy/tutorial", "/doc/scipy/reference"],
        "level": "2", "quota_mb": 60, "wait": 0.4},
    expect={"min_docs": 3, "link_check": False},
    complete="部分", scope="仅 signal 教程页与 signal 参考页及页面资源，不含全部 SciPy 文档",
))
tools.append(item(
    id="CS09T06", cat="09", type="docs", material="官方 PDF", tool="CasADi",
    title="CasADi User Guide (v3.7.2)",
    authors="Joel A. E. Andersson; Joris Gillis et al.", school="CasADi project",
    year="2025", version="3.7.2",
    level="研究生/工程", prereq="数值优化、Python 或 MATLAB",
    topics="符号框架、NLP、最优控制、积分器",
    source="https://web.casadi.org/docs/",
    license="LGPL（软件）；用户指南随发行包公开",
    goal="最优控制/MPC 实现的 CasADi 官方用户指南",
    order=6, out="09_simulation_practice/tools/CasADi_UserGuide_v3.7.2_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://github.com/casadi/casadi/releases/download/3.7.2/casadi-users_guide-v3.7.2.pdf",
        "https://web.casadi.org/casadi-users_guide.pdf",
        "https://sourceforge.net/projects/casadi.mirror/files/3.7.2/casadi-users_guide-v3.7.2.pdf/download",
    ]},
    expect={"title_words": ["CasADi"], "min_pages": 20},
))
tools.append(item(
    id="CS09T07", cat="09", type="docs", material="官方 HTML 离线包", tool="do-mpc",
    title="do-mpc Documentation",
    authors="do-mpc developers (Lucia group et al.)", school="TU Dortmund / do-mpc",
    year="2025", version="docs latest/develop 公开版",
    level="研究生/工程", prereq="MPC 概念、Python、CasADi",
    topics="MPC、MHE、仿真循环、约束",
    source="https://www.do-mpc.com/en/latest/",
    license="GNU LGPL（软件）；文档公开",
    goal="基于 CasADi 的 MPC 工具官方文档",
    order=7, out="09_simulation_practice/tools/do_mpc_Documentation_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://www.do-mpc.com/en/latest/",
        "https://www.do-mpc.com/en/stable/",
    ], "domains": ["www.do-mpc.com"], "level": "3", "quota_mb": 80, "wait": 0.4},
    expect={"min_docs": 8, "link_check": False},
))
tools.append(item(
    id="CS09T08", cat="09", type="docs", material="官方 PDF", tool="OpenModelica",
    title="OpenModelica User's Guide (latest)",
    authors="Open Source Modelica Consortium", school="OSMC",
    year="2026", version="OpenModelicaUsersGuide-latest（检索日）",
    level="本科高年级/工程", prereq="动态系统建模",
    topics="Modelica 建模、仿真、OMEdit、控制模型集成",
    source="https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/",
    license="OSMC / 公开用户指南",
    goal="OpenModelica 官方用户指南",
    order=8, out="09_simulation_practice/tools/OpenModelica_UsersGuide_latest_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/OpenModelicaUsersGuide-latest.pdf",
        "https://openmodelica.org/doc/OpenModelicaUsersGuide/OpenModelicaUsersGuide-latest.pdf",
    ], "max_mb": 80},
    expect={"title_words": ["OpenModelica"], "min_pages": 100},
))
tools.append(item(
    id="CS07T01", cat="07", type="docs", material="官方 HTML 离线包", tool="CODESYS",
    title="CODESYS Development System — First Steps / Getting Started",
    authors="CODESYS GmbH", school="CODESYS",
    year="2025", version="helpme-codesys.com 公开帮助（检索日）",
    level="工程", prereq="无（IEC 61131-3 入门）",
    topics="工程创建、POU、ST/LD、下载到控制器的入门流程",
    source="https://content.helpme-codesys.com/",
    license="CODESYS 公开在线帮助（软件本体不下载）",
    goal="CODESYS 官方入门帮助离线包",
    order=1, out="07_industrial_automation/tools/CODESYS_FirstSteps_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://content.helpme-codesys.com/en/CODESYS%20Development%20System/_cds_f_first_steps.html",
        "https://content.helpme-codesys.com/en/CODESYS%20Development%20System/_cds_start_page.html",
    ], "domains": ["content.helpme-codesys.com"], "level": "2", "quota_mb": 80, "wait": 0.4},
    expect={"min_docs": 5, "link_check": False},
    complete="部分", scope="First Steps / 起始页及一级链接，不含全部 CODESYS 帮助系统",
    note="不下载 CODESYS 安装包",
))
tools.append(item(
    id="CS07T02", cat="07", type="docs", material="厂商公开手册 PDF", tool="Siemens SIMATIC S7-1200",
    title="SIMATIC S7-1200 Easy Book",
    authors="Siemens AG", school="Siemens",
    year="2015", version="A5E02486774-AG, 01/2015",
    level="工程", prereq="无",
    topics="PLC 概念、STEP 7 入门、PID、运动控制、HMI/Web 服务器入门",
    source="https://support.industry.siemens.com/cs/document/39710145/simatic-s7-1200-easy-book",
    license="Siemens 公开下载手册（版权 Siemens）",
    goal="代表性 PLC 厂商公开入门手册",
    order=2, out="07_industrial_automation/tools/Siemens_S71200_EasyBook_2015_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://cache.industry.siemens.com/dl/files/145/39710145/att_5787/v1/s71200_easy_book_en-US_en-US.pdf",
    ], "max_mb": 80},
    expect={"title_words": ["S7-1200", "Easy", "Book"], "min_pages": 200, "allow_scan": True},
))
tools.append(item(
    id="CS07T03", cat="07", type="docs", material="官方协议规范 PDF", tool="Modbus",
    title="Modbus Application Protocol Specification V1.1b3",
    authors="Modbus Organization", school="Modbus Organization",
    year="2012", version="V1.1b3",
    level="工程", prereq="串行/TCP 基础",
    topics="Modbus PDU、功能码、异常响应",
    source="https://modbus.org/specs.php",
    license="Modbus Organization 公开规范",
    goal="工业通信最常用协议的官方公开规范",
    order=3, out="07_industrial_automation/tools/Modbus_ApplicationProtocol_V1_1b3_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf",
        "https://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf",
    ]},
    expect={"title_words": ["Modbus", "Application", "Protocol"], "min_pages": 20},
))
tools.append(item(
    id="CS07T04", cat="07", type="docs", material="官方 HTML 离线包", tool="open62541 / OPC UA",
    title="open62541 Documentation (OPC UA implementation guide)",
    authors="open62541 contributors", school="open62541 project",
    year="2025", version="1.4 文档站点",
    level="工程", prereq="C、TCP、工业通信概念",
    topics="OPC UA 对象模型、服务、安全、开源实现入门（非付费 IEC 62541 原文）",
    source="https://www.open62541.org/doc/1.4/",
    license="MPL-2.0（库）；文档公开",
    goal="OPC UA 公开实现文档与概念入门（不冒充付费标准原文）",
    order=4, out="07_industrial_automation/tools/open62541_OPC_UA_docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://www.open62541.org/doc/1.4/",
        "https://www.open62541.org/doc/master/toc.html",
    ], "domains": ["www.open62541.org"], "include": ["/doc"], "level": "3",
        "quota_mb": 80, "wait": 0.4},
    expect={"min_docs": 8, "link_check": False},
    note="IEC 62541 标准原文需付费，不以摘要冒充；本项为开源实现文档",
))
tools.append(item(
    id="CS09T09", cat="09", type="docs", material="官方 HTML 离线包", tool="GNU Octave control 包",
    title="Octave Forge control package documentation",
    authors="Octave Forge / Lukas Reichlin et al.", school="GNU Octave",
    year="2024", version="control 包当前文档",
    level="本科/工程", prereq="Octave 基础",
    topics="tf、ss、bode、rlocus、lqr 等 Control 工具箱兼容函数",
    source="https://gnu-octave.github.io/packages/control/",
    license="GPL",
    goal="Octave control 包官方函数文档",
    order=9, out="09_simulation_practice/tools/OctaveForge_control_package_docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://gnu-octave.github.io/packages/control/",
        "https://octave.sourceforge.io/control/overview.html",
        "https://octave.sourceforge.io/control/package_doc/index.html",
    ], "domains": ["gnu-octave.github.io", "octave.sourceforge.io"], "span": True,
        "level": "2", "quota_mb": 40, "wait": 0.4},
    expect={"min_docs": 3, "link_check": False},
    complete="部分", scope="control 包概览与函数文档页",
))
tools.append(item(
    id="CS09T10", cat="09", type="docs", material="官方 HTML 离线包", tool="Scilab/Xcos",
    title="Scilab Help — Control Systems and Xcos",
    authors="ESI Group / Scilab team", school="Scilab",
    year="2025", version="help.scilab.org 当前版 control_systems + xcos",
    level="本科/工程", prereq="基础编程",
    topics="Scilab 控制系统函数、Xcos 框图仿真",
    source="https://help.scilab.org/",
    license="公开帮助文档",
    goal="Scilab/Xcos 控制与仿真官方帮助",
    order=10, out="09_simulation_practice/tools/Scilab_Xcos_control_help_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://help.scilab.org/control_systems.html",
        "https://help.scilab.org/xcos.html",
        "https://help.scilab.org/section_cacsd.html",
    ], "domains": ["help.scilab.org"], "level": "2", "quota_mb": 60, "wait": 0.4},
    expect={"min_docs": 5, "link_check": False},
    complete="部分", scope="控制系统与 Xcos 相关帮助页及一级链接，不含全部 Scilab 帮助",
))

# ---------- practice ----------
practice.append(item(
    id="CS09X01", cat="09", type="practice", material="大学公开实验教程 HTML",
    title="Control Tutorials for MATLAB and Simulink (CTMS)",
    authors="Bill Messner; Dawn Tilbury; et al.",
    school="University of Michigan / Carnegie Mellon",
    year="2024", version="ctms.engin.umich.edu 当前站点",
    level="本科", prereq="经典控制概念、MATLAB 或 Octave",
    topics="建模、PID、根轨迹、频率、状态空间、数字控制；巡航/电机/悬架等案例",
    source="https://ctms.engin.umich.edu/CTMS/",
    license="CC BY-SA（站点声明）",
    goal="按对象走完建模-分析-PID-根轨迹-频率-状态空间-数字控制的实验教程",
    order=1, out="09_simulation_practice/practice/Michigan_CTMS_html_en.tar",
    get={"kind": "mirror", "start": "https://ctms.engin.umich.edu/CTMS/",
         "domains": ["ctms.engin.umich.edu"], "level": "4", "quota_mb": 150, "wait": 0.3},
    expect={"min_docs": 20, "link_check": False},
))
practice.append(item(
    id="CS09X02", cat="09", type="practice", material="官方示例源码归档",
    title="python-control examples (official repository examples/)",
    authors="python-control developers", school="python-control",
    year="2025", version="官方仓库 examples 目录（depth-1）",
    level="本科/研究生", prereq="Python、python-control 文档",
    topics="Bode/Nyquist、LQR、MPC 笔记本、MRAC、巡航控制、CDS110/112 练习",
    source="https://github.com/python-control/python-control",
    license="BSD-3-Clause",
    goal="官方示例（含 FBS/OBC 配套笔记本）",
    order=2, out="09_simulation_practice/practice/python_control_examples_en.tar",
    get={"kind": "git", "repo": "https://github.com/python-control/python-control.git",
         "paths": ["examples", "README.md", "LICENSE"]},
    expect={"min_docs": 5, "need_license": True, "must_have": ["examples/"]},
))
practice.append(item(
    id="CS09X03", cat="09", type="practice", material="官方示例包",
    title="CasADi example pack v3.7.2",
    authors="CasADi project", school="CasADi",
    year="2025", version="3.7.2 example pack",
    level="研究生/工程", prereq="CasADi 用户指南",
    topics="最优控制、积分器、NLP 示例（不含 CasADi 软件本体）",
    source="https://github.com/casadi/casadi/releases/tag/3.7.2",
    license="LGPL",
    goal="CasADi 官方示例包",
    order=3, out="09_simulation_practice/practice/CasADi_example_pack_v3.7.2_en.zip",
    get={"kind": "file", "urls": [
        "https://github.com/casadi/casadi/releases/download/3.7.2/casadi-example_pack-v3.7.2.zip",
    ], "max_mb": 50},
    expect={"min_docs": 5, "link_check": False},
))
practice.append(item(
    id="CS09X04", cat="09", type="practice", material="官方示例源码归档",
    title="do-mpc examples",
    authors="do-mpc developers", school="do-mpc",
    year="2025", version="官方仓库 examples 目录",
    level="研究生/工程", prereq="do-mpc 文档、CasADi",
    topics="CSTR、批处理、振荡器等 MPC/MHE 示例",
    source="https://github.com/do-mpc/do-mpc",
    license="LGPL",
    goal="do-mpc 官方示例",
    order=4, out="09_simulation_practice/practice/do_mpc_examples_en.tar",
    get={"kind": "git", "repo": "https://github.com/do-mpc/do-mpc.git",
         "paths": ["examples", "README.md", "LICENSE"]},
    expect={"min_docs": 3, "need_license": True, "must_have": ["examples/"]},
))
practice.append(item(
    id="CS09X05", cat="09", type="practice", material="公开实验 HTML", cross=["07"],
    title="APMonitor Process Dynamics and Control — Temperature Control Lab and modules",
    authors="John Hedengren", school="Brigham Young University / APMonitor",
    year="2024", version="apmonitor.com/pdc 实验与模块页",
    level="本科/工程", prereq="ODE、PID 概念",
    topics="温度控制实验、FOPDT 辨识、PID、GEKKO 仿真",
    source="https://apmonitor.com/pdc/",
    license="课程官网公开",
    goal="可离线阅读的过程控制实验与仿真模块（不含 BYU 整课重复计数的完整课程包）",
    order=5, out="09_simulation_practice/practice/APMonitor_PDC_labs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://apmonitor.com/pdc/index.php/Main/ArduinoTemperatureControl",
        "https://apmonitor.com/pdc/index.php/Main/HomePage",
        "https://apmonitor.com/pdc/index.php/Main/TCLab",
    ], "domains": ["apmonitor.com"], "include": ["/pdc"], "level": "3",
        "quota_mb": 120, "wait": 0.3},
    expect={"min_docs": 10, "link_check": False},
    complete="部分", scope="PDC 课程实验与模块 HTML，不含视频",
    note="与 CS07C01 BYU 整课包互补：本项只计实验/案例，课程计在 CS07C01",
))
practice.append(item(
    id="CS02X01", cat="02", type="practice", material="工业 PID 案例教程 HTML", cross=["07", "09"],
    title="Control Guru — Practical Process Control",
    authors="Douglas J. Cooper / Control Station",
    school="Control Guru",
    year="2024", version="controlguru.com 公开教程",
    level="工程", prereq="一阶过程、PID 概念",
    topics="FOPDT、PID 整定、振荡诊断、工业回路实践",
    source="https://controlguru.com/",
    license="站点公开教程（版权 Control Station）",
    goal="工业 PID 整定与回路诊断的实践案例集",
    order=1, out="02_classical_control/practice/ControlGuru_PracticalProcessControl_html_en.tar",
    get={"kind": "mirror", "start": "https://controlguru.com/",
         "domains": ["controlguru.com", "www.controlguru.com"], "span": True,
         "level": "2", "quota_mb": 80, "wait": 0.4},
    expect={"min_docs": 10, "link_check": False},
    complete="部分", scope="公开 HTML 教程页，不含专有 Loop-Pro 软件",
))
practice.append(item(
    id="CS09X06", cat="09", type="practice", material="教材配套练习站点 HTML",
    title="Feedback Systems additional resources (fbswiki OBC / python-control exercises)",
    authors="Karl Johan Åström; Richard M. Murray",
    school="Caltech / Lund",
    year="2024", version="fbswiki.org 公开页",
    level="本科进阶", prereq="Feedback Systems 教材",
    topics="python-control 练习、OBC 补充、章节资源",
    source="https://fbswiki.org/",
    license="教材配套公开 wiki",
    goal="Åström–Murray 教材的配套练习与计算资源",
    order=6, out="09_simulation_practice/practice/FBS_wiki_resources_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://fbswiki.org/",
        "https://fbswiki.org/wiki/index.php/Main_Page",
        "https://fbswiki.org/wiki/index.php/OBC",
    ], "domains": ["fbswiki.org", "www.cds.caltech.edu"], "span": True,
        "level": "2", "quota_mb": 80, "wait": 0.4},
    expect={"min_docs": 5, "link_check": False},
    complete="部分", scope="wiki 主页面与 OBC/资源页及一级链接",
))
practice.append(item(
    id="CS09X07", cat="09", type="practice", material="官方示例源码归档",
    title="GEKKO examples (process control / MPC Python)",
    authors="BYU PRISM / John Hedengren", school="Brigham Young University",
    year="2025", version="GEKKO 仓库 examples 目录",
    level="本科高年级/工程", prereq="Python、ODE",
    topics="动态优化、MPC、估计、过程控制示例",
    source="https://github.com/BYU-PRISM/GEKKO",
    license="MIT",
    goal="过程控制与动态优化的 Python 实践示例",
    order=7, out="09_simulation_practice/practice/GEKKO_examples_en.tar",
    get={"kind": "git", "repo": "https://github.com/BYU-PRISM/GEKKO.git",
         "paths": ["examples", "README.md", "LICENSE"]},
    expect={"min_docs": 3, "need_license": True},
))
practice.append(item(
    id="CS08X01", cat="08", type="practice", material="官方文档示例 HTML",
    title="FreeRTOS Kernel Documentation (real-time scheduling primer)",
    authors="Amazon Web Services / FreeRTOS",
    school="FreeRTOS",
    year="2025", version="freertos.org 公开文档",
    level="工程", prereq="C、嵌入式基础",
    topics="任务、队列、中断、实时调度，控制回路部署基础",
    source="https://www.freertos.org/Documentation/02-Kernel/02-Kernel-features/01-Tasks-and-co-routines/00-Task-states",
    license="MIT（内核）；文档公开",
    goal="实时内核官方文档，服务控制回路的嵌入式部署（不装软件）",
    order=1, out="08_hardware_realtime/practice/FreeRTOS_kernel_docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://www.freertos.org/Documentation/02-Kernel/01-About-the-FreeRTOS-kernel/01-RTOS-fundamentals",
        "https://www.freertos.org/Documentation/02-Kernel/02-Kernel-features/01-Tasks-and-co-routines/01-Task-states",
    ], "domains": ["www.freertos.org"], "include": ["/Documentation"], "level": "3",
        "quota_mb": 80, "wait": 0.4},
    expect={"min_docs": 8, "link_check": False},
    complete="部分", scope="Kernel 基础与任务特性文档，不含全部端口与演示工程二进制",
))
practice.append(item(
    id="CS07X01", cat="07", type="practice", material="官方示例/入门 HTML",
    title="open62541 Tutorial pages (OPC UA server/client walkthrough)",
    authors="open62541 contributors", school="open62541",
    year="2025", version="1.4 文档 tutorials",
    level="工程", prereq="C、OPC UA 概念",
    topics="创建 Server/Client、读写节点、订阅",
    source="https://www.open62541.org/doc/1.4/tutorial.html",
    license="MPL-2.0",
    goal="OPC UA 开源实现的官方教程页（实践向）",
    order=2, out="07_industrial_automation/practice/open62541_tutorials_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://www.open62541.org/doc/1.4/tutorial.html",
        "https://www.open62541.org/doc/1.4/tutorial_server_firststeps.html",
        "https://www.open62541.org/doc/1.4/tutorial_client_firststeps.html",
    ], "domains": ["www.open62541.org"], "include": ["/doc/1.4"], "level": "2",
        "quota_mb": 40, "wait": 0.4},
    expect={"min_docs": 3, "link_check": False},
    complete="部分", scope="tutorial*.html 及相关页面资源",
    note="与 CS07T04 文档包互补：本项只计教程页实践路径",
))
practice.append(item(
    id="CS09X08", cat="09", type="practice", material="官方示例源码归档",
    title="python-control documentation notebooks packaged with examples (already in CS09X02 if present); SciPy cookbook signal-control scripts via scipy-lectures subset",
    authors="Scientific Python Lectures",
    school="scipy-lectures",
    year="2025", version="scientific-python-lectures 仓库 signal 相关讲义",
    level="本科", prereq="Python、NumPy",
    topics="信号处理与 LTI 系统数值实验",
    source="https://github.com/scipy-lectures/scientific-python-lectures",
    license="CC BY",
    goal="用 SciPy 做 LTI/滤波数值实验的公开讲义",
    order=8, out="09_simulation_practice/practice/ScientificPythonLectures_signal_en.tar",
    get={"kind": "git", "repo": "https://github.com/scipy-lectures/scientific-python-lectures.git",
         "paths": ["intro/scipy", "advanced/image_processing", "README.rst", "LICENSE.txt", "LICENSE"]},
    expect={"min_docs": 3, "need_license": False},
))
practice.append(item(
    id="CS07X02", cat="07", type="practice", material="官方规范 PDF",
    title="Modbus Messaging Implementation Guide V1.0b (TCP/IP)",
    authors="Modbus Organization", school="Modbus Organization",
    year="2006", version="V1.0b",
    level="工程", prereq="Modbus 应用层规范",
    topics="Modbus TCP 实现、MBAP 头、客户端/服务器",
    source="https://modbus.org/specs.php",
    license="Modbus Organization 公开规范",
    goal="工业以太网 Modbus TCP 实现指南（实践向规范）",
    order=3, out="07_industrial_automation/practice/Modbus_MessagingImplementationGuide_V1_0b_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://modbus.org/docs/Modbus_Messaging_Implementation_Guide_V1_0b.pdf",
    ]},
    expect={"title_words": ["Modbus", "Messaging"], "min_pages": 20},
))

all_items = books + courses + tools + practice
ids = [x["id"] for x in all_items]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]

SEEDS.mkdir(parents=True, exist_ok=True)
(SEEDS / "B_books_en.json").write_text(json.dumps(books, ensure_ascii=False, indent=1), encoding="utf-8")
(SEEDS / "C_courses_en.json").write_text(json.dumps(courses, ensure_ascii=False, indent=1), encoding="utf-8")
(SEEDS / "T_tools_en.json").write_text(json.dumps(tools, ensure_ascii=False, indent=1), encoding="utf-8")
(SEEDS / "X_practice_en.json").write_text(json.dumps(practice, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"books {len(books)} courses {len(courses)} tools {len(tools)} practice {len(practice)}")
