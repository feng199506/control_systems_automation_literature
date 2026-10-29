# 下载与解压恢复说明（自动控制与工业自动化文献库，2026-10-29）

本资料库按“轻量 Git 分支 + Release 全文附件”的方式发布：

- **Git 分支 `release-lite-20261029`**：只包含总目录 `catalog_cn.csv`、进度、学习路线、实践索引、检索记录、失败清单、脚本、断点状态（`state/`）和本说明，不含 PDF 全文、课程包、工具文档镜像和实践案例。
- **Release `control-full-20261029`**：1 个不压缩的 `.tar` 包，就是完整的资料库，包括 9 个子方向目录下的全部教材、课程、论文、工具文档和实践案例。

Release 页面：https://github.com/feng199506/control_systems_automation_literature/releases/tag/control-full-20261029

## 1. 包列表

| 包文件名 | 内容 |
|---|---|
| `control_systems_automation_20261029_batch001_cn_en.tar` | 整个资料库：顶层目录与报告、`scripts/`、`state/`、`01_foundations/` 至 `09_simulation_practice/`（包括空的占位子目录） |

每个文件的路径和字节数见 `archive_index_cn.csv`（UTF-8 带 BOM，可直接用 Excel 打开；354 行，其中 335 个文件、19 个空目录）。

包没有压缩，解压很快，所需磁盘空间约等于包的大小。解压约需 **1.1 GiB**；如果还要展开里面的课程包和文档镜像（见第 4 节），建议预留 3 GiB。

## 2. Windows：浏览器下载

1. 打开上面的 Release 页面，展开 **Assets**。
2. 点击 `.tar` 文件，以及 `archive_index_cn.csv`、`windows_rename_map_cn.csv`、`download_restore_cn.md`、`upload_report_cn.md`，全部保存到同一个下载文件夹，例如 `D:\下载\control\`。
3. 包大约 1.1 GB。浏览器提示“是否保留”时选择保留。下载中断可在浏览器下载列表里点“恢复”或重新下载。
4. 对照 `upload_report_cn.md` 中的字节数，在文件属性里核对包的大小（看“大小”的字节数，不要看“占用空间”）。

## 3. Windows：WinRAR 解压

请使用 **WinRAR 6 或更新版本**，目标目录用短路径，例如 `D:\control\`。

1. 右键 `.tar` 文件 → **WinRAR → 解压文件…**（Extract files…）。
2. “目标路径”填 `D:\control\` → 确定。

解压后的目录结构：

```
D:\control\
├─ README_cn.md、catalog_cn.csv、learning_path_cn.md、practice_index_cn.md、progress_cn.csv …
├─ 01_foundations\ … 09_simulation_practice\
├─ scripts\
└─ state\
```

### Windows 文件名兼容

发布包里的全部文件名都已检查并处理，Windows 下解压不会因文件名报错。最长相对路径 114 个字符。资料库的本地原件没有改动；改名明细逐条记录在 `windows_rename_map_cn.csv` 里。

- 发布包第一层的 335 个文件，名字都没有 Windows 不允许的字符，也没有只差大小写的文件，没有改名。
- 有 7 个内层网页离线包的文件名带 `?`，例如 `index.html?p=11.html`、`theme.css?v=…`。这 7 个包在发布包里已经重新打包，包内文件名中的 `?` 一律改成 `_`，网页里对应的链接也同步改写了，所以离线打开时仍能正常显示。除此之外，包里的其他内容都没有变。由于重新打包过，这 7 个文件的字节数与资料库原件不同，这是正常的。共涉及 126 个文件。
  - `02_classical_control/practice/ControlGuru_PracticalProcessControl_html_en.tar`（53 个）
  - `07_industrial_automation/courses/BYU_ProcessDynamicsControl_Online_HTML_en.zip`（1 个）
  - `07_industrial_automation/tools/CODESYS_FirstSteps_html_en.tar`（7 个）
  - `09_simulation_practice/practice/APMonitor_PDC_labs_html_en.tar`（13 个）
  - `09_simulation_practice/tools/OctaveForge_control_package_docs_html_en.tar`（6 个）
  - `09_simulation_practice/tools/do_mpc_Documentation_html_en.tar`（16 个）
  - `09_simulation_practice/tools/python_control_UserGuide_html_en.tar`（30 个）
- 其余 10 个 `.zip` 和 11 个 `.tar` 已逐个检查，无需改动。

## 4. 内层归档（.zip / .tar）

资料库本身就把一部分资料整包保存，解压发布包之后它们仍是单个文件：

- **11 个 `.zip`**：主要是 MIT OCW 课程包，另有 BYU 过程控制在线课程的网页版和 CasADi 示例包。
- **17 个 `.tar`**：工具文档的 HTML 离线镜像或文档源（python-control、SciPy.signal、do-mpc、Octave Forge control、Scilab/Xcos、CODESYS、open62541），以及实践案例的网页或源码快照（Control Guru、APMonitor、GEKKO、TCLab、do-mpc 和 python-control 示例等）。

需要时右键该文件 → WinRAR → **解压到 “文件名\”**。网页离线包解开后，用浏览器打开其中的 `index.html`。

`01_foundations/books/Smith_ScientistEngineersGuideDSP_en/` 是一本按章节分开的 PDF 书，文件扩展名是大写的 `.PDF`，这是原书本来的样子。

## 5. Linux / macOS

```bash
mkdir -p ~/control
tar -xf control_systems_automation_20261029_batch001_cn_en.tar -C ~/control
```

## 6. 资料状态说明（来自资料库自身的目录，与打包无关）

- **只计已核验条目**：共 106 条，分别是教材 19、大学课程 14、论文 50（近三年 43 篇，占 86.0%）、官方工具文档 12、实践案例 11。
- **部分资料 7 条**：`catalog_cn.csv` 的“完整性状态”列里有 7 条标为“部分资料（已核验，范围见说明）”，都是网页离线镜像，具体范围见该表的“核验说明”和“范围说明”两列。
- **失败 5 项**，记录在 `download_failures_cn.csv`，没有计入，也没有对应文件：
  - MathWorks Control System Toolbox 和 System Identification Toolbox 的 PDF 返回 403；
  - 密歇根 CTMS 的网页镜像为空；
  - fbswiki 和 open62541 的教程页没有抓全。
- 本次按 2026-10-29 20:31（中欧时间）的资料库内容打包。打包前先把整个资料库复制成一份快照，打包用的就是这份快照。资料库的最后一次改动是在 19:51。

## 7. 完整性说明

- 本次发布只登记了上传状态（以 GitHub API 显示附件为 `uploaded`、远端大小等于本地大小为准），**没有**做下载回验和哈希校验。
- 资料库本身没有整库的 SHA-256 清单。
- 资料库中的资料文件都已打包，没有遗漏。只排除了 3 类不属于资料的内容：
  - 本地 `.git/`；
  - `scripts/__pycache__/` 中的 2 个 `.pyc`；
  - `state/` 下 7 个空的 `.lock` 锁文件。
