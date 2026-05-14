---
name: scientific-toolkit-skill
description: Research computing toolkit for optoelectronic information science and engineering, MATLAB/Octave, Python scientific analysis, signal processing, image processing, statistics, simulation, optimization, publication figures, sensor/time-series data, citation lookup, and common scientific libraries. Use when the user asks for MATLAB code, scientific Python, data analysis, plots, simulations, formulas, statistics, machine learning, optical/physical/materials computation, or reproducible research workflows.
---

# Scientific Toolkit Skill

## Scope

Use this skill for科研计算 and software-assisted research:

- MATLAB/Octave scripts, debugging, refactoring, signal/image processing, FFT, filtering, matrix computation, simulation, and figure export.
- Python scientific workflows with NumPy, SciPy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, SymPy, and related tools.
- Statistics, exploratory data analysis, sensor/time-series forecasting, optimization, discrete-event simulation, quantum optics/open quantum systems, materials data, and graph/network analysis.
- Literature lookup, citation metadata, BibTeX, and reference verification when it supports coding or research analysis.

Use `research-writing-skill` for manuscript prose. Use `office-academic-skill` for Word/PPT deliverables.

## Domain Defaults

The user's field is光电信息科学与工程. Prefer examples and checks relevant to:

- Optics, optoelectronics, optical communication, optical sensing, fiber sensing, BOTDR/BOTDA, BGS, SPM, dispersion, noise, and deconvolution.
- Signal processing, image processing, spectroscopy, detector data, sensor time series, calibration, and uncertainty.
- MATLAB simulation and reproducible figure generation for论文/答辩.

Do not fabricate physical parameters, material constants, software menu operations, experimental results, or paper conclusions. When uncertain, ask for the source file or mark the assumption.

## General Workflow

1. Read the provided code, data, README, docs, and project instructions before changing anything.
2. Identify variables, dimensions, units, input/output paths, random seeds, and expected figures.
3. Make small, verifiable changes and avoid unrelated refactors.
4. Prefer mature libraries over hand-rolled numerical methods.
5. Run a script-level or test-level verification when possible.
6. Report environment, commands, output paths, generated figures, and known limitations.

## MATLAB And Figures

- Preserve the original code structure when possible.
- Add concise comments for physical meaning, units, assumptions, or formula sources.
- Centralize key parameters and avoid hardcoded absolute paths.
- Add `rng` for stochastic simulations when reproducibility matters.
- For publication figures, export both high-resolution `.png` and vector `.svg` when feasible.
- Check axes, units, legends, sampling rate, line width, font, color, and image resolution.

For MATLAB/Octave details, use `references/scientific-skills/matlab/SKILL.md`.

## Python Scientific Modules

Load only the relevant bundled reference:

- Plotting and publication figures: `matplotlib`, `seaborn`, `scientific-visualization`.
- Statistics and time series: `statistical-analysis`, `statsmodels`, `timesfm-forecasting`.
- Machine learning: `scikit-learn`.
- Symbolic math and formulas: `sympy`.
- Exploratory data analysis: `exploratory-data-analysis`.
- Optimization: `pymoo`.
- Simulation: `simpy`.
- Quantum optics/open quantum systems: `qutip`.
- Materials/crystal/band/DOS workflows: `pymatgen`.
- Graphs/networks/citation graphs: `networkx`.
- FITS or astronomical/optical imaging style data: `astropy`.
- Spreadsheet/PDF utilities: `xlsx`, `pdf`.
- Literature/citation support: `paper-lookup`, `citation-management`, `literature-review`.

Some bundled references mention optional installs such as `uv pip install ...` or optional API keys for higher rate limits. Do not install packages, use cloud APIs, or send user data to external services unless the current task requires it and the user agrees.

## Safety Rules

- Never expose or commit API keys, tokens, private data, or unpublished paper content.
- Do not overwrite original data, code, Word/PPT, or figures. Write versioned outputs.
- Do not delete or recursively clean user files without explicit confirmation.
- For external lookups, prefer open APIs and official documentation; clearly distinguish live lookup results from local inference.

## Verification

For code:

- Run the relevant script or a minimal example.
- Check generated files exist and are readable.
- Inspect plots for axes, units, legends, and plausible dimensions.

For research analysis:

- State software versions when known.
- List input files and commands.
- Mark assumptions and uncertain parameters.

