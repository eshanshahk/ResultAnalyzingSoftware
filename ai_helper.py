import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path="D:/ML/.env")

# Create the OpenAI client with OpenRouter settings
client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Make a chat completion request to Claude 3 Haiku
response = client.chat.completions.create(
    model="anthropic/claude-3-haiku",
    messages=[
        {"role": "user", "content": "Hello Claude, what can you do?"}
    ]
)

# Print the response content
print(response.choices[0].message.content)