"""
Quick AAPL test using TradingAgents with Claude as the LLM backbone.

Prerequisites:
  1. Set ANTHROPIC_API_KEY in .env (or as env var)
  2. Run from the TradingAgents directory inside the venv:
       source venv/bin/activate
       python run_aapl_test.py

  Or via CLI (non-interactive, no prompts):
       venv/bin/tradingagents \\
           --ticker AAPL \\
           --date $(date +%Y-%m-%d) \\
           --analysts market,news,technical \\
           --save --html --no-show
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from this directory
load_dotenv(Path(__file__).parent / ".env")

# Validate key
api_key = os.getenv("ANTHROPIC_API_KEY", "")
if not api_key:
    raise SystemExit(
        "ERROR: ANTHROPIC_API_KEY is not set.\n"
        "Edit .env and add your key:\n"
        "  ANTHROPIC_API_KEY=sk-ant-..."
    )

from tradingagents.default_config import build_default_config
from tradingagents.graph.trading_graph import TradingAgentsGraph

# Use today's date for the analysis
from datetime import date
analysis_date = date.today().strftime("%Y-%m-%d")
ticker = "AAPL"

print(f"=== TradingAgents AAPL Test ===")
print(f"Ticker : {ticker}")
print(f"Date   : {analysis_date}")
print(f"LLM    : anthropic / claude-sonnet-5 (deep) + claude-haiku-4-5 (quick)")
print()

config = build_default_config()
# Provider already set via .env / TRADINGAGENTS_* vars, but hard-code here too for clarity
config["llm_provider"] = "anthropic"
config["deep_think_llm"] = "claude-sonnet-5"
config["quick_think_llm"] = "claude-haiku-4-5"
config["max_debate_rounds"] = 1
config["max_risk_discuss_rounds"] = 1
config["max_tool_rounds"] = 10
config["temperature"] = 0.0

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate(ticker, analysis_date)

print("\n=== DECISION ===")
print(decision)
