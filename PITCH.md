# Talking Points: Introducing AI Agents to Customers

> Use this as a guide for live conversations, demos, or presentations with business stakeholders.
> Adjust the examples to match your customer's industry.

---

## Opening hook (30 seconds)

> *"You've probably used ChatGPT or a chatbot — you ask it something, it tells you an answer. AI agents are fundamentally different. An agent doesn't just answer questions. It takes actions. Let me show you what I mean."*

Then open the terminal and run the demo. Let the output speak first before you explain it.

---

## The one-line explanation

> *"An AI agent is like an executive assistant that can actually do things — not just advise."*

- A chatbot **answers** questions.
- An agent **completes** tasks.

---

## The "why now" story

Three things came together recently that make agents viable for business:

1. **Language models got good enough** to understand complex, ambiguous instructions and make sensible decisions.
2. **Tool use / function calling** lets AI reliably interact with your existing software — CRMs, databases, APIs, email.
3. **The cost dropped dramatically** — tasks that would have required a developer to build a custom workflow can now be described in plain English.

---

## Walking through the demo

When you run `agent.py`, walk the customer through what they're seeing:

**Step 1 — CRM lookup**
> *"Notice the agent didn't need me to tell it to check the CRM. It figured out that was the right first step. And it pulled exactly the fields that matter — not everything, just what's useful."*

**Step 2 — Web search**
> *"Now it's searching the web. This is real-time information. Your team can't read every press release about every client. The agent can — every time, before every call."*

**Step 3 — Calculate**
> *"It's doing a quick back-of-the-napkin calculation on upsell potential. Again, nobody told it to do this. It inferred that a sales rep would want this number."*

**Step 4 — Draft email**
> *"Finally it writes the email. Not a generic template — a personalised one, using the specific data it just gathered."*

**The punchline:**
> *"That whole sequence took the agent about 15 seconds. The equivalent for a human rep is 20–30 minutes of prep, across four different tabs, every time. Multiply that by your team size and call volume."*

---

## Handling common questions

### "Is this just another chatbot?"
> *"No — and the difference matters. A chatbot gives you information. An agent completes work. You could ask a chatbot 'how do I prep for a sales call?' and it would give you a checklist. The agent just does the checklist for you."*

### "What happens when it makes a mistake?"
> *"That's exactly the right question. The answer is: you design for it. The agent surfaces its work for review before anything goes out. A human is always in the loop for consequential decisions — the agent handles the tedious, repetitive parts."*

### "How does it connect to our systems?"
> *"Each 'tool' the agent can use is just an API call — the same way your apps already talk to each other. If you have a CRM with an API, you point the agent at it. We can start with one or two integrations and expand from there."*

### "Is our data safe?"
> *"The agent only calls the APIs you give it access to — nothing more. You control the permissions, the data, and the outputs. Anthropic (the AI company) processes the prompts but your CRM data never leaves your infrastructure — it only gets referenced in the tool results."*

### "How long does this take to build?"
> *"The demo you just saw is about 200 lines of Python. A production version with your real CRM and real search would take 1–2 weeks for a developer to build and test properly. The economics change dramatically compared to a traditional workflow automation project."*

---

## Closing the conversation

**If they're excited:**
> *"The best next step is a 2-week pilot on one specific workflow — something your team does repeatedly today. We pick the highest-value, most repetitive task, build a focused agent, measure the time saved. That gives you a real number to bring to the business case."*

**If they're skeptical:**
> *"Totally fair. The technology is genuinely new and the hype is real. What I'd suggest is: don't believe me, believe the demo. Take the code, plug in your API key, and run it yourself this afternoon. The best way to evaluate it is to touch it."*

**If they want to talk ROI:**

Use this simple framework:

```
Hours saved per week  =  (Minutes per task / 60)  ×  Tasks per day  ×  Team size  ×  5

At $75/hour fully-loaded cost:

Annual value  =  Hours saved per week  ×  52  ×  $75
```

Example: A team of 10 reps, 3 calls/day each, 25 min of prep saved per call:
```
(25/60) × 3 × 10 × 5 = 62.5 hours/week
62.5 × 52 × $75 = $243,750/year
```

---

## The emotional close

> *"The goal isn't to replace your team — it's to remove the parts of their job they hate. Nobody went into sales to copy-paste CRM data. Nobody became an analyst to spend three hours reformatting a report. Agents handle the tedious parts so your people can focus on the human parts — relationships, judgment, creativity. That's the pitch."*

---

## Demo cheat sheet

| Command | What it shows |
|---------|---------------|
| `python agent.py` | Full Acme Corp demo (default) |
| Change `request = "..."` to `"Prep me for Globex"` | Second company profile, different data |
| Comment out `verbose=True` | Shows only final output (cleaner for exec presentations) |
