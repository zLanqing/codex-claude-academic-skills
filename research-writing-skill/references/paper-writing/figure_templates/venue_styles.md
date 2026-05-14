# Venue-Specific Figure Styling Defaults

These defaults apply to ALL non-data figures (both AI-generated and TikZ). They ensure figures match the paper's formatting and print correctly.

---

## Column Widths

| Venue family | Single column | Double column (figure*) | Margin notes |
|-------------|---------------|------------------------|--------------|
| **USENIX** (NSDI, OSDI, ATC, Security) | 3.33 in | 7.0 in | None |
| **ACM** (SIGCOMM, IMC, CoNEXT, MobiCom) | 3.5 in | 7.16 in | None |
| **IEEE** (INFOCOM, ICNP, TDSC) | 3.5 in | 7.16 in | None |

Architecture overview figures almost always span full width (double column). Pipeline details and component diagrams fit single column.

## Font Rules

- **Body text in figure labels** must be legible at print size: **8 pt minimum**, 9 pt preferred.
- Match the paper's body font family where possible:
  - USENIX: Times / Linux Libertine
  - ACM: Times New Roman
  - IEEE: Times New Roman
- **Sans-serif** (Helvetica, CMSans) is acceptable for diagram labels and annotations — it improves readability inside boxes and along arrows.
- **Bold** only for the figure's title element or the component representing the paper's key contribution.

## Color Palette

Use the **Paul Tol "bright" palette** — colorblind-safe and print-friendly:

| Name | Hex | Use |
|------|-----|-----|
| Blue | `#4477AA` | Primary components, input data flow |
| Cyan | `#66CCEE` | Secondary components, intermediate stages |
| Green | `#228833` | Output / results / success states |
| Yellow | `#CCBB44` | Warnings, optional paths, annotations |
| Red | `#EE6677` | Errors, failures, key problems |
| Purple | `#AA3377` | External systems, baselines, prior work |
| Grey | `#BBBBBB` | Background elements, inactive components, context |
| White | `#FFFFFF` | Figure background (always white) |

**Rules:**
- Maximum 5-6 distinct colors per figure.
- Use grey for elements that provide context but are not the focus.
- The paper's key contribution component should use the most visually prominent color (Blue or Green).
- Reserve Red for problem/failure states in comparison schematics.

## Line and Shape Standards

| Element | Weight | Style |
|---------|--------|-------|
| Box borders | 0.5 pt | Solid |
| Primary arrows (data flow) | 0.75 pt | Solid, filled arrowhead |
| Secondary arrows (control flow) | 0.5 pt | Dashed |
| Connection lines | 0.5 pt | Solid |
| Grouping boxes | 0.5 pt | Dashed, rounded corners |
| Emphasis borders | 1.0 pt | Solid (for key contribution) |

## TikZ Preamble (for TikZ-backend figures)

```latex
\usepackage[dvipsnames]{xcolor}
\usepackage{tikz}
\usetikzlibrary{positioning, arrows.meta, shapes.geometric, fit, calc, backgrounds}

% Paul Tol bright palette
\definecolor{ptblue}{HTML}{4477AA}
\definecolor{ptcyan}{HTML}{66CCEE}
\definecolor{ptgreen}{HTML}{228833}
\definecolor{ptyellow}{HTML}{CCBB44}
\definecolor{ptred}{HTML}{EE6677}
\definecolor{ptpurple}{HTML}{AA3377}
\definecolor{ptgrey}{HTML}{BBBBBB}

% Standard node styles
\tikzset{
    component/.style={rectangle, draw, rounded corners=3pt,
        minimum width=2cm, minimum height=0.8cm,
        font=\small\sffamily, thick},
    arrow/.style={-{Stealth[length=5pt]}, thick},
    dashedarrow/.style={-{Stealth[length=5pt]}, dashed},
    group/.style={draw=gray!50, dashed, rounded corners=5pt, inner sep=8pt},
    annotation/.style={font=\footnotesize\sffamily, text=gray!70!black},
}
```

## AI Prompt Styling Block

Inject this block into every AI image generation prompt to ensure venue-appropriate output:

```
STYLING REQUIREMENTS (non-negotiable):
- Pure white background (#FFFFFF)
- Clean, professional academic style suitable for a top-tier systems/networking venue (NSDI, SIGCOMM, IMC)
- All text labels must be crisp, readable, and at least 8pt equivalent at print size
- Use sans-serif font for all labels and annotations
- Color palette: blue (#4477AA) for primary components, cyan (#66CCEE) for secondary,
  green (#228833) for outputs, grey (#BBBBBB) for context/background elements
- Maximum 5-6 distinct colors
- Solid lines for data flow arrows (0.75pt), dashed for control flow (0.5pt)
- No gradients, no drop shadows, no 3D effects, no decorative elements
- No clip art, no stock imagery, no photorealistic elements
- Every visual element must encode information — nothing purely decorative
- Rounded corners on component boxes (3pt radius)
- Filled arrowheads on all directional arrows
- Group related components with dashed boundary boxes and phase/stage labels
- The figure must be self-contained: a reader should understand the high-level flow without reading the paper
```

## Print Safety Checklist

Before finalizing any figure, verify:
1. Readable in grayscale (not just color) — shapes and labels distinguish components, not only color
2. Text legible at 50% zoom (simulates print at column width)
3. No thin hairlines that may vanish in print (minimum 0.5pt)
4. White background (no transparency issues in PDF embedding)
5. Aspect ratio fits the target column width without scaling below legibility
