"""
Notification dispatcher: email (SendGrid), Slack webhook, Discord webhook.
All channels are optional — missing env vars simply skip that channel.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

SENDGRID_KEY = os.getenv("SENDGRID_API_KEY", "")
FROM_EMAIL = os.getenv("NOTIFY_FROM_EMAIL", "")
TO_EMAIL = os.getenv("NOTIFY_TO_EMAIL", "")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL", "")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL", "")


def send_email(subject: str, body: str) -> bool:
    if not SENDGRID_KEY or not FROM_EMAIL or not TO_EMAIL:
        print("[notify] SendGrid not configured — skipping email.")
        return False

    payload = {
        "personalizations": [{"to": [{"email": TO_EMAIL}]}],
        "from": {"email": FROM_EMAIL},
        "subject": subject,
        "content": [{"type": "text/plain", "value": body}],
    }
    r = requests.post(
        "https://api.sendgrid.com/v3/mail/send",
        headers={"Authorization": f"Bearer {SENDGRID_KEY}", "Content-Type": "application/json"},
        json=payload,
        timeout=15,
    )
    if r.status_code in (200, 202):
        print(f"[notify] Email sent to {TO_EMAIL}")
        return True
    print(f"[notify] Email failed: HTTP {r.status_code} — {r.text[:200]}")
    return False


def send_slack(message: str) -> bool:
    if not SLACK_WEBHOOK:
        return False
    r = requests.post(SLACK_WEBHOOK, json={"text": message}, timeout=10)
    if r.status_code == 200:
        print("[notify] Slack message sent.")
        return True
    print(f"[notify] Slack failed: HTTP {r.status_code}")
    return False


def send_discord(message: str) -> bool:
    if not DISCORD_WEBHOOK:
        return False
    r = requests.post(DISCORD_WEBHOOK, json={"content": message[:2000]}, timeout=10)
    if r.status_code in (200, 204):
        print("[notify] Discord message sent.")
        return True
    print(f"[notify] Discord failed: HTTP {r.status_code}")
    return False


def send_all(subject: str, body: str):
    """Send to all configured channels."""
    send_email(subject, body)
    send_slack(f"*{subject}*\n{body[:500]}")
    send_discord(f"**{subject}**\n{body[:1800]}")


def send_daily_digest(journal_date: str | None = None):
    """Read today's journal and blast it to all channels."""
    date = journal_date or datetime.utcnow().strftime("%Y-%m-%d")
    journal_path = Path(__file__).parent.parent / "journal" / f"{date}.md"

    if not journal_path.exists():
        send_all(f"Trading Agent — No Journal for {date}", "No journal file found for today.")
        return

    body = journal_path.read_text(encoding="utf-8")
    send_all(f"Trading Agent Daily Digest — {date}", body)


def send_trade_alert(symbol: str, side: str, qty: float, price: float, reasoning: str):
    msg = (
        f"TRADE EXECUTED: {side.upper()} {qty} {symbol} @ ${price:.2f}\n"
        f"Reasoning: {reasoning}"
    )
    send_all(f"Trade Alert — {symbol}", msg)


def send_risk_alert(message: str):
    send_all("RISK ALERT — Trading Bot", message)


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "digest"

    if action == "digest":
        send_daily_digest()
    elif action == "test":
        send_all("Test Notification", "This is a test from the trading bot notify.py script.")
    elif action == "risk":
        send_risk_alert(sys.argv[2] if len(sys.argv) > 2 else "Test risk alert")
    else:
        print("Usage: python notify.py [digest|test|risk 'message']")
