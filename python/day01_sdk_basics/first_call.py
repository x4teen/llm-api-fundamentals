import anthropic
from dotenv import load_dotenv          # Import the load_dotenv function from the dotenv library

load_dotenv()  # Load environment variables from .env file (Anthropic API key should be stored in the .env file as ANTHROPIC_API_KEY)

# Create an instance of the Anthropics client with the API key loaded from the environment variable
client = anthropic.Client()

# Make a call to the Anthropics API to create a message using the specified model, max tokens, system prompt, and user message
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    system="You are a helpful IT assistant.",
    messages=[
        {"role": "user", "content": "What is a JWT token?"}
    ])

# Parse the response and print the text content of the first message in the response
print(response.content[0].text)  # Print the text content of the first message in the response