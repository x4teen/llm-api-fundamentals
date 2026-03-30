from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

class CostTracker:
    # Claude claude-opus-4-5 pricing (per 1M tokens)
    INPUT_COST_PER_M  = 3.00   # $3.00 per 1M input tokens
    OUTPUT_COST_PER_M = 15.00  # $15.00 per 1M output tokens

    def __init__(self):
        self.total_input_tokens  = 0
        self.total_output_tokens = 0
        self.total_cost_usd      = 0.0
        self.call_count          = 0

    def record(self, response):
        input_tokens  = response.usage.input_tokens
        output_tokens = response.usage.output_tokens

        # Calculate cost for this single call
        call_cost = (
            (input_tokens  / 1_000_000) * self.INPUT_COST_PER_M +
            (output_tokens / 1_000_000) * self.OUTPUT_COST_PER_M
        )

        # Accumulate running totals
        self.total_input_tokens  += input_tokens
        self.total_output_tokens += output_tokens
        self.total_cost_usd      += call_cost
        self.call_count          += 1

        print(f"Call #{self.call_count}: "
              f"in={input_tokens}, out={output_tokens}, "
              f"cost=${call_cost:.5f}")

    def summary(self):
        print(f"\n── Daily Summary ───────────────────────")
        print(f"Total calls        : {self.call_count}")
        print(f"Total input tokens : {self.total_input_tokens:,}")
        print(f"Total output tokens: {self.total_output_tokens:,}")
        print(f"Total cost         : ${self.total_cost_usd:.4f}")
        print(f"────────────────────────────────────────")


# ── Usage ────────────────────────────────────────────────────
tracker = CostTracker()

questions = [
    "How do I reset my VPN?",
    "My laptop won't connect to Wi-Fi.",
    "How do I request a new monitor?"
]

for q in questions:
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=512,
        temperature=0.0,
        system="You are an IT helpdesk assistant.",
        messages=[{"role": "user", "content": q}]
    )
    tracker.record(response)

tracker.summary()