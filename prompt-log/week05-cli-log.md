# Week 05 CLI Prompt Log

## Tool & Environment
- **Tool**: Google Gemini CLI (google-genai Python library)
- **Model**: gemini-2.5-flash
- **Date**: 2026-02-15
- **Repository**: SOP-Assign05-Repo (main branch)

---

## Session 1: Generate Mermaid Flowchart

### Goal
Generate a Mermaid flowchart diagram from SOP.md that visualizes the literature review process.

### Input Files
- SOP.md (Systematic Literature Review for Dissertation Research)

### Timestamp
2026-02-15 [Current Time]

### Prompt
```
Read this SOP and generate a Mermaid flowchart (flowchart TD syntax).

Requirements:
- Include explicit Start and End nodes
- Every decision must have labeled branches (Yes/No or specific conditions)
- Use the exact step names from the SOP
- Do NOT invent steps - only use what's in the SOP
- If something is unclear, mark it as [TBD] in a note

[Full SOP content provided from SOP.md file]

Generate ONLY the Mermaid code, no explanations.
```

### Output
- File created: diagrams/mermaid/process.mmd (2,772 bytes)
- Diagram exported: diagrams/mermaid/process.svg (57,657 bytes)
- Successfully captured all 13 main steps plus exception handling flow
- Generated flowchart shows decision points for result count validation and institutional login process

### Validation Performed
Verified all steps from SOP are present in diagram
Checked that decision branches are properly labeled
Confirmed Start and End nodes are present
Visual review shows clear flow from research focus to PDF download

### Edits Made
- Removed markdown code fences (```mermaid and ```) from generated file to enable SVG export
- No content changes needed - AI accurately captured the SOP workflow

### Result
- Final files committed: process.mmd (source), process.svg (export)
- Diagram successfully visualizes the complete literature review process

---

## Session 2: Generate BPMN Diagram

### Goal
Generate a BPMN 2.0 XML diagram from SOP.md for formal business process documentation.

### Input Files
- SOP.md (Systematic Literature Review for Dissertation Research)

### Timestamp
2026-02-15 [Current Time]

### Prompt
```
Read this SOP and generate BPMN 2.0 XML code.

Requirements:
- Start event and end event required
- Use tasks for action steps
- Use gateways for decisions
- Use lanes ONLY if roles differ (all steps are by "Researcher" so use single lane)
- Do NOT invent systems or approvals not in the SOP
- Generate valid BPMN 2.0 XML

[Full SOP content provided from SOP.md file]

Generate ONLY the BPMN XML code, no explanations.
```

### Output
- File created: diagrams/bpmn/process.bpmn (18,489 bytes)
- Diagram exported via bpmn.io: diagrams/bpmn/process.png (128,782 bytes)
- Successfully generated valid BPMN 2.0 XML

### Validation Performed
Opened BPMN file in bpmn.io web editor
Verified diagram renders correctly
Checked all process steps are represented
Confirmed proper use of tasks and gateways

### Edits Made
- Removed XML code fences (```xml and ```) from generated file
- Manually exported PNG via bpmn.io interface
- No structural changes needed to BPMN XML

### Result
- Final files committed: process.bpmn (source), process.png (export)
- BPMN successfully represents literature review workflow in standard format