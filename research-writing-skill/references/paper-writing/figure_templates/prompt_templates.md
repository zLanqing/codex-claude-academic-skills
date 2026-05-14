# AI Image Generation Prompt Templates

These templates produce prompts for Gemini, DALL-E, or other image generation models. Each template has a **skeleton** (the structure with placeholders) and **assembly instructions** (how to fill it from a `figure_spec.md`).

The AI prompt styling block from `venue_styles.md` is appended to every prompt automatically. Do not duplicate styling instructions inside the archetype-specific content.

---

## Architecture Overview

**When to use:** Full system pipeline showing end-to-end data flow through named stages. Typically the first figure in the Design section, spanning full page width.

**Skeleton:**

```
Create a clean, professional architecture diagram for a systems research paper.

SYSTEM NAME: {{system_name}}

OVERALL FLOW: {{flow_direction — e.g., "left to right" or "top to bottom"}}

COMPONENTS (in order of data flow):
{{for each component in figure_spec.components:}}
- [{{component.label}}]: {{component.description}}. Shape: {{component.shape}}. Color: {{component.color}}.
{{end for}}

DATA FLOW CONNECTIONS:
{{for each connection in figure_spec.connections:}}
- {{connection.from}} → {{connection.to}}: "{{connection.label}}" ({{connection.style}} arrow)
{{end for}}

GROUPINGS (draw dashed boundary boxes around these sets):
{{for each group in figure_spec.groupings:}}
- "{{group.label}}": contains [{{group.contains}}]
{{end for}}

KEY CONTRIBUTION: The component [{{emphasis_component}}] is the paper's main contribution — make it visually prominent (thicker border, slightly larger, brighter color).

ANNOTATIONS:
{{for each annotation in figure_spec.annotations:}}
- {{annotation}}
{{end for}}

SIZE: {{width}} inches wide, suitable for a two-column academic paper (full-width figure).

{{VENUE_STYLING_BLOCK from venue_styles.md}}
```

**Assembly instructions:**
1. Read the figure_spec.md's Components, Connections, and Groupings tables
2. Identify which component is the key contribution (from the Styling → Emphasis field)
3. Set flow direction from Layout → Flow direction
4. Set width from Layout → Size target (typically 7.0in for architecture overview)
5. Append the AI prompt styling block from `venue_styles.md`

---

## Concept Illustration

**When to use:** Making an abstract concept concrete through visual metaphor, before/after comparison, or spatial analogy. Typically in Background or Motivation sections.

**Skeleton:**

```
Create a concept illustration for a systems research paper.

CONCEPT: {{concept_name}}

ILLUSTRATION TYPE: {{one of: before_after | spatial_analogy | visual_metaphor | process_contrast}}

{{if before_after:}}
LEFT PANEL ("Before" / "Problem"):
- Title: "{{before_title}}"
- Show: {{description of the problematic state}}
- Visual elements: {{what to draw — e.g., "scattered points with no structure, arrows pointing in random directions"}}
- Color: use red (#EE6677) and grey (#BBBBBB) to convey the problem

RIGHT PANEL ("After" / "Solution"):
- Title: "{{after_title}}"
- Show: {{description of the improved state}}
- Visual elements: {{what to draw — e.g., "organized clusters with clear boundaries, arrows aligned"}}
- Color: use blue (#4477AA) and green (#228833) to convey the solution

DIVIDING ELEMENT: {{arrow, vertical line, or transformation symbol between panels}}
{{end if}}

{{if spatial_analogy:}}
SPACE: {{describe the conceptual space — e.g., "2D embedding space"}}
ELEMENTS IN SPACE:
{{list of elements and their spatial positions/relationships}}
KEY INSIGHT: {{what the spatial arrangement reveals — e.g., "similar items cluster, dissimilar items separate"}}
{{end if}}

{{if visual_metaphor:}}
METAPHOR: {{the analogy — e.g., "funnel" for progressive filtering, "bridge" for connecting domains}}
CONCRETE MAPPING:
- {{metaphor element 1}} represents {{technical concept 1}}
- {{metaphor element 2}} represents {{technical concept 2}}
AVOID: Do not make the metaphor cartoonish. Keep it abstract and geometric.
{{end if}}

{{if process_contrast:}}
TOP ROW ("Existing Approach"):
- Steps: {{step 1}} → {{step 2}} → {{step 3}}
- Outcome: {{what goes wrong}}
- Mark the failure point with a red X or broken arrow

BOTTOM ROW ("Our Approach"):
- Steps: {{step 1}} → {{step 2}} → {{step 3}}
- Outcome: {{what succeeds}}
- Mark the success with a green checkmark

ALIGNMENT: Both rows should be horizontally aligned so the reader can compare step-by-step.
{{end if}}

SIZE: {{width}} inches wide.

{{VENUE_STYLING_BLOCK from venue_styles.md}}
```

**Assembly instructions:**
1. Determine the illustration type from figure_spec.md's Content section
2. Fill in the appropriate conditional block
3. For before/after: the "before" state should match the Problem Gap from `project_context.md`; the "after" state should match the key contribution
4. Keep the illustration abstract and geometric — no realistic imagery

---

## Comparison Schematic

**When to use:** Side-by-side showing why the existing approach fails and the proposed approach works. Motivation or design justification sections.

**Skeleton:**

```
Create a comparison diagram for a systems research paper showing two approaches side by side.

LEFT SIDE — "{{existing_approach_name}}" (the limitation):
- Components: {{list of components in the existing approach}}
- Data flow: {{how data moves through the existing approach}}
- FAILURE POINT: {{where and why it breaks — mark with red (#EE6677)}}
- Label: "{{short failure description — e.g., 'Misses bursty patterns'}}"

RIGHT SIDE — "{{proposed_approach_name}}" (the solution):
- Components: {{list of components in the proposed approach}}
- Data flow: {{how data moves through the proposed approach}}
- SUCCESS POINT: {{where the improvement happens — mark with green (#228833)}}
- Label: "{{short success description — e.g., 'Captures event boundaries'}}"

SHARED ELEMENTS:
- Both sides receive the same input: {{input description}}
- Both sides produce: {{output description}}
- Align shared elements horizontally so the structural difference is immediately visible

VISUAL CUES:
- Use a vertical dividing line or "vs." marker between the two sides
- Matching components (same in both approaches) should have the same position and grey color
- Differing components should be highlighted in their respective colors (red for problem, blue/green for solution)

SIZE: {{width}} inches wide (typically full-width for maximum clarity).

{{VENUE_STYLING_BLOCK from venue_styles.md}}
```

**Assembly instructions:**
1. The left side comes from the Problem Gap in `project_context.md` — the structural limitation of existing work
2. The right side comes from the key contribution — the insight that fixes the limitation
3. Shared elements should be visually identical to emphasize that the difference is surgical, not wholesale

---

## Deployment / System Diagram

**When to use:** Physical or logical arrangement of infrastructure components. Systems evaluation or background sections showing how the system is deployed in practice.

**Skeleton:**

```
Create a system deployment diagram for a systems/networking research paper.

DEPLOYMENT CONTEXT: {{e.g., "distributed measurement infrastructure" or "cloud-edge pipeline"}}

INFRASTRUCTURE LAYERS (top to bottom or left to right):
{{for each layer:}}
### {{layer_name}} (e.g., "Client tier", "Edge tier", "Cloud tier")
Components:
{{for each component in layer:}}
- [{{component.label}}]: {{component.description}}. Icon style: {{server / database / router / switch / cloud / mobile / container}}.
{{end for}}
{{end for}}

NETWORK CONNECTIONS:
{{for each connection:}}
- {{from}} ↔ {{to}}: {{protocol or description}} ({{style: solid for data plane, dashed for control plane}})
{{end for}}

ANNOTATIONS:
- Latency/bandwidth labels on key links: {{list}}
- Replication indicators: {{e.g., "×3 replicas" near a database component}}
- Trust boundaries: {{dashed boxes separating trusted from untrusted zones}}

SCALE INDICATORS: {{e.g., "N clients", "K edge nodes"}}

SIZE: {{width}} inches wide.

{{VENUE_STYLING_BLOCK from venue_styles.md}}
```

**Assembly instructions:**
1. Identify the deployment topology from `project_context.md` or the Design section outline
2. Use standard infrastructure icon styles (box=server, cylinder=database, cloud shape=cloud service, diamond=router)
3. Distinguish data plane (solid) from control plane (dashed) connections
4. Mark the paper's contribution within the deployment (thicker border, brighter color)

---

## Assembling the Final Prompt

When Claude runs generate mode, it:

1. Reads the `figure_spec.md` for the target figure
2. Selects the matching archetype template from this file
3. Fills in all `{{placeholders}}` from the spec
4. Appends the AI prompt styling block from `venue_styles.md`
5. Presents the assembled prompt to the student

The student can then:
- Paste the prompt into Gemini (recommended: `gemini-2.5-flash-image` or later)
- Paste into DALL-E or another image generation tool
- Use the prompt as a brief for manual creation in Figma, draw.io, or Inkscape
- Run it through a local script if they have API access configured

If the student has a Gemini API key available, Claude can generate the figure directly by running a Python script:

```python
# Requires: pip install google-genai
from google import genai
client = genai.Client()
response = client.models.generate_images(
    model="gemini-2.0-flash-exp",  # or latest image-capable model
    prompt=assembled_prompt,
    config=genai.types.GenerateImagesConfig(number_of_images=1)
)
# Save the image
response.generated_images[0].image.save("figures/fig_name.png")
```
