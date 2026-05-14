# TikZ Skeletons by Archetype

These are starter templates for the TikZ-default archetypes. Each skeleton compiles standalone and follows the venue styling from `venue_styles.md`. Replace placeholder content with figure-specific components from the `figure_spec.md`.

---

## Pipeline / Process Flow

Sequential transformation of data through stages. Vertical or horizontal. Each stage shows input shape → transformation → output shape.

```latex
\documentclass[border=5pt]{standalone}
\usepackage[dvipsnames]{xcolor}
\usepackage{tikz}
\usetikzlibrary{positioning, arrows.meta, shapes.geometric, fit, calc}

% Paul Tol bright palette
\definecolor{ptblue}{HTML}{4477AA}
\definecolor{ptcyan}{HTML}{66CCEE}
\definecolor{ptgreen}{HTML}{228833}
\definecolor{ptgrey}{HTML}{BBBBBB}

\begin{document}
\begin{tikzpicture}[
    node distance=0.6cm and 1.8cm,
    stage/.style={rectangle, draw, rounded corners=3pt, thick,
        minimum width=2.2cm, minimum height=0.7cm,
        font=\small\sffamily},
    data/.style={font=\footnotesize\sffamily, text=gray!60!black},
    arrow/.style={-{Stealth[length=5pt]}, thick},
]

% --- Stages (left to right) ---
\node[stage, fill=ptblue!15] (s1) {Stage 1};
\node[stage, fill=ptcyan!15, right=of s1] (s2) {Stage 2};
\node[stage, fill=ptgreen!15, right=of s2] (s3) {Stage 3};

% --- Data annotations between stages ---
\node[data, above=0.15cm of s1.west, anchor=south west] {Raw input};
\draw[arrow] (s1) -- node[data, above] {intermediate} (s2);
\draw[arrow] (s2) -- node[data, above] {transformed} (s3);
\node[data, above=0.15cm of s3.east, anchor=south east] {Output};

% --- Input/output markers ---
\draw[arrow, ptgrey] ([xshift=-1cm]s1.west) -- (s1.west);
\draw[arrow, ptgreen] (s3.east) -- ([xshift=1cm]s3.east);

\end{tikzpicture}
\end{document}
```

**Customization points:**
- Add/remove stage nodes as needed
- Add data shape annotations (e.g., "[N x D tensor]") as `data` nodes
- For vertical flow, change `right=of` to `below=of` and adjust arrow directions
- Add branching with additional nodes positioned above/below the main flow

---

## Component Detail

Zoomed view of a single pipeline component showing internal structure. Uses nested boxes to show sub-components.

```latex
\documentclass[border=5pt]{standalone}
\usepackage[dvipsnames]{xcolor}
\usepackage{tikz}
\usetikzlibrary{positioning, arrows.meta, fit, backgrounds}

\definecolor{ptblue}{HTML}{4477AA}
\definecolor{ptcyan}{HTML}{66CCEE}
\definecolor{ptgreen}{HTML}{228833}
\definecolor{ptgrey}{HTML}{BBBBBB}

\begin{document}
\begin{tikzpicture}[
    node distance=0.5cm and 0.8cm,
    subcomp/.style={rectangle, draw, rounded corners=2pt,
        minimum width=1.8cm, minimum height=0.6cm,
        font=\footnotesize\sffamily, thick},
    arrow/.style={-{Stealth[length=4pt]}, thick},
    label/.style={font=\footnotesize\sffamily\bfseries},
]

% --- Sub-components ---
\node[subcomp, fill=ptblue!15] (a) {Sub-component A};
\node[subcomp, fill=ptcyan!15, right=of a] (b) {Sub-component B};
\node[subcomp, fill=ptgreen!15, below right=0.8cm and 0cm of $(a)!0.5!(b)$] (c) {Sub-component C};

% --- Internal connections ---
\draw[arrow] (a) -- (b);
\draw[arrow] (a) |- (c);
\draw[arrow] (b) |- (c);

% --- Outer boundary ---
\begin{scope}[on background layer]
\node[draw=ptblue, thick, dashed, rounded corners=5pt,
    fit=(a)(b)(c), inner sep=10pt,
    label={[label, anchor=south]above:Component Name}] {};
\end{scope}

% --- Input/output ---
\draw[arrow, ptgrey] ([xshift=-1.2cm]a.west) -- (a.west)
    node[pos=0, left, font=\footnotesize\sffamily] {Input};
\draw[arrow, ptgreen] (c.east) -- ([xshift=1.2cm]c.east)
    node[pos=1, right, font=\footnotesize\sffamily] {Output};

\end{tikzpicture}
\end{document}
```

**Customization points:**
- Add/remove sub-components
- Adjust layout (vertical vs. horizontal internal flow)
- Add parameter annotations next to sub-components
- Use `fill` colors to indicate which sub-components are novel vs. standard

---

## Taxonomy / Classification

2x2 matrix or hierarchical categorization. Use for positioning figures in related work or background sections.

### 2x2 Matrix Variant

```latex
\documentclass[border=5pt]{standalone}
\usepackage[dvipsnames]{xcolor}
\usepackage{tikz}
\usetikzlibrary{positioning, calc}

\definecolor{ptblue}{HTML}{4477AA}
\definecolor{ptcyan}{HTML}{66CCEE}
\definecolor{ptgreen}{HTML}{228833}
\definecolor{ptred}{HTML}{EE6677}
\definecolor{ptgrey}{HTML}{BBBBBB}

\begin{document}
\begin{tikzpicture}[
    cell/.style={rectangle, draw, rounded corners=2pt, thick,
        minimum width=3cm, minimum height=1.5cm,
        font=\small\sffamily, align=center},
    axislabel/.style={font=\small\sffamily\bfseries},
    entry/.style={font=\footnotesize\sffamily},
]

% --- Quadrant cells ---
\node[cell, fill=ptblue!10] (q1) at (0, 0) {Quadrant 1\\[2pt] {\footnotesize Work A, Work B}};
\node[cell, fill=ptcyan!10] (q2) at (3.5, 0) {Quadrant 2\\[2pt] {\footnotesize Work C}};
\node[cell, fill=ptred!10] (q3) at (0, -2) {Quadrant 3\\[2pt] {\footnotesize Work D, Work E}};
\node[cell, fill=ptgreen!15, line width=1.2pt] (q4) at (3.5, -2)
    {\textbf{This paper}\\[2pt] {\footnotesize (empty quadrant)}};

% --- Axis labels ---
\node[axislabel, above=0.3cm of $(q1.north)!0.5!(q2.north)$] {Dimension X};
\node[axislabel, rotate=90, left=0.3cm of $(q1.west)!0.5!(q3.west)$] {Dimension Y};

% --- Axis value labels ---
\node[entry, above=0.05cm of q1.north] {Low X};
\node[entry, above=0.05cm of q2.north] {High X};
\node[entry, rotate=90, left=0.05cm of q1.west] {High Y};
\node[entry, rotate=90, left=0.05cm of q3.west] {Low Y};

\end{tikzpicture}
\end{document}
```

### Hierarchical Tree Variant

```latex
\documentclass[border=5pt]{standalone}
\usepackage[dvipsnames]{xcolor}
\usepackage{tikz}
\usetikzlibrary{positioning, arrows.meta}

\definecolor{ptblue}{HTML}{4477AA}
\definecolor{ptcyan}{HTML}{66CCEE}
\definecolor{ptgreen}{HTML}{228833}
\definecolor{ptgrey}{HTML}{BBBBBB}

\begin{document}
\begin{tikzpicture}[
    node distance=0.6cm and 1.5cm,
    cat/.style={rectangle, draw, rounded corners=3pt, thick,
        minimum width=2cm, minimum height=0.6cm,
        font=\small\sffamily},
    leaf/.style={rectangle, draw, rounded corners=2pt,
        minimum width=1.6cm, minimum height=0.5cm,
        font=\footnotesize\sffamily},
    edge/.style={thick},
]

% --- Root ---
\node[cat, fill=ptblue!15] (root) {Category};

% --- Level 1 ---
\node[cat, fill=ptcyan!15, below left=0.8cm and 1.5cm of root] (l1a) {Subcategory A};
\node[cat, fill=ptcyan!15, below right=0.8cm and 1.5cm of root] (l1b) {Subcategory B};

% --- Leaves ---
\node[leaf, fill=ptgrey!20, below left=0.6cm and 0.3cm of l1a] (w1) {Work 1};
\node[leaf, fill=ptgrey!20, below right=0.6cm and 0.3cm of l1a] (w2) {Work 2};
\node[leaf, fill=ptgreen!20, line width=1.2pt, below=0.6cm of l1b] (ours) {\textbf{This paper}};

% --- Edges ---
\draw[edge] (root) -- (l1a);
\draw[edge] (root) -- (l1b);
\draw[edge] (l1a) -- (w1);
\draw[edge] (l1a) -- (w2);
\draw[edge] (l1b) -- (ours);

\end{tikzpicture}
\end{document}
```

**Customization points:**
- 2x2: Change axis dimensions and quadrant labels to match your positioning argument
- 2x2: Bold-border the quadrant where your paper sits (the "empty quadrant" claim)
- Tree: Add/remove levels and leaves
- Tree: Annotate edges with the distinguishing property (e.g., "statistical" vs. "learned")
