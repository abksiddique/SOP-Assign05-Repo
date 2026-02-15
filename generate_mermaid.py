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

# Prompt for Mermaid generation
prompt = f"""Read this SOP and generate a Mermaid flowchart (flowchart TD syntax).

Requirements:
- Include explicit Start and End nodes
- Every decision must have labeled branches (Yes/No or specific conditions)
- Use the exact step names from the SOP
- Do NOT invent steps - only use what's in the SOP
- If something is unclear, mark it as [TBD] in a note

SOP Content:
{sop_content}

Generate ONLY the Mermaid code, no explanations."""

# Generate
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)

# Save to file
output_file = 'diagrams/mermaid/process.mmd'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(response.text)

print(f"Mermaid diagram generated: {output_file}")
print(f"\nPreview (first 500 chars):\n{response.text[:500]}")