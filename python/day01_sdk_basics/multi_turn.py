import anthropic
from dotenv import load_dotenv          # Import the load_dotenv function from the dotenv library

load_dotenv()  # Load environment variables from .env file (Anthropic API key should be stored in the .env file as ANTHROPIC_API_KEY)

# Create an instance of the Anthropics client with the API key loaded from the environment variable
client = anthropic.Client()
system_prompt = """You are an IT helpdesk assistant for Acme Corp.
    - Only answer IT-related questions
    - Always ask for the user's employee ID before helping
    - Never discuss competitor products"""

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=512,
    system=system_prompt,   
    messages=[
        {"role": "user", "content": "My laptop won't turn on."}
    ]
)

messages = []

# ── Turn 1 ──────────────────────────────────────────
messages.append({"role": "user", "content": "My laptop won't turn on."})

response = client.messages.create(
    model="claude-opus-4-5", max_tokens=256,
    messages=messages
)
# Claude sees: [user: "My laptop won't turn on."]
# Claude replies: "Let's troubleshoot. Is the charging light on?"

messages.append({"role": "assistant", "content": response.content[0].text})

# messages is now:
# [
#   {role: user,      "My laptop won't turn on."},
#   {role: assistant, "Let's troubleshoot. Is the charging light on?"}
# ]

# ── Turn 2 ──────────────────────────────────────────
messages.append({"role": "user", "content": "No light at all."})

response = client.messages.create(
    model="claude-opus-4-5", max_tokens=256,
    system=system_prompt,   # ← user never sees this
    messages=messages
)
# Claude sees the FULL transcript — all 3 messages
# Claude replies: "Try a different power cable..."

messages.append({"role": "assistant", "content": response.content[0].text})

# messages is now:
# [
#   {role: user,      "My laptop won't turn on."},
#   {role: assistant, "Let's troubleshoot. Is the charging light on?"},
#   {role: user,      "No light at all."},
#   {role: assistant, "Try a different power cable..."}
# ]

# ── Turn 3 ──────────────────────────────────────────
messages.append({"role": "user", "content": "I tried a new cable, still nothing."})
# Claude now has full context of everything said so far
response = client.messages.create(
    model="claude-opus-4-5", max_tokens=256,
    system=system_prompt,   # ← user never sees this
    messages=messages
)
messages.append({"role": "assistant", "content": response.content[0].text})

# ── Turn 4 ──────────────────────────────────────────
# Out of scope for this example, but you could keep going as long as you want! Just keep appending to the messages list and sending the full transcript each time.
messages.append({"role": "user", "content": "Can you write me a poem about my stupid laptop?"})
# Claude now has full context of everything said so far
response = client.messages.create(
    model="claude-opus-4-5", max_tokens=256,
    system=system_prompt,   # ← user never sees this
    messages=messages
)
messages.append({"role": "assistant", "content": response.content[0].text})

# ── Turn 5 ──────────────────────────────────────────
# Out of scope for this example, with temperature control.
messages.append({"role": "user", "content": "How is the weather in Chicago today?"})
# Claude now has full context of everything said so far
response = client.messages.create(
    model="claude-opus-4-5", max_tokens=256,
    temperature=0.0,   # Adjust the temperature strict replies, 0.0 is the most strict, 1.0 is the most creative
    system=system_prompt,   # ← user never sees this
    messages=messages
)
messages.append({"role": "assistant", "content": response.content[0].text})

# Print all the messages in the conversation so far
turn = 1
for message in messages:
    print(f"\n\n\n")
    print(f"── Turn {turn} ──────────────────────────────────────────")
    print(f"{message['role']}: {message['content']}")
    turn += 1

