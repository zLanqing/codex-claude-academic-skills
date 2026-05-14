# Figure Synthesis Guide: Non-Data Figures for Systems/Networking Papers

This guide helps synthesize **conceptual figures** — architecture diagrams, pipeline illustrations, comparison schematics, and other non-data figures. It does NOT handle data figures (CDFs, bar charts, scatter plots, heatmaps) — those go through the [data-visualization-skill](https://github.com/SNL-UCSB/data-visualization-skill) via `/viz`.

**The boundary:** If a figure requires experimental data to render, it goes through `/viz`. If it illustrates structure, flow, or concepts, it comes here.

## Modes

- `/paper-writing figure spec` — Classify non-data figures, walk through archetype-specific questions, produce a `figure_spec.md`
- `/paper-writing figure generate` — Route to AI prompt or TikZ, produce the figure
- `/paper-writing figure critique` — Review against claims, venue formatting, design principles

## Choosing a Mode

When the user asks for help with a non-data figure, assess where they are:

| State | Suggested mode |
|-------|---------------|
| Has `project_context.md` but no `figure_spec.md` for this figure | **Spec** |
| Has a `figure_spec.md` but no generated figure | **Generate** |
| Has a generated figure and wants feedback | **Critique** |
| Not sure what figures they need | **Spec** (start from project_context.md's Key Figures Needed) |

If no `project_context.md` exists, stop. The student must run the brainstorming workflow first (`/paper-writing` → brainstorming). Figures cannot be designed in a vacuum — they serve claims, and claims live in the project context.

---

## Seven Figure Archetypes

Every non-data figure in a systems/networking paper fits one of these archetypes. The archetype determines which questions to ask in spec mode and which generation backend to use.

| Archetype | What it shows | Typical section | Default backend |
|-----------|--------------|-----------------|-----------------|
| **Architecture Overview** | Full system pipeline, end-to-end flow with named stages, phase groupings | §3 Design (opener), full-width | AI image generation |
| **Pipeline / Process Flow** | Sequential transformation of data through stages, with intermediate representations | §3 Design (subsection) | TikZ |
| **Component Detail** | Internal structure of one pipeline stage, sub-components and their interactions | §3 Design (subsection) | TikZ |
| **Concept Illustration** | Abstract concept made concrete — before/after, spatial analogy, visual metaphor | §2 Background / Motivation | AI image generation |
| **Comparison Schematic** | Why approach A fails and approach B works, side-by-side structural contrast | §1 or §2 Motivation, §3 Design justification | AI image generation |
| **Taxonomy / Classification** | Hierarchical or matrix organization of categories, positioning the paper | §5 Related Work, §2 Background | TikZ |
| **Deployment / System Diagram** | Physical or logical infrastructure topology, how the system runs in practice | §4 Evaluation setup, §2 Background | AI image generation |

**The student can override the default backend.** If they want TikZ for an architecture overview (for precise control) or AI generation for a taxonomy (for visual richness), respect that choice.

---

## Mode 1: Spec — "What does this figure need to show?"

### Step 1: Identify Non-Data Figures

Read `project_context.md` → "Key Figures Needed" section. For each figure listed:

1. **Classify as data or non-data.** Ask: "Does this figure require experimental data to render?"
   - Yes → route to `/viz`. Tell the student.
   - No → continue here.
2. **Assign an archetype** from the table above. If ambiguous, ask the student.
3. **Confirm the generation backend** (AI image or TikZ). State the default and let the student override.

Present a summary table:

| # | Figure | Section | Archetype | Backend |
|---|--------|---------|-----------|---------|
| 1 | ... | ... | ... | ... |

### Step 2: Walk Through Archetype-Specific Questions

For each non-data figure, ask the questions below. Skip questions the student has already answered in `project_context.md`. Push back on vague answers — every answer should be specific enough to appear in a generation prompt.

#### Architecture Overview Questions

1. What is the system's name?
2. How many major stages/phases does it have? Name them.
3. What is the input to the first stage? What is the output of the last stage?
4. For each stage: what transformation does it perform? What goes in, what comes out?
5. Which stage is the paper's key contribution? (This gets visual emphasis.)
6. Are there any parallel paths or branches in the pipeline?
7. Are there feedback loops or iterative components?
8. What groupings make sense? (e.g., "Offline training" vs. "Online inference")
9. Does the figure need to show data shapes/dimensions at each stage?

#### Pipeline / Process Flow Questions

1. What is being transformed? (e.g., "raw time series → event representation")
2. How many transformation steps are there?
3. For each step: what is the operation? Is it standard (off-the-shelf) or novel?
4. Where does the pipeline branch or merge?
5. Should intermediate data representations be shown (e.g., tensor shapes, data examples)?
6. Does the pipeline have a natural direction (left-to-right for temporal, top-to-bottom for processing depth)?

#### Component Detail Questions

1. Which component from the architecture overview is being expanded?
2. What are the sub-components inside it?
3. What are the internal data flows between sub-components?
4. Are there configurable parameters that should be annotated?
5. What makes this component different from a standard implementation?

#### Concept Illustration Questions

1. What is the concept you need to illustrate?
2. What is the reader's likely misconception or default mental model?
3. What type of illustration best corrects that misconception?
   - **Before/after**: "Here's the problem state → here's the improved state"
   - **Spatial analogy**: "Think of this as a 2D space where..."
   - **Visual metaphor**: "This works like a funnel / bridge / filter..."
   - **Process contrast**: "Existing approach does X; ours does Y"
4. What are the concrete elements in the illustration? (No abstract blobs — every shape must represent something named.)
5. Where is the "aha moment" — the point where the reader sees why the old way fails?

#### Comparison Schematic Questions

1. What two approaches are being compared?
2. What is the shared input to both approaches?
3. Where exactly does the existing approach fail? (Name the specific step or assumption.)
4. Where exactly does the proposed approach succeed? (Name the corresponding step.)
5. What structural element is different between the two? (Not just "ours is better" — what specific mechanism differs?)
6. Are there components shared between both approaches? (These should be visually identical.)

#### Taxonomy / Classification Questions

1. What is being classified? (Papers? Techniques? Systems?)
2. What are the axes or dimensions of classification?
3. Which quadrant/category/branch does this paper occupy?
4. Is the key insight that this paper fills an **empty quadrant** or creates a **new branch**?
5. What specific prior works go in each category? (Name them — "Work A [citation]".)
6. Is this a 2x2 matrix, a hierarchical tree, or a Venn diagram?

#### Deployment / System Diagram Questions

1. What is the deployment environment? (Cloud, edge, campus network, ISP backbone, etc.)
2. What are the infrastructure layers? (Client → Edge → Core → Cloud)
3. What components exist at each layer?
4. What are the network connections? Distinguish data plane from control plane.
5. Are there replication factors, scale indicators, or trust boundaries to show?
6. Where does the paper's system sit in this deployment? (Which component is "ours"?)

### Step 3: Generate the Figure Spec

Read `figure_templates/figure_spec_template.md`. Fill in every field from the student's answers:

1. **Identity section**: figure ID, section, placement, archetype, backend.
2. **Purpose section**: copy the claim from `project_context.md` verbatim. Write the "what it shows" and "why it exists" from the student's answers.
3. **Content section**: build the Components, Connections, and Groupings tables from the archetype-specific answers.
4. **Layout section**: flow direction, hierarchy levels, symmetry constraints, size target (from `figure_templates/venue_styles.md`).
5. **Styling section**: assign colors from the Paul Tol palette based on semantic roles. Note which component gets emphasis.
6. **For AI backend**: assemble the generation prompt using the template from `figure_templates/prompt_templates.md`. Fill all placeholders. Append the styling block from `venue_styles.md`.
7. **For TikZ backend**: note which skeleton from `figure_templates/tikz_skeletons.md` to start from.
8. **Caption**: draft an interpretive caption following voice_profile.md rules — claim-first, states the takeaway.

Save the completed spec as `figure_spec_[fig_id].md` in the paper's `figures/` directory (create the directory if needed).

Tell the student: "Figure spec saved to `figures/figure_spec_[fig_id].md`. Run `/paper-writing figure generate` to produce the figure."

---

## Mode 2: Generate — "Produce the figure"

### Step 1: Read the Figure Spec

Load `figures/figure_spec_[fig_id].md`. Verify all required fields are populated. If any are missing, return to spec mode for that field.

### Step 2: Route by Backend

#### Manual Or Local Figure Path

1. Read the assembled prompt from the spec's "Generation prompt" field.
2. Do not call external image-generation APIs or check for image API keys from this skill.
3. Prefer reproducible local figure creation with TikZ, matplotlib, PowerPoint shapes, or a user-provided drawing tool.
4. If an AI image prompt is useful, present the prompt text only and let the user decide whether to use an external service.
5. After the user provides a generated image or a local draft, proceed to critique mode.

**Iteration**: If the first result is unsatisfactory, refine the prompt:
- Be more specific about spatial layout ("component A is directly above component B, connected by a downward arrow")
- Add negative instructions ("do NOT show component X as a circle, use a rectangle")
- Adjust emphasis ("make the contribution component 1.5x larger than the others")
- Cap at 3 prompt iterations before suggesting manual refinement in a drawing tool.

#### TikZ Path

1. Read the archetype from the spec. Load the corresponding skeleton from `figure_templates/tikz_skeletons.md`.
2. Customize the skeleton:
   - Replace placeholder nodes with the actual components from the spec.
   - Set colors from the spec's color mapping.
   - Adjust layout (node distances, positioning) to fit the actual component count.
   - Add all connections, groupings, and annotations from the spec.
   - Set the figure width to match the venue target from `figure_templates/venue_styles.md`.
3. Write the TikZ code to `figures/fig_[short_id].tex`.
4. **Compile** (if `pdflatex` is available):
   ```bash
   cd figures && pdflatex -interaction=nonstopmode fig_[short_id].tex
   ```
   - If compilation fails, read the error log, fix the TikZ code, and retry (max 3 attempts).
   - If compilation succeeds, display the PDF for the student to review.
5. **If `pdflatex` is not available:**
   - Present the TikZ code to the student.
   - Instruct them to compile in Overleaf or their local TeX installation.

### Step 3: Update the Spec

After generation, update the `figure_spec.md`:
- Set "Generated: yes" with today's date
- For TikZ: record the source file path
- For AI: save the successful prompt version and the output image path

Tell the student: "Figure generated. Run `/paper-writing figure critique` to review it against your paper's claims and venue standards."

---

## Mode 3: Critique — "Does this figure serve the paper?"

### Step 1: Load Context

Read all of:
- The `figure_spec.md` for this figure
- The generated figure (image or compiled PDF)
- The paper's `project_context.md`
- `figure_templates/venue_styles.md` for formatting standards

### Step 2: Run Five Checks

#### Check 1: Claim Alignment

- Does the figure support the specific claim listed in the spec's "Paper claim supported" field?
- Could a reader understand the claim from the figure alone (with caption)?
- Does the figure show anything that contradicts or weakens the claim?
- **Verdict**: PASS / REVISE (with specific fix)

#### Check 2: Completeness

- Are all components from the spec present in the figure?
- Are all connections shown?
- Are all groupings visible?
- Are labels legible and correctly spelled?
- Is the key contribution component visually prominent?
- **Verdict**: PASS / REVISE (list missing elements)

#### Check 3: Venue Formatting

- Does the figure fit the target column width without rescaling below legibility?
- Is text at least 8pt at print size?
- Is the background white?
- Are colors from the approved palette?
- Would the figure be readable in grayscale?
- **Verdict**: PASS / REVISE (list violations)

#### Check 4: Design Principles

- **Data-ink ratio** (Tufte): Is every visual element encoding information? Remove decorative borders, background fills, and chrome that don't carry meaning.
- **Self-containment**: Can a reader understand the high-level flow without reading the paper body?
- **Simplicity**: Could any component be removed without losing information? If yes, remove it.
- **Consistency**: Does the style match other figures in this paper? (Same fonts, colors, line weights, node shapes.)
- **Verdict**: PASS / REVISE (list violations)

#### Check 5: Caption Quality

- Is the caption interpretive (states what the figure shows and why it matters)?
- Is it claim-first (the takeaway leads, details follow)?
- Does it follow voice_profile.md rules (no hedging, no filler adjectives, active voice)?
- Is it self-contained enough for a skim-reader?
- **Verdict**: PASS / REVISE (suggest rewrite)

### Step 3: Produce Critique Report

Present results as a table:

| Check | Verdict | Details |
|-------|---------|---------|
| Claim alignment | PASS/REVISE | ... |
| Completeness | PASS/REVISE | ... |
| Venue formatting | PASS/REVISE | ... |
| Design principles | PASS/REVISE | ... |
| Caption quality | PASS/REVISE | ... |

**Overall verdict:**
- **PASS** — all checks pass. The figure is ready for inclusion.
- **REVISE** — one or more checks failed. List the specific action items and suggest re-running generate mode with updated spec/prompt.

### Step 4: Update the Spec

After critique, update the `figure_spec.md`:
- Set "Critique passed: yes/no"
- Record iteration notes (what needs to change for the next version)

---

## Cross-Figure Consistency

When a paper has multiple non-data figures, enforce consistency across all of them:

1. **Color semantics**: If blue represents "our system" in Figure 1, it must represent "our system" in all figures. Document the color-to-meaning mapping in the first `figure_spec.md` and reference it from all others.
2. **Node shapes**: Consistent shape vocabulary across figures (rectangles for processing stages, cylinders for data stores, diamonds for decision points).
3. **Font and line weight**: Identical across all figures — use the shared styles from `venue_styles.md`.
4. **Naming**: The same component must have the same label in every figure. If the architecture overview calls it "Event Encoder," the component detail figure must also call it "Event Encoder."
5. **Level of detail**: Figures at the same level of abstraction should have similar visual complexity. An architecture overview shouldn't be more detailed than a component detail figure.

When critiquing any figure after the first, check consistency against all previously critiqued figures.

---

## Integration with the Paper Pipeline

This guide connects to the paper-writing pipeline at three points:

**Stage 2 (Architecture):** When building the section architecture table, classify each figure from "Key Figures Needed" as data (→ `/viz`) or non-data (→ spec mode here). Run spec mode for all non-data figures during this stage.

**Stage 3 (Section Drafts):** When drafting the Design section, the architecture overview figure should already exist. Design Move 3 (Component Architecture) uses it as structural scaffolding — each subsection corresponds to a component in the overview figure. If the figure doesn't exist yet, generate it before drafting.

**Stage 4 (Integration):** During the cross-section consistency pass, run critique mode on all non-data figures. Check visual balance, claim alignment, and cross-figure consistency.
