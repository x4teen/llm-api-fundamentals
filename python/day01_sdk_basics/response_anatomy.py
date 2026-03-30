import anthropic
from dotenv import load_dotenv          # Import the load_dotenv function from the dotenv library

load_dotenv()  # Load environment variables from .env file (Anthropic API key should be stored in the .env file as ANTHROPIC_API_KEY)

# Create an instance of the Anthropics client with the API key loaded from the environment variable
client = anthropic.Client()

# Make a call to the Anthropics API to create a message using the specified model, max tokens, system prompt, and user message
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=256,
    messages=[{"role": "user", "content": "Say hello in one sentence."}]
)

# Parse the response and print the text content of the first message in the response
print(response.id)  # Print the ID of the response
print(response.model)  # Print the model used for the response
print(response.role) # Print the role of the message in the response
print(response.content)  # Print content of the response
print(response.content[0].text)  # Print the text content of the first message in the response
print(response.stop_reason)  # Print the reason why the response generation stopped
print(response.usage.input_tokens)  # Print the number of input tokens used in the response
print(response.usage.output_tokens)  # Print the number of output tokens generated in the response