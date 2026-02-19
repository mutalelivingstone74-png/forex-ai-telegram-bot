import requests
import datetime

BOT_TOKEN = "8466329982:AAGRP7QTIkOLnf19cUPN1QkHj3OJtFcWsZ8"
CHAT_ID = "6885100476"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

def run_bot():
    now = datetime.datetime.utcnow()
    message = f"🤖 AI Bot check\nTime (UTC): {now}"
    send_telegram(message)

if __name__ == "__main__":
    run_bot()
