\# Change Log



All notable changes to this project will be documented in this file.



\## \[2026-02-15] - Complete Assignment 05 Submission



\### Added

\- \*\*Mermaid Flowchart\*\*: Generated process.mmd from SOP.md using Gemini CLI

&nbsp; - Exported to process.svg (57,657 bytes)

&nbsp; - Visualizes complete literature review workflow with decision points

\- \*\*BPMN Diagram\*\*: Generated process.bpmn from SOP.md using Gemini CLI

&nbsp; - Exported to process.png (128,782 bytes)  

&nbsp; - Formal business process representation in BPMN 2.0 standard

\- \*\*Glossary\*\*: Created comprehensive data dictionary with 15+ key terms

\- \*\*Prompt Log\*\*: Documented all CLI interactions with timestamps, prompts, outputs, and edits

\- \*\*Generation Scripts\*\*: 

&nbsp; - generate\_mermaid.py - Automated Mermaid diagram generation

&nbsp; - generate\_bpmn.py - Automated BPMN XML generation

&nbsp; - test\_gemini.py - API connectivity validation



\### Tools Configured

\- Google Gemini CLI (gemini-2.5-flash model)

\- Mermaid CLI (@mermaid-js/mermaid-cli) for SVG export

\- bpmn.io web editor for BPMN visualization and PNG export

\- Python libraries: google-genai, docx2txt



\### Files Structure

```

SOP-Assign05-Repo/

├── SOP.md (source of truth - converted from v1 Word doc)

├── SOP.docx (original backup)

├── CHANGELOG.md (this file)

├── README.md (project documentation)

├── glossary.md (terminology reference)

├── diagrams/

│   ├── mermaid/

│   │   ├── process.mmd (source)

│   │   └── process.svg (generated)

│   └── bpmn/

│       ├── process.bpmn (source)

│       └── process.png (generated)

└── prompt-log/

&nbsp;   └── week05-cli-log.md (CLI interaction log)

```



\## \[2026-02-15] - Initial Setup



\### Added

\- Created project folder structure (diagrams/, artifacts/, prompt-log/)

\- Added SOP v1: "Systematic Literature Review for Dissertation Research"

\- Created empty files: glossary.md, .gitignore

\- Initialized Git repository and pushed to GitHub



\### Source Files

\- SOP.md - Source of truth (converted from SOP\_v1\_Literature\_Review.docx)

\- SOP.docx - Original Word document backup

