# Sales Prep Agent — Demo

A working AI agent that prepares a sales rep for a client meeting by automatically pulling data from four sources.

## What it does

Given a single sentence like *"Prep me for my 2pm call with Acme Corp,"* the agent:

1. **Looks up the account** in your CRM → gets products, revenue, renewal date, and notes
2. **Searches for recent news** → pulls headlines about the company
3. **Runs a calculation** → estimates upsell potential based on their revenue
4. **Drafts an email** → writes a meeting-prep summary, ready to send

You can watch every step in real time in your terminal.

## Setup

### 1. Get an API key

Sign up for free at [console.anthropic.com](https://console.anthropic.com) and copy your API key.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your API key

```bash
export ANTHROPIC_API_KEY=your_key_here
```

### 4. Run

```bash
python agent.py
```

## Expected output

```
════════════════════════════════════════════════════════════
🤖  SALES PREP AGENT — STARTING
════════════════════════════════════════════════════════════

📨  Request: Prep me for my 2pm call with Acme Corp.

🔧  Using tool: crm_lookup
    Input: { "company_name": "Acme Corp" }
    Result: { "status": "found", "data": { "industry": "Manufacturing" ...

🔧  Using tool: web_search
    Input: { "query": "Acme Corp recent news 2026" }
    Result: { "status": "ok", "results": ["Acme Corp announces 15% ...

🔧  Using tool: calculate
    Input: { "expression": "85_000_000 * 0.02" }
    Result: { "status": "ok", "result": 1700000 ...

🔧  Using tool: draft_email
    Input: { "to": "Jordan Lee", "subject": "Meeting Prep: Acme Corp" ...
    Result: { "status": "drafted", "email": "TO: Jordan Lee ...

════════════════════════════════════════════════════════════
✅  AGENT COMPLETE
════════════════════════════════════════════════════════════
```

## Customise it

- **Change the company:** Edit `request = "Prep me for my 2pm call with ..."` in `agent.py` and try `"Globex"` instead of `"Acme Corp"`.
- **Add a real CRM:** Replace `crm_lookup()` with a call to your Salesforce, HubSpot, or custom API.
- **Add real search:** Replace `web_search()` with a call to a real search API (Brave, Bing, etc.).
- **Connect to email:** Replace `draft_email()` to create a real draft in Gmail or Outlook.

## Key concepts demonstrated

| Concept | Where to see it |
|---------|-----------------|
| Tool definitions | `TOOLS` list — each tool has a name, description, and schema |
| Agentic loop | `run_agent()` function — keeps calling Claude until no more tool calls |
| Tool dispatch | `run_tool()` function — routes tool calls to the right implementation |
| Message history | `messages` list — agent remembers context across all steps |
