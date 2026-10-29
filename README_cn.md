# 自动控制与工业自动化资料库

检索日：**2026-10-30**（论文时间窗口 2023-10-30 至 2026-10-30）。  
根目录：`/root/control_systems_automation_literature/`。  
本轮只收集本类别，不进入机器人或无人机。

## 核验后数量（整库合计，不是每个子目录）

| 类型 | 已核验 | 目标 | 状态 |
|---|---:|---|---|
| 完整教材 / 参考书 / 专著 | 19 | 15–25 | 达到 |
| 大学完整课程或讲义 | 14 | 10–15 | 达到 |
| 研究论文、综述及学术教程 | 50（近三年 43，占 86.0%；经典 7） | 约 50，近三年 ≥85% | 达到 |
| 官方工具文档或完整教程 | 12（完整 7，部分离线包 5） | 8–12 | 达到 |
| 公开实验及实践案例 | 11（完整 9，部分 2） | 10–15 | 达到 |

已有复用 21 份（只复制、不移动原库），新下载 85 份。失败 5 项，见 `download_failures_cn.csv`。已核验体积约 1.14 GB。

## 子目录

| 目录 | 内容 |
|---|---|
| `01_foundations/` | 微分方程、线性代数、Laplace/Z、信号与系统、数值与 DSP |
| `02_classical_control/` | 传递函数、反馈、稳定性、根轨迹、频率响应、PID |
| `03_modern_control/` | 状态空间、能控能观、状态反馈、观测器、离散控制 |
| `04_estimation_identification/` | 最小二乘、系统辨识、Kalman 与状态估计 |
| `05_advanced_control/` | 最优控制、LQR/LQG、MPC、鲁棒、自适应、非线性与 Lyapunov |
| `06_learning_control/` | 数据驱动、学习辅助、强化学习控制、安全约束 |
| `07_industrial_automation/` | PLC、顺序与逻辑、联锁、工业通信、OPC UA 开源实现 |
| `08_hardware_realtime/` | 嵌入式 C、传感器接口、实时内核 |
| `09_simulation_practice/` | 建模仿真工具文档与实验案例 |

每个子目录下按 `books/` `courses/` `papers/` `tools/` `practice/` 存放。文件在扩展名前有语言后缀 `_en`。

## 登记文件

- `catalog_cn.csv` — 每一份已核验资料的标题、作者、机构、类型、年份、版本、语言、层次、先修、主题、来源、本地路径、完整性
- `progress_cn.csv` — 按整库与子目录汇总
- `download_failures_cn.csv` — 失败项与原因
- `search_log_cn.md` — 检索与来源决策
- `learning_path_cn.md` — 基础 → 理论 → 工业应用 → 实践
- `practice_index_cn.md` — 实验与案例索引（本轮不运行代码、不装软件）

## 覆盖要点

- **经典控制**：Åström–Murray *Feedback Systems*、Doyle–Francis–Tannenbaum、MIT 2.004 / 2.14 / 16.30、PID 近三年综述
- **现代控制**：Sontag *Mathematical Control Theory*、MIT 6.241J、Stanford EE263
- **辨识与估计**：Pillonetto 等 OA 教材、Särkkä 滤波、MIT 6.435、UCCS ECE5550/5560
- **PLC 工程**：Hugh Jack 开放教材、Siemens S7-1200 Easy Book、CODESYS 入门帮助、Modbus 官方规范
- **工具**：GNU Octave、python-control、SciPy.signal、CasADi、do-mpc、OpenModelica、Octave Forge control、Scilab/Xcos、open62541（OPC UA 实现文档，**不是**付费 IEC 62541 原文）

## 缺口（未计入数量）

1. **MATLAB/Simulink Control System Toolbox 与 System Identification Toolbox** 官方 HTML 与 `pdf_doc` 均返回 403，未保存。用 python-control、Octave control、SciPy.signal 与 APMonitor/GEKKO 案例覆盖同类工作流。
2. **密歇根 CTMS**（Control Tutorials for MATLAB and Simulink）站点 403/空镜像，未计入。PID/根轨迹练习改走 python-control examples 与 Control Guru。
3. **fbswiki.org** 与 **open62541 HTML 教程页** wget 不完整；已用 OBC 教材、python-control 示例、open62541 `doc/` 源码与 `examples/` 替代，不重复计数失败项。
4. 无独立 DCS/SCADA 厂商完整手册（公开入口不足）；HMI/联锁在 Jack PLC 教材与 Siemens Easy Book 中有章节级覆盖。
5. 无单独的传感器/执行器/伺服专著；硬件侧为 Fiore 嵌入式教材 + FreeRTOS 教程。

## 规则摘要

只保存合法公开全文。不下载商业软件本体、破解或付费手册。复用时复制并标注，不移动原文件。本轮不运行代码、不安装软件、不操作工业设备、不上传 GitHub。
