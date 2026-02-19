import os
import requests
import datetime

# Read secrets from GitHub Actions
BOT_TOKEN = os.getenv("8466329982:AAGRP7QTIkOLnf19cUPN1QkHj3OJtFcWsZ8")
CHAT_ID = os.getenv("6885100476")

def send_telegram(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("Missing BOT_TOKEN or CHAT_ID")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

def run_bot():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    # This is where your AI logic will go later
    message = (
        "🤖 Forex AI Bot is LIVE\n\n"
        f"🕒 Time: {now}\n"
        "📊 Status: Market check completed\n"
        "✅ No card • Free server • Auto running"
    )

    send_telegram(message)

if __name__ == "__main__":
    run_bot()
