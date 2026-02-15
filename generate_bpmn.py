from google import genai

# Load API key
with open('.env', 'r') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY='):
            api_key = line.strip().split('=')[1]
            break

# Read SOP
with open('SOP.md', 'r', encoding='utf-8') as f:
    sop_content = f.read()

# Configure Gemini
client = genai.Client(api_key=api_key)

# Prompt for BPMN generation
prompt = f"""Read this SOP and generate BPMN 2.0 XML code.

Requirements:
- Start event and end event required
- Use tasks for action steps
- Use gateways for decisions
- Use lanes ONLY if roles differ (all steps are by "Researcher" so use single lane)
- Do NOT invent systems or approvals not in the SOP
- Generate valid BPMN 2.0 XML

SOP Content:
{sop_content}

Generate ONLY the BPMN XML code, no explanations."""

# Generate
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)

# Save to file
output_file = 'diagrams/bpmn/process.bpmn'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(response.text)

print(f"BPMN diagram generated: {output_file}")
print(f"\nPreview (first 500 chars):\n{response.text[:500]}")