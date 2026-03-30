from anthropic import Anthropic
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self, provider: str = "anthropic"):
        self.provider = provider
        if provider == "anthropic":
            self.client = Anthropic()
        elif provider == "openai":
            self.client = OpenAI()

    def chat(self, user_message: str, system: str = "You are a helpful assistant.") -> str:
        if self.provider == "anthropic":
            response = self.client.messages.create(
                model="claude-opus-4-5",
                max_tokens=1024,
                temperature=0.3,
                system=system,
                messages=[{"role": "user", "content": user_message}]
            )
            return response.content[0].text          # Anthropic format

        elif self.provider == "openai":
            response = self.client.chat.completions.create(
                model="gpt-4o",
                max_tokens=1024,
                temperature=0.3,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user_message}
                ]
            )
            return response.choices[0].message.content  # OpenAI format
        
# Example usage:
if __name__ == "__main__":
    llm_client = LLMClient(provider="anthropic")  # or provider="openai"
    answer = llm_client.chat("What is a JWT token?")
    print(answer) 