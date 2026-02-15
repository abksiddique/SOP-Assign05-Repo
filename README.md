\# SOP Documentation Package - Assignment 05



\*\*Process Documentation with AI-Assisted CLI Workflow\*\*



Author: Siddique Abubakr Muntaka  

Course: AI for SOPs  

Date: February 15, 2026  

Repository: https://github.com/abksiddique/SOP-Assign05-Repo



---



\## Table of Contents

\- \[Project Overview](#project-overview)

\- \[Folder Structure](#folder-structure)

\- \[Quick Start](#quick-start)

\- \[How to Regenerate Artifacts](#how-to-regenerate-artifacts)

\- \[Source vs Generated Files](#source-vs-generated-files)

\- \[Version History](#version-history)

\- \[Tools Required](#tools-required)



---



\## Project Overview



This repository contains a complete documentation package for a \*\*Systematic Literature Review Process\*\* used in dissertation research on anonymous communication networks. The project demonstrates:



\- \*\*Repeatable CLI workflow\*\* using AI tools (Gemini CLI)

\- \*\*Version-controlled documentation\*\* with Git

\- \*\*Multiple diagram formats\*\* (Mermaid flowchart + BPMN process model)

\- \*\*Complete audit trail\*\* via prompt logs



\*\*Why This Matters:\*\*  

Documentation that can't be regenerated from source will decay over time. This project ensures anyone can reproduce all artifacts from the source SOP using documented CLI commands.



---



\## Folder Structure

```

SOP-Assign05-Repo/

│

├── README.md                    ← You are here

├── SOP.md                       ← SOURCE OF TRUTH (Markdown format)

├── SOP.docx                     ← Original Word document (backup)

├── CHANGELOG.md                 ← Version history and changes

├── glossary.md                  ← Key terms and data dictionary

├── .gitignore                   ← Git exclusions (protects .env)

│

├── diagrams/                    ← All visual process models

│   ├── mermaid/

│   │   ├── process.mmd         ← SOURCE (Mermaid flowchart code)

│   │   └── process.svg         ← GENERATED (visual diagram)

│   └── bpmn/

│       ├── process.bpmn        ← SOURCE (BPMN 2.0 XML)

│       └── process.png         ← GENERATED (visual diagram)

│

├── artifacts/                   ← Supporting documents

│   ├── screenshots/

│   └── examples/

│

└── prompt-log/                  ← CLI interaction logs

&nbsp;   └── week05-cli-log.md       ← Complete prompt history

```



\*\*Navigation Tips:\*\*

\- \*\*Start here\*\*: README.md (this file)

\- \*\*Process details\*\*: SOP.md

\- \*\*Visual workflows\*\*: diagrams/ folder

\- \*\*Change history\*\*: CHANGELOG.md

\- \*\*CLI evidence\*\*: prompt-log/week05-cli-log.md



---



\## Quick Start



\### Prerequisites

\- Python 3.x with pip

\- Node.js with npm

\- Git

\- Google Gemini API key (free tier)



\### Installation

```bash

\# Clone repository

git clone https://github.com/abksiddique/SOP-Assign05-Repo.git

cd SOP-Assign05-Repo



\# Install Python dependencies

pip install google-genai docx2txt



\# Install Mermaid CLI (for diagram generation)

npm install -g @mermaid-js/mermaid-cli



\# Configure API key (create .env file)

echo "GEMINI\_API\_KEY=your\_key\_here" > .env

```



\### View Existing Diagrams

```bash

\# Open Mermaid flowchart

start diagrams/mermaid/process.svg



\# Open BPMN diagram

start diagrams/bpmn/process.png

```



---



\## How to Regenerate Artifacts



All diagrams can be regenerated from `SOP.md` using these commands:



\### Regenerate Mermaid Flowchart

```bash

\# 1. Generate Mermaid code from SOP

python generate\_mermaid.py



\# 2. Convert to SVG image

mmdc -i diagrams/mermaid/process.mmd -o diagrams/mermaid/process.svg



\# 3. View result

start diagrams/mermaid/process.svg

```



\*\*What it does:\*\*

\- Reads SOP.md content

\- Uses Gemini CLI to generate Mermaid flowchart syntax

\- Exports flowchart as SVG image



\### Regenerate BPMN Diagram

```bash

\# 1. Generate BPMN XML from SOP

python generate\_bpmn.py



\# 2. Open in BPMN editor and export

\# - Go to https://bpmn.io/

\# - Click "Open" → select diagrams/bpmn/process.bpmn

\# - Review diagram

\# - Export → Export as PNG → save as process.png



\# 3. Move PNG to project

move Downloads/process.png diagrams/bpmn/process.png

```



\*\*What it does:\*\*

\- Reads SOP.md content

\- Uses Gemini CLI to generate BPMN 2.0 XML

\- Manual step: Use bpmn.io to visualize and export PNG



\### Test Gemini Connection

```bash

\# Verify API key works

python test\_gemini.py

```



---



\## Source vs Generated Files



\### SOURCE FILES (Edit These)

These are the source of truth - edit these directly:



\- ✏️ \*\*SOP.md\*\* - Process documentation (Markdown)

\- ✏️ \*\*SOP.docx\*\* - Original Word format (backup)

\- ✏️ \*\*diagrams/mermaid/process.mmd\*\* - Mermaid flowchart code

\- ✏️ \*\*diagrams/bpmn/process.bpmn\*\* - BPMN XML code

\- ✏️ \*\*glossary.md\*\* - Terminology definitions

\- ✏️ \*\*CHANGELOG.md\*\* - Version history



\### GENERATED FILES (Don't Edit - Regenerate Instead)

These are created from source files:



\- 🤖 \*\*diagrams/mermaid/process.svg\*\* - Generated from process.mmd

\- 🤖 \*\*diagrams/bpmn/process.png\*\* - Generated from process.bpmn



\*\*Rule:\*\* If you edit SOP.md, regenerate the diagrams using the commands above.



---



\## Version History



See \[CHANGELOG.md](CHANGELOG.md) for detailed version history.



\*\*Current Version:\*\* v1 (February 15, 2026)

\- Complete Mermaid and BPMN diagrams

\- Full glossary with 15+ terms

\- Documented CLI workflow in prompt log



\*\*Previous Version:\*\* v0 (Initial SOP)

\- 32 improvements documented in Change\_Log.docx



---



\## Tools Required



| Tool | Purpose | Install Command |

|------|---------|----------------|

| \*\*Python 3.x\*\* | Run generation scripts | \[python.org](https://python.org) |

| \*\*google-genai\*\* | Gemini CLI library | `pip install google-genai` |

| \*\*docx2txt\*\* | Word to Markdown conversion | `pip install docx2txt` |

| \*\*Node.js\*\* | JavaScript runtime | \[nodejs.org](https://nodejs.org) |

| \*\*@mermaid-js/mermaid-cli\*\* | Mermaid diagram export | `npm install -g @mermaid-js/mermaid-cli` |

| \*\*Git\*\* | Version control | \[git-scm.com](https://git-scm.com) |

| \*\*bpmn.io\*\* | BPMN visualization | \[bpmn.io](https://bpmn.io) (web-based, no install) |



---



\## Contact \& Support



\*\*Author:\*\* Siddique Abubakr Muntaka  

\*\*Institution:\*\* University of Cincinnati  

\*\*Research Focus:\*\* Anonymous Communication Networks (I2P)



\*\*Questions?\*\* See prompt-log/week05-cli-log.md for detailed CLI workflow examples.



---



\## License



This documentation is for academic purposes as part of coursework for "AI for SOPs" course.

