# Academic Skills for Claude Code & Codex

> 三个面向中国科研工作者的学术技能包，覆盖论文写作、学术 Office 文档生成与科研计算三大场景。
> 所有 skill 均可在 **Claude Code** 和 **Codex** 两个平台上直接使用。

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Claude%20Code-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Platform-Codex%20CLI-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Language-Chinese--first-red?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Skills-3-purple?style=flat-square" />
</p>

---

## 技能概览

| 技能 | 核心用途 | 典型场景 |
|------|----------|----------|
| [`research-writing-skill`](#1-research-writing-skill--论文写作) | 论文章节撰写、修改、润色 | 论文正文、摘要、引言、方法、实验、回复审稿人 |
| [`office-academic-skill`](#2-office-academic-skill--学术-office-文档) | 学术 Word/PPT 生成与编辑 | 文献阅读报告、组会 PPT、开题/中期/答辩 PPT |
| [`scientific-toolkit-skill`](#3-scientific-toolkit-skill--科研计算工具箱) | 科研计算与数据分析 | MATLAB/Python 仿真、信号处理、统计、机器学习、论文配图 |

三个 skill 设计为**互补协作**关系，可在同一任务中联动调用：

```
论文写作场景：
  scientific-toolkit-skill（数据分析、出图）
  → research-writing-skill（撰写论文正文）
  → office-academic-skill（生成答辩 PPT）

文献阅读场景：
  office-academic-skill（PDF → Word 阅读报告）
  → office-academic-skill（组会 PPT）

仿真研究场景：
  scientific-toolkit-skill（MATLAB/Python 仿真 + 论文配图）
  → research-writing-skill（方法 + 实验章节）
```

---

## 1. research-writing-skill — 论文写作

**中文优先**的学术写作技能，适用于论文正文、LaTeX/Overleaf 文稿、学位论文等。

### 功能

- 论文各章节撰写：摘要、引言、相关工作、方法、实验、讨论、结论
- 论文修改与润色：逻辑性、术语一致性、引用准确性
- 审稿意见回复（Rebuttal / Peer-review response）
- 论证规划：从模糊想法到论文大纲

### 写作原则

- 默认中文表达，保留英文标题、公式、变量、方法名、软件命令、参考文献
- 不编造数据、DOI、期刊信息、实验结果
- 区分「原文/已有数据」「用户确认内容」「推断」「建议性扩展」四类信息
- 避免「显著」「先进」「有效」等模糊用词，代之以可测量的条件和对比基准

### 内置参考资源

| 路径 | 内容 |
|------|------|
| `paper-writing/section_rhetorical_moves/` | 各章节修辞结构指南 |
| `paper-writing/writing_checklists/` | 写作自查清单 |
| `paper-writing/figure_templates/` | 图表规划模板 |
| `paper-writing/brainstorming_guide.md` | 从想法到论文蓝图 |

---

## 2. office-academic-skill — 学术 Office 文档

**中文优先**的学术 Word 和 PowerPoint 工作流，生成可编辑的 `.docx` 和 `.pptx` 文件。

### 功能

**Word 文档**

- PDF/论文 → 文献阅读报告（双语或中文）
- 结构化 DOCX 生成：标题、表格、图表占位符、来源标注
- 对已有 Word 文档进行版本化编辑

**PowerPoint 演示文稿**

- 文献报告 PPT、组会 PPT、课程报告 PPT
- 开题/中期/答辩 PPT（模板匹配、母版克隆）
- 科研展示 PPT、科普 PPT

### PPT 质量规则

- 每页一个核心观点，使用「行动标题」（陈述结论而非话题标签）
- 图表、公式承载技术论证，避免大段文字
- 保持坐标轴、单位、图例、公式、数据来源的科学准确性
- 白色或克制的学术背景，用颜色引导注意力

### 内置参考资源与工具

| 路径 | 内容 |
|------|------|
| `office-docx/` | OOXML 级别 DOCX 检查与编辑，含 XSD 模式库 |
| `office-pptx/` | OOXML 级别 PPTX 检查与编辑 |
| `thesis-defense-pptx/scripts/` | 论文上下文提取、模板克隆、幻灯片导出、溢出检查等工具脚本 |
| `report-structure.md` | 默认文献报告结构与证据标注格式 |

---

## 3. scientific-toolkit-skill — 科研计算工具箱

面向**光电信息科学与工程**领域的科研计算技能。

### 功能

**MATLAB/Octave**

- 信号/图像处理、FFT、滤波、矩阵计算、仿真、论文配图导出
- 保留原始代码结构，集中管理关键参数，添加物理意义注释

**Python 科学计算**

| 库 | 用途 |
|----|------|
| NumPy, SciPy, pandas | 数据处理与数值计算 |
| matplotlib, seaborn | 论文级数据可视化 |
| scikit-learn | 机器学习（分类、回归、聚类、降维）|
| statsmodels | 统计建模（线性模型、时间序列、GLM）|
| SymPy | 符号数学与公式推导 |
| pymoo | 多目标优化 |
| simpy | 离散事件仿真 |
| QuTiP | 量子光学/开放量子系统 |
| pymatgen | 材料科学计算（晶体结构、能带、态密度）|
| TimesFM | 时间序列预测 |
| NetworkX | 图与网络分析 |
| Astropy | 天文/光学成像数据处理 |

**文献与引用**

- 论文查找：arXiv, PubMed, CrossRef, Semantic Scholar, OpenAlex
- 引文管理：DOI → BibTeX，文献元数据提取，引文验证

### 领域关注

- 光学、光电子、光通信、光纤传感
- BOTDR/BOTDA、BGS、SPM、色散、噪声、去卷积
- 光谱学、探测器数据、传感器时间序列、标定与不确定度

### 内置参考资源

20+ 子模块的详细参考文档、脚本模板和示例，包括 matplotlib 出图模板、统计检验选择指南、scikit-learn 分类管线等。

---

## 跨平台安装

三个 skill 采用相同的目录结构和 SKILL.md 格式，在 Claude Code 和 Codex 中均可直接加载。

### Claude Code

```bash
# 克隆仓库
git clone https://github.com/你的用户名/claude-academic-skills.git

# 安装到全局 skills 目录
cp -r claude-academic-skills/research-writing-skill ~/.claude/skills/
cp -r claude-academic-skills/office-academic-skill ~/.claude/skills/
cp -r claude-academic-skills/scientific-toolkit-skill ~/.claude/skills/
```

也可通过 Plugin 方式一键安装：

```bash
/plugin install 你的用户名/claude-academic-skills
```

### Codex

```bash
# 安装到全局 skills 目录
cp -r claude-academic-skills/research-writing-skill ~/.codex/skills/
cp -r claude-academic-skills/office-academic-skill ~/.codex/skills/
cp -r claude-academic-skills/scientific-toolkit-skill ~/.codex/skills/
```

也可通过 `--plugin-url` 参数在当前会话中直接加载：

```bash
codex --plugin-url https://github.com/你的用户名/claude-academic-skills
```

> 如需**项目级安装**，将 skill 目录放入项目根目录下的 `.claude/skills/` 或 `.codex/skills/` 即可，仅对该项目生效。

---

## 目录结构

每个 skill 统一采用以下结构：

```
skill-name/
├── SKILL.md          # 技能定义与使用说明
├── agents/           # 子代理配置
└── references/       # 参考文档、脚本、模板等资源
```

---

## 语言与证据规范

三个 skill 共同遵循以下规范：

| 规范 | 说明 |
|------|------|
| **默认中文** | 解释、正文撰写、幻灯片制作均使用中文 |
| **保留英文** | 论文标题、公式、变量名、模型名、软件命令、参考文献条目 |
| **不编造数据** | 不虚构 DOI、作者、期刊、实验值、图表编号、页码、结论 |
| **标注来源** | 对声明、参数、定量结果、数据集、图表等附加来源标签 |

---

## 致谢

本项目在设计过程中参考了以下优秀的开源 Skill 项目，感谢这些作者的公开贡献：

| 项目 | 简介 |
|------|------|
| [zouchenzhen/thesis-defense-pptx-skill](https://github.com/zouchenzhen/thesis-defense-pptx-skill) | 从论文 PDF/LaTeX 生成可编辑答辩 PPTX，支持模板风格保留、逐页 PNG 导出与文字溢出检查，专为 Windows + PowerPoint 环境优化 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 134+ 科研 Agent Skill 集合，涵盖 MATLAB/Octave、Matplotlib、信号处理、科学可视化等模块 |
| [tfriedel/claude-office-skills](https://github.com/tfriedel/claude-office-skills) | 系统化的 Office 文档处理 Skill 集，包含 docx/、pptx/、pdf/、xlsx/ 四个子模块，结构清晰 |
| [Gabberflast/academic-pptx-skill](https://github.com/Gabberflast/academic-pptx-skill) | 专注学术 PPT 规范：结论式标题、每页一个核心观点、图表引用标准与参考文献页 |
| [SNL-UCSB/paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) | 编码了经过验证的论文写作原则，涵盖论证逻辑、图表支撑、初稿重构与压缩 |

---

## 许可

本仓库采用 [MIT License](LICENSE) 开源许可。

- 你可以自由使用、复制、修改、合并、发布、分发、再许可和/或销售软件的副本
- 需在软件所有副本或实质性部分中保留版权声明和本许可声明
- 软件按「原样」提供，不提供任何形式的明示或暗示保证

其中引用的部分外部资源（如 `scientific-toolkit-skill/references/scientific-skills/` 中的脚本）遵循其原始许可协议。
