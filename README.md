# llm-api-fundamentals
Anthropic &amp; OpenAI SDK mastery, prompt engineering, Pydantic validation, and a Spring Boot REST wrapper — Phase 1 of 6 in an enterprise LLM customization roadmap.

# Phase 1: API & Prompt Engineering Foundations

> Part of the **LLM Customization for Enterprise** learning roadmap  
> 📅 Duration: 2 weeks &nbsp;|&nbsp; 🐍 Python + ☕ Java &nbsp;|&nbsp; ⏱ ~35–45 hours

---

## Overview

This repository contains all code, exercises, and the capstone project for **Phase 1** of the LLM Customization Plan. The goal is to master the Anthropic and OpenAI APIs, prompt engineering patterns, structured output, Pydantic validation, streaming, token/cost management, and a production-style Java Spring Boot wrapper.

By the end of Phase 1 you will have a deployable **Enterprise Q&A Bot** — a Python backend exposed via a Spring Boot REST API with authentication, rate limiting, and structured logging.

---

## Repository Structure

```
phase1-llm-foundations/
│
├── python/
│   ├── day01_sdk_basics/
│   │   ├── first_call.py               # Your first Anthropic API call
│   │   ├── response_anatomy.py         # Dissecting the response object
│   │   └── parameters_demo.py          # temperature, max_tokens, top_p, top_k
│   │
│   ├── day02_prompt_engineering/
│   │   ├── system_prompts.py           # System prompt patterns
│   │   ├── few_shot.py                 # Few-shot prompting examples
│   │   └── prompt_comparison.py        # Compare outputs across prompt designs
│   │
│   ├── day03_chain_of_thought/
│   │   ├── zero_shot_cot.py            # "Think step by step" pattern
│   │   ├── few_shot_cot.py             # Few-shot CoT with examples
│   │   └── cot_comparison.py           # With vs without CoT benchmark
│   │
│   ├── day04_openai_sdk/
│   │   ├── openai_basics.py            # OpenAI SDK basics
│   │   ├── provider_wrapper.py         # Provider-agnostic LLM client
│   │   └── azure_openai.py             # Azure OpenAI endpoint setup
│   │
│   ├── day05_structured_output/
│   │   ├── json_mode.py                # JSON mode prompt engineering
│   │   ├── tool_use_json.py            # Tool-use trick for structured output
│   │   └── safe_json_parser.py         # Retry logic on parse failure
│   │
│   ├── day06_pydantic/
│   │   ├── basic_models.py             # BaseModel, fields, validators
│   │   ├── schema_to_prompt.py         # Generate JSON schema → inject into prompt
│   │   ├── validated_pipeline.py       # Full validated LLM response pipeline
│   │   └── nested_models.py            # Complex multi-field response parsing
│   │
│   ├── day07_mini_project/
│   │   ├── qa_cli.py                   # Q&A CLI with Pydantic-validated output
│   │   └── tests/
│   │       └── test_llm_wrapper.py     # Unit tests with mocked API calls
│   │
│   ├── day08_streaming/
│   │   ├── streaming_basic.py          # Anthropic streaming API
│   │   ├── streaming_openai.py         # OpenAI streaming comparison
│   │   └── streaming_chatbot.py        # Real-time CLI chatbot
│   │
│   ├── day09_tokens_cost/
│   │   ├── tokenizer_demo.py           # Token counting before sending
│   │   ├── cost_tracker.py             # CostTracker class
│   │   └── pricing_reference.py        # Model pricing constants
│   │
│   └── capstone/
│       ├── system_prompt.txt           # Domain system prompt
│       ├── models.py                   # Pydantic response models
│       ├── pipeline.py                 # Full Q&A pipeline
│       ├── cost_logger.py              # Cost logging per call
│       └── tests/
│           └── test_pipeline.py        # Integration tests
│
├── java/
│   └── qa-bot-api/                     # Spring Boot 3.x project
│       ├── src/main/java/com/enterprise/qabot/
│       │   ├── QaBotApplication.java
│       │   ├── controller/
│       │   │   └── QaController.java   # POST /api/ask endpoint
│       │   ├── service/
│       │   │   └── ClaudeService.java  # Anthropic REST client (WebClient)
│       │   ├── model/
│       │   │   ├── AskRequest.java
│       │   │   └── AskResponse.java
│       │   ├── security/
│       │   │   └── SecurityConfig.java # Basic auth / JWT stub
│       │   └── config/
│       │       └── RateLimitConfig.java
│       ├── src/test/java/com/enterprise/qabot/
│       │   └── QaControllerIntegrationTest.java
│       ├── pom.xml
│       └── README.md
│
├── docs/
│   ├── study_plan.md                   # Full 14-day plan (reference)
│   ├── prompt_patterns.md              # Prompt engineering cheat sheet
│   └── cost_model.md                   # Token pricing and cost estimates
│
├── .env.example                        # Environment variable template
├── requirements.txt                    # Python dependencies
├── .gitignore
└── README.md                           # This file
```

---

## Quickstart

### Prerequisites

- Python 3.11+
- Java 21+ and Maven 3.9+
- An [Anthropic API key](https://console.anthropic.com/)
- An [OpenAI API key](https://platform.openai.com/) *(Day 4 onwards)*

### Python Setup

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/phase1-llm-foundations.git
cd phase1-llm-foundations

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your API keys
cp .env.example .env
# Edit .env and add your keys

# 5. Run your first script
python python/day01_sdk_basics/first_call.py
```

### Java Setup (Day 10+)

```bash
cd java/qa-bot-api
mvn spring-boot:run
# API will be available at http://localhost:8080
```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in your keys. **Never commit `.env` to Git.**

```bash
# .env.example
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=https://YOUR_RESOURCE.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

Load in Python with:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

## Python Dependencies

```text
# requirements.txt
anthropic>=0.25.0
openai>=1.30.0
pydantic>=2.7.0
python-dotenv>=1.0.0
tiktoken>=0.7.0
pytest>=8.2.0
pytest-mock>=3.14.0
```

---

## Phase 1 Skills Checklist

Track your progress as you work through each day:

| # | Skill | Day | Status |
|---|-------|-----|--------|
| 1 | Anthropic SDK — Messages API, response object, parameters | Day 1 | ⬜ |
| 2 | System prompts, few-shot prompting, prompt design patterns | Day 2 | ⬜ |
| 3 | Chain-of-thought prompting (zero-shot and few-shot) | Day 3 | ⬜ |
| 4 | OpenAI SDK, provider-agnostic wrapper, Azure endpoint | Day 4 | ⬜ |
| 5 | Structured output — JSON mode, tool-use trick, safe parsing | Day 5 | ⬜ |
| 6 | Pydantic models — validation, schema generation, retries | Day 6 | ⬜ |
| 7 | Streaming — SSE events, real-time CLI chatbot | Day 8 | ⬜ |
| 8 | Token counting, cost tracking, CostTracker class | Day 9 | ⬜ |
| 9 | Java Spring Boot wrapper — auth, rate limiting, logging | Day 10–11 | ⬜ |

---

## Capstone Project: Enterprise Q&A Bot

The capstone ties together all Phase 1 skills into a deployable system.

### Architecture

```
User
 │
 ▼
POST /api/ask  ←── Spring Boot (Java)
 │                 • Basic auth
 │                 • Rate limiting
 │                 • JSON logging
 │
 ▼
Python Pipeline
 │  • Domain system prompt
 │  • Anthropic Claude API
 │  • Pydantic validation
 │  • Token counting + cost logging
 │
 ▼
AskResponse JSON
 {
   "answer": "...",
   "confidence": 0.92,
   "sources": [...],
   "tokens_used": 312,
   "cost_usd": 0.00047
 }
```

### Example Request

```bash
curl -X POST http://localhost:8080/api/ask \
  -u admin:secret \
  -H "Content-Type: application/json" \
  -d '{"question": "How do I reset my VPN credentials?"}'
```

### Example Response

```json
{
  "answer": "To reset your VPN credentials, navigate to the IT portal at ...",
  "confidence": 0.95,
  "sources": ["IT Handbook v3.2", "VPN Setup Guide"],
  "tokens_used": 284,
  "cost_usd": 0.00043
}
```

---

## Key Resources

| Resource | URL |
|----------|-----|
| Anthropic Prompt Engineering Guide | https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview |
| Anthropic Python SDK | https://github.com/anthropics/anthropic-sdk-python |
| Anthropic API Reference | https://docs.anthropic.com/en/api |
| OpenAI Cookbook | https://cookbook.openai.com |
| Pydantic Docs | https://docs.pydantic.dev |
| Spring Boot Docs | https://spring.io/projects/spring-boot |
| tiktoken (tokenizer) | https://github.com/openai/tiktoken |

---

## Learning Roadmap Context

This is **Phase 1 of 6** in the LLM Customization for Enterprise roadmap:

| Phase | Topic | Status |
|-------|-------|--------|
| **1** | **API & Prompt Engineering Foundations** | 🔵 In progress |
| 2 | RAG & Knowledge Pipelines | ⬜ |
| 3 | Agent Frameworks | ⬜ |
| 4 | MCP & Enterprise Tool Integration | ⬜ |
| 5 | Fine-tuning & Model Customization | ⬜ |
| 6 | Enterprise Production & Security | ⬜ |

---

## License

MIT

