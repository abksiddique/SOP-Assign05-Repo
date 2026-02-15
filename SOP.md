STANDARD OPERATING PROCEDURE (SOP) v1

REFINED VERSION

Systematic Literature Review for Dissertation Research



Title: Literature Review Process for Dissertation Research on Anonymous Communication Networks

Author: Siddique Abubakr Muntaka

Changes from v0: 32 improvements documented in Change_Log.docx

KEY IMPROVEMENTS IN v1:

All 24 steps now explicitly name the actor (Researcher)

Screen-level cues added (button names, locations, colors)

Decision criteria made testable and observable

Validation checkpoints added after critical actions

File naming conventions specified

Exception recovery expanded to step-by-step procedures

1. PURPOSE

This SOP establishes a repeatable methodology for conducting literature reviews in cybersecurity research, specifically for identifying and cataloging academic papers on anonymous communication networks (Tor, I2P, Freenet) for dissertation research at the University of Cincinnati.

7. PROCEDURE - IMPROVED WITH SCREEN-LEVEL CUES

PHASE 1: Formulating Search Strategy

Step 1: The researcher identifies the research focus from the dissertation chapter outline

Action: Researcher reviews the dissertation chapter outline document and identifies a specific topic requiring literature coverage.

Example Output: 'Chapter 3 needs coverage of I2P traffic analysis methods published 2020-present.'

Time: 5 minutes

Step 2: The researcher extracts 3-5 primary keywords

Action: The researcher underlines nouns and technical terms in the research question.

Example Keywords: ['I2P', 'traffic analysis', 'network topology', 'security']

Validation: Each keyword should be searchable (not verbs or connectors).

Step 3: The researcher formulates a search query string

Action: The researcher combines keywords with spaces between terms.

Example: 'anonymous communication networks security'

PHASE 2: Executing Database Searches

Step 4: The researcher opens Google Scholar

Action: Researcher opens Chrome browser and navigates to scholar.google.com

Screen Cues: Google Scholar blue/white interface with search bar at top center.

Validation: Search bar displays placeholder text 'Stand on the shoulders of giants'.

Step 5: Researcher types search query and executes search

Action: Researcher types the search string from Step 3 into the Google Scholar search bar.

Action: Researcher presses Enter key OR clicks blue Search button (magnifying glass icon).

Screen Cues: Results page loads showing 'About X results' count in gray text below the search bar.

Step 6: The researcher applies a date filter

Action: Researcher locates the 'Any time' dropdown in the LEFT SIDEBAR under the search bar.

Action: Researcher clicks 'Any time' dropdown.

Action: Researcher selects 'Since 2020' option.

Action: Researcher clicks 'Apply' button (if present) OR selection auto-applies.

Validation: Results refresh, first page shows publication years ≥2020.

Step 7: The researcher verifies the appropriate result count

Action: The researcher reads the result count displayed below the search bar.

Decision Criteria:

• IF result count 100-5000: Acceptable range → Proceed to Step 8

• IF result count <100: Too narrow → Broaden search terms, return to Step 3

• IF result count >5000: Too broad → Add specificity, return to Step 3

Step 8: The researcher scans the first page for relevant papers

Action: Researcher scans titles of top 10 results on first page.

Relevance Criteria (Testable):

• IF title contains 2+ keywords from search query AND year ≥2020, flag as potentially relevant

• IF title contains 1 keyword OR unclear relevance, read snippet/abstract

• IF title contains 0 keywords, skip

Target: Identify 3-5 potentially relevant papers on first page.

PHASE 3: Accessing and Downloading Papers

Step 9: Researcher checks access type using visual indicators

Action: Researcher examines [PDF] link on right side of each Google Scholar result.

Visual Decision Criteria:

• IF [PDF] link is GREEN with no $ symbol: Open Access → Proceed to Step 10

• IF [PDF] link shows $ symbol OR says 'Get access': Paywall → Go to Step 11

• IF no [PDF] link, only [CITATION]: Not available → Skip paper

Step 10: Researcher opens paper page

Action: Researcher right-clicks on paper title (blue link).

Action: Researcher selects 'Open link in new tab' from context menu.

Validation: A new tab opens successfully, displaying the paper page.

Step 11: Researcher accesses UC institutional login (if paywalled)

Action: On database page (IEEE/ACM/Springer), Researcher locates 'Institutional Sign In' button (usually top right).

Action: Researcher clicks 'Institutional Sign In' button.

Action: Researcher enters UC credentials in 6+2 format (example: abubaksr26).

Action: Researcher clicks 'Login' button.

Validation: Page shows 'Authenticated as [username]' OR 'Download PDF' button becomes active (not grayed out).

If Login Fails: See Exception 1 recovery steps.

Step 12: Researcher downloads PDF file

Action: Researcher clicks 'Download PDF' button (label varies: 'Download Article', 'Get PDF', 'View PDF').

Action: PDF downloads to browser's Downloads folder OR opens in new tab.

Validation: Researcher checks Downloads folder and verifies file size >0 KB (not corrupted).

Step 13: Researcher saves PDF with standard naming convention

Action: Researcher moves PDF from Downloads to Assignment_02/Papers/ folder.

Action: Researcher renames file following convention: [FirstAuthor_Year_Topic].pdf

Example: Sun_2022_IoT_Security.pdf

Validation: Researcher opens PDF to confirm it displays correctly (not corrupted).

[Phases 4-6 continue with same level of detail: explicit actors, screen cues, validation checkpoints]

8. EXCEPTIONS - EXPANDED RECOVERY PROCEDURES

Exception 1: Paywall Access (EXPANDED)

Trigger: Paper shows $ symbol OR 'Get access' message, OR institutional login fails.

Recovery Steps:

1. Researcher clicks 'Institutional Sign In' button on database page

2. Researcher enters UC credentials (6-character username + 2-digit year)

3. Researcher clicks 'Login' button

4. Researcher validates 'Authenticated' message appears

5. IF login fails: Researcher checks VPN connection (must be on UC network or VPN)

6. IF still fails: Researcher verifies credential format is correct (6+2)

7. IF still fails: Researcher contacts advisor to arrange library access support

Escalation: If UC subscription doesn't cover database, discuss alternatives with advisor (ILL request, open access versions).

[Exceptions 2-8 similarly expanded with step-by-step recovery procedures]