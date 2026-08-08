# AI Agents Customer Introduction — Session Notes
*Date: 2026-05-24*

---

## Context

Session to address the question: **"What's the best way to demonstrate or introduce AI Agents to customers?"**

Target audience: **Non-technical business users** (executives, product managers, decision-makers)
Focus: **Tool use / integrations** — agents that call APIs, read files, run code, etc.

---

## What Was Built

A complete customer introduction package, committed to the repo `marctek/https-github.com-ionic-team-capacitor-swift-pm` on branch `claude/ai-agents-customer-intro-micXV`.

### Files created

| File | Purpose |
|------|---------|
| `README.md` | Plain-language intro to AI agents for business audiences |
| `PITCH.md` | Talking points, objection handling, ROI framework |
| `demos/sales-prep-agent/agent.py` | Working Sales Prep Agent demo (Python) |
| `demos/sales-prep-agent/README.md` | Setup and walkthrough guide |
| `demos/sales-prep-agent/requirements.txt` | `anthropic>=0.40.0` |

---

## The Demo

**Scenario:** A sales rep types one sentence: *"Prep me for my 2pm call with Acme Corp."*

The agent automatically chains 4 tool calls:

| Step | Tool | What it does |
|------|------|--------------|
| 1 | `crm_lookup` | Looks up the client account — products, revenue, renewal date, notes |
| 2 | `web_search` | Finds recent news headlines about the company |
| 3 | `calculate` | Estimates upsell potential (~2% of annual revenue) |
| 4 | `draft_email` | Writes a personalised meeting-prep email summary |

**Time taken:** ~15 seconds. Human equivalent: 20–30 minutes.

### How to run it

```bash
cd demos/sales-prep-agent
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
python agent.py
```

Get a free API key at: https://console.anthropic.com

---

## Key Concepts

### The one-line explanation
> *"An AI agent is like an executive assistant that can actually do things — not just advise."*

- A **chatbot** answers questions.
- An **agent** completes tasks.

### How tool use works

```
You: "Prep me for my 2pm call with Acme Corp."

Agent thinks:
  → I need their account info        [uses CRM tool]
  → I need recent news about them    [uses web search]
  → I need the deal size estimate    [uses calculator]
  → I should draft a summary email   [uses email tool]

Agent delivers: a complete meeting brief, ready to send.
```

The agent decides *which tools to use* and *in what order* — no step-by-step instructions needed.

---

## Demo Tips

1. **Don't explain first — run the demo first.** Watching it work is 10x more persuasive than any slide.
2. Open the terminal in front of them and let the output scroll.
3. Narrate as it runs: *"Notice it didn't wait for me to tell it to check the CRM — it figured that out itself."*

---

## Pitch Highlights

### Opening hook (30 seconds)
> *"You've probably used ChatGPT or a chatbot — you ask it something, it tells you an answer. AI agents are fundamentally different. An agent doesn't just answer questions. It takes actions. Let me show you what I mean."*

### Common objections

| Objection | Response |
|-----------|----------|
| "Is this just another chatbot?" | "A chatbot gives you information. An agent completes work." |
| "What happens when it makes a mistake?" | "You design for it — the agent surfaces its work for human review before anything goes out." |
| "How does it connect to our systems?" | "Each tool is just an API call — the same way your apps already talk to each other." |
| "Is our data safe?" | "The agent only calls the APIs you give it access to. Your data never leaves your infrastructure." |
| "How long to build?" | "The demo is ~200 lines of Python. A production version takes 1–2 weeks." |

### ROI Framework

```
Hours saved per week = (Minutes per task / 60) × Tasks per day × Team size × 5

Annual value = Hours saved per week × 52 × $75 (fully-loaded cost)
```

**Example:** 10 reps, 3 calls/day, 25 min prep saved per call
→ 62.5 hrs/week → **$243,750/year**

---

## Next Steps (suggested)

- [ ] Get an Anthropic API key and run the demo yourself first
- [ ] Customise `agent.py` with a real CRM API (Salesforce, HubSpot, etc.)
- [ ] Identify one high-volume, repetitive workflow for a 2-week pilot
- [ ] Use `PITCH.md` to prepare for the customer conversation

---

## Links

- PR: https://github.com/marctek/https-github.com-ionic-team-capacitor-swift-pm/pull/2
- Anthropic Console (API keys): https://console.anthropic.com
- Anthropic Docs — Tool Use: https://docs.anthropic.com/en/docs/tool-use
- Anthropic Docs — Agents: https://docs.anthropic.com/en/docs/agents
