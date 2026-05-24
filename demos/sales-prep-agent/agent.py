"""
Sales Prep Agent — AI Agents Customer Demo
==========================================
This demo shows a business-focused AI agent that uses multiple tools
to complete a real task: preparing for a sales call.

The agent is given one plain-English request and decides for itself
which tools to call, in what order, to produce a useful result.

Run it:
    export ANTHROPIC_API_KEY=your_key_here
    python agent.py
"""

import json
import os
import anthropic

# ─────────────────────────────────────────────
#  MOCK DATA  (stands in for your real CRM/DB)
# ─────────────────────────────────────────────

MOCK_CRM = {
    "acme corp": {
        "account_id": "ACM-0042",
        "industry": "Manufacturing",
        "employees": 1200,
        "annual_revenue_usd": 85_000_000,
        "current_products": ["Capacitor Basic", "Capacitor Pro"],
        "renewal_date": "2026-09-01",
        "account_manager": "Jordan Lee",
        "last_contact": "2026-03-12",
        "notes": "Happy with product; interested in enterprise tier during last call.",
    },
    "globex": {
        "account_id": "GLX-0017",
        "industry": "Energy",
        "employees": 400,
        "annual_revenue_usd": 22_000_000,
        "current_products": ["Capacitor Basic"],
        "renewal_date": "2026-07-15",
        "account_manager": "Sam Rivera",
        "last_contact": "2026-04-01",
        "notes": "Price-sensitive; evaluating competitors.",
    },
}

MOCK_NEWS = {
    "acme corp": [
        "Acme Corp announces 15% revenue growth in Q1 2026 driven by factory expansion.",
        "Acme Corp named to Fortune 500 list for the third consecutive year.",
        "Acme Corp CTO interview: 'We're doubling our software investment this year.'",
    ],
    "globex": [
        "Globex secures $50M Series C funding round.",
        "Globex expands into European markets; hires new VP of Engineering.",
        "Globex signs partnership with AWS for cloud infrastructure.",
    ],
}

# ─────────────────────────────────────────────
#  TOOL DEFINITIONS  (what the agent can use)
# ─────────────────────────────────────────────

TOOLS = [
    {
        "name": "crm_lookup",
        "description": (
            "Look up a customer account in the CRM database. "
            "Returns account details including current products, revenue, renewal date, and notes."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string",
                    "description": "The name of the company to look up (case-insensitive).",
                }
            },
            "required": ["company_name"],
        },
    },
    {
        "name": "web_search",
        "description": (
            "Search the web for recent news and information about a company or topic. "
            "Returns a list of recent headlines and summaries."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query, e.g. 'Acme Corp recent news 2026'.",
                }
            },
            "required": ["query"],
        },
    },
    {
        "name": "calculate",
        "description": "Evaluate a mathematical expression and return the numeric result.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "A valid Python math expression, e.g. '85_000_000 * 0.02'.",
                }
            },
            "required": ["expression"],
        },
    },
    {
        "name": "draft_email",
        "description": (
            "Draft a professional email. Returns the formatted email text ready to review and send."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "Recipient name or email address."},
                "subject": {"type": "string", "description": "Email subject line."},
                "body": {"type": "string", "description": "Full email body text."},
            },
            "required": ["to", "subject", "body"],
        },
    },
]

# ─────────────────────────────────────────────
#  TOOL IMPLEMENTATIONS  (the actual logic)
# ─────────────────────────────────────────────

def crm_lookup(company_name: str) -> dict:
    key = company_name.lower().strip()
    if key in MOCK_CRM:
        return {"status": "found", "data": MOCK_CRM[key]}
    return {"status": "not_found", "message": f"No account found for '{company_name}'."}


def web_search(query: str) -> dict:
    # Extract company name from query for mock lookup
    for company in MOCK_NEWS:
        if company in query.lower():
            return {"status": "ok", "results": MOCK_NEWS[company]}
    return {
        "status": "ok",
        "results": ["No recent news found. Try a more specific company name."],
    }


def calculate(expression: str) -> dict:
    try:
        # Safe eval: only allow math operations
        allowed = {k: v for k, v in __builtins__.items()
                   if k in ("abs", "round", "min", "max", "sum", "pow")} if isinstance(__builtins__, dict) else {}
        result = eval(expression, {"__builtins__": allowed})  # noqa: S307
        return {"status": "ok", "result": result, "expression": expression}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def draft_email(to: str, subject: str, body: str) -> dict:
    email_text = f"""
TO: {to}
SUBJECT: {subject}

{body}
    """.strip()
    return {"status": "drafted", "email": email_text}


def run_tool(tool_name: str, tool_input: dict) -> str:
    """Dispatch a tool call and return its result as a JSON string."""
    if tool_name == "crm_lookup":
        result = crm_lookup(**tool_input)
    elif tool_name == "web_search":
        result = web_search(**tool_input)
    elif tool_name == "calculate":
        result = calculate(**tool_input)
    elif tool_name == "draft_email":
        result = draft_email(**tool_input)
    else:
        result = {"status": "error", "message": f"Unknown tool: {tool_name}"}
    return json.dumps(result, indent=2)


# ─────────────────────────────────────────────
#  AGENT LOOP
# ─────────────────────────────────────────────

def run_agent(user_request: str, verbose: bool = True) -> str:
    """
    Run the sales prep agent on a user request.
    Uses an agentic loop: keep calling Claude until it stops using tools.
    """
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    system_prompt = """You are a Sales Prep Agent for a software company.
When given a customer name or meeting request, you:
1. Look up their account in the CRM
2. Search for recent news about the company
3. Calculate relevant business metrics (e.g. potential upsell value = ~2% of their revenue)
4. Draft a short, professional meeting-prep email summary for the sales rep

Always use all four tools in order. Be concise and business-focused in your final summary."""

    messages = [{"role": "user", "content": user_request}]

    if verbose:
        print("\n" + "═" * 60)
        print("🤖  SALES PREP AGENT — STARTING")
        print("═" * 60)
        print(f"\n📨  Request: {user_request}\n")

    final_text = ""

    # Agentic loop: continue until the model stops calling tools
    while True:
        response = client.messages.create(
            model="claude-opus-4-7",        # Most capable model for agentic tasks
            max_tokens=4096,
            system=system_prompt,
            tools=TOOLS,
            messages=messages,
        )

        # Collect any text the model produces this turn
        tool_calls = []
        text_blocks = []
        for block in response.content:
            if block.type == "text":
                text_blocks.append(block.text)
            elif block.type == "tool_use":
                tool_calls.append(block)

        if text_blocks and verbose:
            for text in text_blocks:
                print(f"💬  Agent: {text}\n")

        # If no tool calls, the agent is done
        if response.stop_reason == "end_turn" or not tool_calls:
            final_text = "\n".join(text_blocks)
            break

        # Add the assistant's response (including tool calls) to the message history
        messages.append({"role": "assistant", "content": response.content})

        # Execute each tool call and collect results
        tool_results = []
        for tool_call in tool_calls:
            if verbose:
                print(f"🔧  Using tool: {tool_call.name}")
                print(f"    Input: {json.dumps(tool_call.input, indent=6)}")

            result = run_tool(tool_call.name, tool_call.input)

            if verbose:
                result_preview = result[:200] + "..." if len(result) > 200 else result
                print(f"    Result: {result_preview}\n")

            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tool_call.id,
                "content": result,
            })

        # Feed the tool results back to the agent
        messages.append({"role": "user", "content": tool_results})

    if verbose:
        print("═" * 60)
        print("✅  AGENT COMPLETE")
        print("═" * 60)

    return final_text


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\n⚠️  Please set your ANTHROPIC_API_KEY environment variable.")
        print("   Get a free key at: https://console.anthropic.com\n")
        print("   Then run:  export ANTHROPIC_API_KEY=your_key_here\n")
        exit(1)

    # Demo request — try changing this to "Globex" or your own company name
    request = "Prep me for my 2pm call with Acme Corp."

    result = run_agent(request, verbose=True)

    print("\n" + "─" * 60)
    print("📋  FINAL OUTPUT:")
    print("─" * 60)
    print(result)
    print()
