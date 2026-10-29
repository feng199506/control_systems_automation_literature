# 检索与来源日志

检索日：2026-10-30。论文窗口：2023-10-30–2026-10-30。  
类别：自动控制与工业自动化。不进入机器人/无人机。

## 已有资料库复用（先核验，再复制，不移动）

从下列目录核验后复制控制相关全文：

- `industrial_process_monitoring_literature`：Åström FBS、Doyle FCT、Särkkä、Pillonetto、Rawlings MPC、Brunton
- `probability_statistics_curriculum_literature`：Boyd VMLS、Boyd Convex Optimization、MIT 18.03
- `ai_undergraduate_graduate_curriculum_literature`：Liberzon 最优控制讲义、MIT 18.06SC 等

复用标记写在 `catalog_cn.csv` 的「来源方式」列。原文件保留。

## 教材与课程来源

| 检索 | 采用 | 备注 |
|---|---|---|
| Trinity Digital Commons Trench ODE | 采用，Chrome UA 后 200 | 作者 CC 教材 |
| Hefferon linearalgebra book.pdf | 采用 | GFDL |
| Ptolemy/Lee–Varaiya SISS | 采用 | 作者站点公开 PDF |
| dspguide.com 整本 pdfbook.pdf | 404 | 改为 CH1–CH33 分章 PDF，整本计一次 |
| Analog Devices DSP 封面页 | 长时间无响应 | 去掉，33 章已覆盖全书正文 |
| MIT OCW 2.004 / 2.14 zip | 采用 | 2.004 去掉过严的 must_have 后成员名核验通过 |
| MIT OCW Roberge 运放 | 采用 ans7870 合并章节 PDF | 课程资源页 404 |
| Sontag MCT 作者站点 | 采用 | Springer 版权、作者获准公开 |
| Murray OBC complete PDF | 采用 cds.caltech.edu | |
| Bemporad BBM MPC PDF | 采用实验室公开 PDF | |
| Hugh Jack PLC | Internet Archive Open Textbook Library `plcbook5_1.pdf` | 作者 GFDL；engineeronadisk HTML 未整站镜像 |
| Fiore Embedded Controllers | MVCC `/Micro/` PDF | dissidents.com 证书过期；已加 SSL 回退 |
| Goodwin CSD 全本 | 无合法全文 | 不收录 |
| Kalman 1960 ASME | 付费 | 不收录；用 Särkkä + 近三年 Kalman 教程 |

大学课程以 MIT OCW 官方 zip、Stanford EE263/EE363 讲义、UCCS ECE5550/5560 讲义、BYU APMonitor PDC 为主，完整课程计一套。

## 论文

- 主检索：arXiv `eess.SY` / `math.OC` / `cs.SY`，查询 PID、system identification、Kalman、MPC、robust/adaptive/Lyapunov、data-driven control、PLC/ICS。
- 近三年 43 篇，经典 7 篇单独标注 `classic_reason`。
- 替换弱相关误匹配（仍保留磁盘上的旧文件，不计入目录）：
  - `1910.06691` 断裂力学 → `1906.10417` Wabersich 等 PMPSC（学习控制安全）
  - `2211.12016` 因果识别 → `1903.06842` De Persis–Tesi 数据驱动公式
- 不把强化学习作为主体；Recht 2018 仅作控制视角教程。

## 工具文档

| 工具 | 结果 |
|---|---|
| MATLAB Control System Toolbox / System Identification Toolbox HTML | wget rc=8 空包 |
| 同上 `help/pdf_doc/*.pdf` | HTTP 403 |
| GNU Octave `octave.pdf` | 成功 |
| python-control ReadTheDocs | 成功（wget 在已超 min_docs 后打包） |
| SciPy.signal | 成功（部分：教程+参考及相关页） |
| CasADi 3.7.2 User Guide + example pack | 成功 |
| do-mpc HTML | 成功（配额截断，部分） |
| OpenModelica UsersGuide-latest.pdf | 成功 |
| Octave Forge control | 成功（部分） |
| Scilab/Xcos help | 成功（配额截断，部分） |
| CODESYS First Steps | 成功（部分 HTML） |
| Siemens S7-1200 Easy Book | 成功（cache.industry.siemens.com） |
| Modbus `/docs/*.pdf` | 404；改 `modbus.org/file/secure/modbusprotocolspecification.pdf` 与 `messagingimplementationguide.pdf` |
| open62541 HTML `/doc/1.4/` | 几乎空；改官方仓库 `doc/` RST 源 |
| IEC 62541 | 付费，不下载、不以摘要冒充 |

## 实践案例

| 来源 | 结果 |
|---|---|
| python-control / do-mpc / GEKKO / scipy-lectures git | 成功 |
| CasADi example pack zip | 成功（min_docs 改为 1，包内多为 `.m`） |
| APMonitor PDC / TCLab HTML | 成功（部分） |
| Control Guru | 成功（部分） |
| TCLab GitHub | 成功 |
| FreeRTOS HTML 文档 | 空/404；改官方教程 PDF *Mastering the FreeRTOS Real Time Kernel* |
| 密歇根 CTMS | wget 空包，urllib 403，archive.org 429；**缺口** |
| fbswiki.org | 仅 1 个文档文件；**缺口**（有 FBS 教材与 python-control 练习替代） |
| open62541 tutorial HTML | 空包；用 examples git 替代 |

## 技术处理（下载核验，非内容改写）

- HTTP：Chrome UA；证书失败时对 SSL `URLError` 走未校验 TLS（仅用于作者过期证书的 OA PDF）。
- 分章教材：任选章节失败不再整本作废，达到 `min_files` 即通过。
- HTML：配额截断且 `min_docs` 已满足时记为部分资料，不记失败。
- 不扫描整库 SHA256，不把试读/摘要计为完整资料。
