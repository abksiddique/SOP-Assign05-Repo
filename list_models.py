from google import genai

# Load API key from .env file
with open('.env', 'r') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY='):
            api_key = line.strip().split('=')[1]
            break

# Configure Gemini
client = genai.Client(api_key=api_key)

# List available models
print("Available models:")
for model in client.models.list():
    print(f"- {model.name}")