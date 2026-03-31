import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

ticket = "My laptop is slow and sometimes freezes"

# ── Weak prompt ───────────────────────────────────────────────
weak_response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=512,
    temperature=0.3,
    system="You are a helpful IT assistant.",
    messages=[{"role": "user", "content": ticket}]
)

# ── Strong prompt ─────────────────────────────────────────────
strong_response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=512,
    temperature=0.0,
    system="""You are a Tier 1 IT support analyst.
Diagnose the issue and respond ONLY in this JSON format:
{
  "likely_causes": ["cause1", "cause2"],
  "immediate_steps": ["step1", "step2", "step3"],
  "priority": "P1 | P2 | P3",
  "escalate_to_tier2": true | false
}""",
    messages=[{"role": "user", "content": ticket}]
)

print("WEAK:\n",   weak_response.content[0].text)
print("\nSTRONG:\n", strong_response.content[0].text)