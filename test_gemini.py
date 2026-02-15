from google import genai
from google.genai import types

# Load API key from .env file
with open('.env', 'r') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY='):
            api_key = line.strip().split('=')[1]
            break

# Configure Gemini
client = genai.Client(api_key=api_key)

# Test with a simple prompt
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Say hello and confirm you are working!'
)

print("Gemini CLI is working!")
print("Response:", response.text)