# Introducing AI Agents to Customers

> A practical guide and live demo for showing business leaders what AI agents can actually do.

---

## What Is an AI Agent?

Most people have used a chatbot — you ask a question, it gives an answer. An **AI Agent** is different in one key way:

> **An agent can take actions, not just give answers.**

Instead of saying *"Here's how you could look that up,"* an agent actually looks it up. It can call your CRM, search the web, run a calculation, send a draft email — and chain all of these steps together automatically to complete a task you've described in plain English.

Think of it like the difference between a consultant who gives you advice, and an executive assistant who reads your email, checks your calendar, and hands you a prepared brief before the meeting.

---

## The Demo

This repo contains a **Sales Prep Agent** — a live, runnable example built with the [Anthropic API](https://docs.anthropic.com).

**Scenario:** A sales rep types one sentence before a client call. The agent:

| Step | What the agent does | Tool used |
|------|---------------------|-----------|
| 1 | Looks up the client's account history | `crm_lookup` |
| 2 | Finds recent news about their company | `web_search` |
| 3 | Calculates their estimated deal value | `calculate` |
| 4 | Drafts a personalised meeting-prep email | `draft_email` |

No clicking through four different apps. No copy-pasting. One request, four actions, one polished output.

👉 **[Run the demo →](demos/sales-prep-agent/)**

---

## Why This Matters for Your Business

| Without AI agents | With AI agents |
|-------------------|----------------|
| Employee spends 30 min prepping for every sales call | Agent delivers a brief in seconds |
| Data lives in silos — CRM, email, web — hard to combine | Agent pulls from all sources in one pass |
| Automation requires hard-coded rules and technical setup | Agent adapts to natural language instructions |
| One tool per task | One agent for many tasks |

---

## How It Works (No Jargon)

```
You: "Prep me for my 2pm call with Acme Corp."

Agent thinks:
  → I need their account info        [uses CRM tool]
  → I need recent news about them    [uses web search]
  → I need the deal size estimate    [uses calculator]
  → I should draft a summary email   [uses email tool]

Agent delivers: a complete meeting brief, ready to send.
```

The agent decides *which tools to use* and *in what order* — you don't have to tell it. That's the difference from traditional automation.

---

## Getting Started

### Prerequisites
- Python 3.9+
- An [Anthropic API key](https://console.anthropic.com) (free to try)

### Run the demo

```bash
cd demos/sales-prep-agent
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
python agent.py
```

You'll see the agent work through each step in real time, showing exactly which tools it's calling and why.

---

## What's in This Repo

```
├── README.md                    ← You are here
├── PITCH.md                     ← Talking points for customer conversations
└── demos/
    └── sales-prep-agent/
        ├── agent.py             ← The working demo (fully annotated)
        ├── requirements.txt     ← Dependencies
        └── README.md            ← Demo-specific setup guide
```

---

## Learn More

- [Anthropic documentation](https://docs.anthropic.com)
- [Claude API tool use guide](https://docs.anthropic.com/en/docs/tool-use)
- [AI agent patterns and best practices](https://docs.anthropic.com/en/docs/agents)
