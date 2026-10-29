# 实验与实践案例索引

本轮只下载整理，**不运行代码、不安装 MATLAB/Octave/CODESYS/PLC 软件、不连接工业设备**。下表说明每套案例覆盖什么、用哪份文档配合读、以及本地路径。

完整性：完整 = 官方示例树或全文 PDF 已核验；部分 = 公开 HTML 按配额/层级截断，范围见目录备注。

| 编号 | 标题 | 类型 | 完整 | 主题 | 建议配合 | 本地路径 |
|---|---|---|---|---|---|---|
| CS02X01 | Control Guru — Practical Process Control | HTML 教程包 | 部分 | FOPDT、PID 整定、回路振荡 | Åström FBS、Siemens Easy Book PID 章 | `02_classical_control/practice/ControlGuru_PracticalProcessControl_html_en.tar` |
| CS09X02 | python-control 官方 examples | git 示例 | 完整 | Bode/Nyquist、LQR、巡航、MRAC、CDS 练习 | python-control 用户指南、FBS/OBC | `09_simulation_practice/practice/python_control_examples_en.tar` |
| CS09X03 | CasADi example pack v3.7.2 | 官方 zip | 完整 | NLP、积分器、最优控制脚本 | CasADi User Guide v3.7.2 | `09_simulation_practice/practice/CasADi_example_pack_v3.7.2_en.zip` |
| CS09X04 | do-mpc examples | git 示例 | 完整 | CSTR、批处理、振荡器上的 MPC/MHE | do-mpc 文档、CasADi | `09_simulation_practice/practice/do_mpc_examples_en.tar` |
| CS09X05 | APMonitor PDC 温度控制实验页 | HTML | 部分 | TCLab、FOPDT 辨识、PID、GEKKO 仿真 | BYU PDC 课程包 CS07C01 | `09_simulation_practice/practice/APMonitor_PDC_labs_html_en.tar` |
| CS09X07 | GEKKO examples | git 示例 | 完整 | 动态优化、MPC、估计 | APMonitor 实验页、MPC 教材 | `09_simulation_practice/practice/GEKKO_examples_en.tar` |
| CS09X08 | Scientific Python Lectures（signal 相关） | git 讲义 | 完整 | LTI、滤波数值实验 | SciPy.signal 文档 | `09_simulation_practice/practice/ScientificPythonLectures_signal_en.tar` |
| CS09X09 | TCLab Python 包示例 | git | 完整 | 温度对象接口与示例（不含硬件操作） | CS09X05 实验页 | `09_simulation_practice/practice/TCLab_python_package_en.tar` |
| CS07X02 | Modbus Messaging Implementation Guide V1.0b | 官方 PDF | 完整 | Modbus TCP、MBAP、客户端/服务器 | Modbus 应用层规范 CS07T03 | `07_industrial_automation/practice/Modbus_MessagingImplementationGuide_V1_0b_en.pdf` |
| CS07X03 | open62541 examples | git 示例 | 完整 | OPC UA Server/Client 示例 | open62541 `doc/` 源 CS07T04 | `07_industrial_automation/practice/open62541_examples_en.tar` |
| CS08X01 | Mastering the FreeRTOS Real Time Kernel | 官方教程 PDF | 完整 | 任务、队列、优先级、实时调度 | Fiore 嵌入式教材 | `08_hardware_realtime/practice/Barry_MasteringFreeRTOS_KernelTutorial_161204_en.pdf` |

## 建议上机顺序（以后再做）

1. **回路直觉**：Control Guru 的 FOPDT/PID 页 + python-control examples 里的巡航/电机。
2. **辨识与 PID**：APMonitor TCLab 模块页（先读，再考虑是否接硬件）；GEKKO 示例做仿真对照。
3. **MPC**：CasADi example pack → do-mpc CSTR/batch。
4. **工业通信**：先读 Modbus 两份规范，再对照 open62541 examples 的节点读写（不要对着付费 IEC 原文）。
5. **实时部署概念**：FreeRTOS 教程中的任务与优先级，对应控制回路的周期任务，不刷固件。

## 工具文档（实践时打开，不计实践套数）

见 `09_simulation_practice/tools/` 与 `07_industrial_automation/tools/`：Octave、python-control、SciPy.signal、CasADi、do-mpc、OpenModelica、Octave control 包、Scilab/Xcos、CODESYS First Steps、Siemens S7-1200 Easy Book、Modbus 规范、open62541 文档源。

## 未计入的失败实践

- 密歇根 CTMS：站点拒绝抓取（403/空包）。
- fbswiki 补充页、open62541 HTML tutorial：镜像不完整。已分别被 python-control examples 与 open62541 `doc/`+`examples/` 覆盖，不重复计数。
