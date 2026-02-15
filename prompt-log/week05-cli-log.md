\# Week 05 CLI Prompt Log



\## Tool \& Environment

\- \*\*Tool\*\*: Google Gemini CLI (google-genai Python library)

\- \*\*Model\*\*: gemini-2.5-flash

\- \*\*Date\*\*: 2026-02-15

\- \*\*Repository\*\*: SOP-Assign05-Repo (main branch)



---



\## Session 1: Generate Mermaid Flowchart



\### Goal

Generate a Mermaid flowchart diagram from SOP.md that visualizes the literature review process.



\### Input Files

\- SOP.md (Systematic Literature Review for Dissertation Research)



\### Timestamp

2026-02-15 \[Current Time]



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



\### Output

\[Will be added after generation]



\### Validation

\[Will be documented after review]



\### Edits Made

\[Will be documented after manual corrections]

