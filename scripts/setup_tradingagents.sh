#!/usr/bin/env bash
# Setup TradingAgents (TauricResearch/TradingAgents) for comparison
# Run from the trading-bot repo root:
#   bash scripts/setup_tradingagents.sh

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TA_DIR="$REPO_DIR/../TradingAgents"

echo "=== TradingAgents Setup ==="

if [ ! -d "$TA_DIR" ]; then
    echo "Cloning TauricResearch/TradingAgents..."
    git clone https://github.com/TauricResearch/TradingAgents.git "$TA_DIR"
else
    echo "TradingAgents already cloned at $TA_DIR"
fi

cd "$TA_DIR"

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Installing dependencies..."
venv/bin/pip install -e "." -q

if [ ! -f ".env" ]; then
    echo "Creating .env from template..."
    cat > .env << 'ENVEOF'
# TradingAgents — Lars's comparison setup
ANTHROPIC_API_KEY=        # ← add your key here
ALPACA_API_KEY=
ALPACA_SECRET_KEY=
ALPACA_BASE_URL=https://paper-api.alpaca.markets
SEC_EDGAR_USER_AGENT=Lars Veenstra e.larsve@gmail.com
TRADINGAGENTS_LLM_PROVIDER=anthropic
TRADINGAGENTS_DEEP_THINK_LLM=claude-sonnet-5
TRADINGAGENTS_QUICK_THINK_LLM=claude-haiku-4-5
TRADINGAGENTS_OUTPUT_LANGUAGE=English
TRADINGAGENTS_MAX_DEBATE_ROUNDS=1
TRADINGAGENTS_MAX_RISK_ROUNDS=1
TRADINGAGENTS_MAX_TOOL_ROUNDS=10
TRADINGAGENTS_TEMPERATURE=0.0
TRADINGAGENTS_LLM_MAX_RETRIES=3
ENVEOF
    echo ".env created — add ANTHROPIC_API_KEY before running"
fi

echo ""
echo "✓ Setup complete. To run AAPL test:"
echo "  cd $TA_DIR"
echo "  source venv/bin/activate"
echo "  python ../trading-bot/scripts/tradingagents_test.py"
