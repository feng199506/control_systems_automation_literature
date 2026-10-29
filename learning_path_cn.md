# 学习顺序：基础 → 理论 → 工业应用 → 实践

按一条主线读，不必每个子目录并行铺开。论文放在对应阶段之后作扩展，不要用近三年 AI 控制论文代替 PID、状态空间、辨识和 PLC。

先修默认：单变量微积分。有电路基础则硬件段更顺。

---

## 第一段 基础（约 01）

**目标**：能写线性 ODE、做 Laplace/Z 变换、用矩阵描述动态系统、分清连续/离散信号。

1. 教材：Trench 微分方程（含 Laplace）→ Hefferon 线性代数 → Boyd–Vandenberghe *VMLS*（接到最小二乘）。
2. 课程：MIT 18.03 → MIT 18.06SC → MIT 6.003。
3. 信号与采样：Lee–Varaiya *SISS*；需要数字滤波直觉时读 Smith DSP（分章 PDF，整本计一次）。
4. 工具预备：GNU Octave 手册 + SciPy.signal 离线文档（本段只读，不装软件）。

**出口**：能把一个二阶系统写成 ODE、传递函数和状态方程三种形式。

---

## 第二段 经典控制（02）

**目标**：反馈、稳定性、根轨迹、Bode/Nyquist、PID 设计与调参。

1. 主教材：Åström–Murray *Feedback Systems*（第 2 版公开稿）。
2. 课程：MIT 2.004（动力学与控制）→ MIT 2.14 或 MIT 16.30（反馈设计）。
3. 硬件直觉：Roberge 运放与反馈（模拟回路、补偿）。
4. 实践：Control Guru 工业 PID 案例（部分 HTML）。
5. 扩展：Doyle–Francis–Tannenbaum *Feedback Control Theory*（频率域鲁棒入门，可放到第五段再精读）。
6. 近三年论文：PID anti-windup 与调参综述（`02_classical_control/papers/`）。

**出口**：能对 FOPDT/二阶对象画 Bode、选 PID、解释增益裕度与积分饱和。

---

## 第三段 现代控制与数字实现（03）

**目标**：能控能观、状态反馈、观测器、离散与采样控制。

1. 课程：MIT 6.241J *Dynamic Systems and Control*；Stanford EE263（线性动态系统）。
2. 教材：Sontag *Mathematical Control Theory*（研究生严格版，按章节选读能控/能观/镇定）。
3. 与第二段衔接：*Feedback Systems* 中的状态空间与观测器章节。
4. 近三年论文：多面体不变集、离散/跳变系统滤波等（`03_modern_control/papers/`）。

**出口**：能判断能控能观、设计极点配置与全维观测器，并说明采样周期对离散模型的影响。

---

## 第四段 估计与系统辨识（04）

**目标**：从数据得到模型，从噪声测量得到状态。

1. 辨识课程：MIT 6.435；UCCS ECE5560。
2. 辨识教材：Pillonetto 等 *Regularized System Identification*（PEM → 正则化/核方法）。
3. 状态估计课程：UCCS ECE5550；教材 Särkkä–Svensson *Bayesian Filtering and Smoothing*。
4. 工具文档：SciPy.signal（LTI/离散仿真）；System Identification Toolbox 官方 PDF 未能保存，改用 python-control / GEKKO 示例理解工作流。
5. 近三年论文：控制导向辨识综述、Kalman/UKF 教程与应用（`04_estimation_identification/papers/`）。

**出口**：能做一次开环/闭环辨识思路（激励、PEM 或正则化、验证），并能写 Kalman 预测—更新。

---

## 第五段 进阶理论（05，可与第四段部分并行）

**目标**：LQR/LQG、MPC、鲁棒与自适应、非线性 Lyapunov。

1. 最优控制：Liberzon 变分/PMP 讲义 → Boyd–Vandenberghe *Convex Optimization*（计算语言）→ Murray *Optimization-Based Control*。
2. MPC：Rawlings–Mayne–Diehl；互补读 Borrelli–Bemporad–Morari（显式/混杂）。
3. 课程：Stanford EE363；MIT 6.231（动态规划，随机控制）。
4. 鲁棒：回到 Doyle FCT；近三年鲁棒/安全 MPC 与 CBF 综述。
5. 非线性/Lyapunov：Sontag 相关章 + 近三年 backstepping 综述与 Lyapunov 证书论文。
6. 工具：CasADi 用户指南、do-mpc 文档（部分离线包）。

**出口**：能陈述 LQR 与约束 MPC 的差别，并说明稳定性/递归可行的基本条件。

---

## 第六段 学习与数据驱动控制（06）

**目标**：在已有稳定性语言上读数据驱动与 RL 控制，而不是反过来。

1. 教材：Brunton–Kutz *Data-Driven Science and Engineering*（SVD/DMD/SINDy）。
2. 经典论文（单列）：De Persis–Tesi 数据驱动公式；Coulson DeePC；Berberich 等数据驱动 MPC；Recht RL-from-control 教程；Wabersich 等学习控制安全认证。
3. 近三年论文：直接/间接数据驱动、带通信约束的网络系统、有限样本保证（`06_learning_control/papers/`）。
4. 实践：python-control 示例中的数据驱动/MRAC 笔记本；do-mpc / CasADi 示例。

**出口**：能区分直接数据驱动、辨识+控制、RL，并能指出安全约束是加在哪一层。

---

## 第七段 工业应用（07–08）

**目标**：顺序逻辑、联锁、PLC/HMI 概念、工业通信；再看嵌入式实时。

1. PLC 教材：Hugh Jack *Automating Manufacturing Systems with PLCs*（梯形图、IEC 61131、接线、联锁）。
2. 厂商公开手册：Siemens S7-1200 Easy Book；CODESYS First Steps（部分 HTML）。
3. 过程控制课程：BYU / APMonitor *Process Dynamics and Control*。
4. 通信：Modbus 应用层规范 + Modbus TCP 实现指南；OPC UA 用 open62541 文档源与 examples（**不是** IEC 62541 付费原文）。
5. 硬件：Fiore *Embedded Controllers Using C and Arduino*；Barry *Mastering the FreeRTOS Real Time Kernel*。
6. 近三年论文：PLC 程序生成/评测、工控安全审计（`07_industrial_automation/papers/`），作为工程阅读而非替代 PLC 基础。

**出口**：能读懂一个简单联锁梯形逻辑，并说明 Modbus 功能码与 OPC UA 地址空间的差别。

---

## 第八段 实践（09，贯穿但最后集中做）

本轮**不运行代码、不安装软件、不接设备**。只按 `practice_index_cn.md` 把案例与工具文档对应起来，下一阶段再上机。

建议顺序：

1. python-control 用户指南 + examples（经典/状态空间/LQR）。
2. Control Guru（工业 PID）+ APMonitor TCLab 模块页 + TCLab 软件包示例。
3. GEKKO 示例（过程动态、MPC）。
4. CasADi 示例包 → do-mpc examples。
5. OpenModelica 用户指南（建模，不装软件）。
6. Octave control 包文档 / Scilab-Xcos 帮助（MATLAB 语法替代）。
7. open62541 examples 与 Modbus 规范（通信实现阅读）。
8. FreeRTOS 教程（把控制回路放到实时任务里的概念）。

---

## 不建议的跳读

- 不要先堆强化学习论文再补 PID。
- 不要用 Toolbox 截图教程代替传递函数与状态空间教材。
- 不要把付费标准摘要当成已收藏的 IEC 62541。
