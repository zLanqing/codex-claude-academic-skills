# Reader-skill Report Structure

Use this structure when generating literature report documents from academic papers.

## Bilingual Report

Title page:
- Paper title / 论文标题
- Authors / 作者
- Venue and year / 期刊会议与年份
- DOI, arXiv, URL, or source file / 文献来源
- Report generation date / 汇报生成日期

1. Executive Summary / 快速总览
- Research question / 研究问题
- Core method / 核心方法
- Main finding / 主要发现
- Why it matters / 学术或工程意义
- Evidence label for each key point

2. Reading Map / 阅读导图
- Suggested reading order
- Important sections, figures, tables, and equations
- What to focus on when preparing a group meeting or presentation

3. Background and Motivation / 背景与动机
- Field context
- Unsolved problem or limitation in prior work
- Paper's stated objective

4. Method / 方法
- Overall framework
- Core model, algorithm, experiment workflow, or theoretical derivation
- Formula list with variable definitions, units, and assumptions
- Implementation details if present

5. Experiments or Evidence / 实验、仿真或论证证据
- Dataset/sample/device/software/environment
- Parameter settings
- Baselines or controls
- Evaluation metrics

6. Results / 结果分析
- Key quantitative results
- Figure/table-by-figure/table interpretation
- What each result supports
- Any contradictory or weak evidence

7. Contributions and Novelty / 创新点
- Contribution claimed by the authors
- Evidence from the paper
- Whether the novelty is methodological, experimental, theoretical, application-oriented, or system-level

8. Limitations / 局限性
- Limitations stated by the authors
- Limitations inferred from scope, assumptions, dataset, sample size, metrics, or missing ablation
- Label inferred points clearly

9. Reproducibility / 可复现要点
- Required data, code, instruments, software, versions, parameters, and steps
- Missing details that prevent reproduction

10. Relationship to User Topic / 与用户课题关系
- Directly reusable ideas
- Cautions before reuse
- Possible extension experiments or simulations

11. Presentation Notes / 汇报讲稿要点
- 5-minute version
- 10-minute version
- likely questions from supervisor or audience

12. Reference Trace Table / 原文依据索引表
- Claim
- Source location
- Evidence type: text, equation, figure, table, experiment
- Confidence: high, medium, low

## Chinese-Only Report

Use the same intellectual structure, but make all explanatory prose Chinese. Preserve English titles, model names, software names, formulas, variable symbols, datasets, and cited reference names.

Recommended Chinese headings:
- 文献信息
- 一页式摘要
- 阅读路线
- 研究背景与问题
- 方法与模型
- 实验/仿真/数据设置
- 结果与图表解读
- 创新点与贡献
- 局限性与边界条件
- 可复现要点
- 与用户课题的关系
- 汇报讲稿要点
- 原文依据索引表

## Evidence Label Format

Preferred:
- `来源: Section 2.1, p. 3`
- `来源: Methods, pp. 4-5, Eq. (3)`
- `来源: Results, Fig. 5 and Table 2`
- `来源: 原文 Discussion, p. 9`

If exact location is unavailable:
- `来源: 原文未提供页码；见 Results 小节关于 Fig. 4 的段落`
- `来源: PDF 文本提取未识别章节号；见第 6 页表格下方段落`

Inference labels:
- `推断: 基于作者实验设置和缺失消融项`
- `建议: 可作为后续仿真实验方向，非原文结论`

## Quality Checklist

Before final delivery:
- Both reports exist and open.
- Chinese text is readable, not garbled.
- Each key conclusion has a source label.
- Quantitative values match the paper.
- Figures, tables, and equations are not misnumbered.
- Inferred comments are not mixed with original claims.
- The report notes missing information honestly.
- The final answer lists exact output paths and verification.
