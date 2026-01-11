import requests
import hashlib
import os

URL = "https://pointlessjourney.jp/"
STATE_FILE = "state.txt"

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

html = requests.get(URL).text
new = sha(html)

old = None
if os.path.exists(STATE_FILE):
    old = open(STATE_FILE).read()

if old and old != new:
    token = os.environ["LINE_TOKEN"]
    requests.post(
        "https://api.line.me/v2/bot/message/broadcast",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json={
            "messages": [
                {"type": "text", "text": "🔔 pointlessjourney.jp が更新されました"}
            ]
        }
    )

open(STATE_FILE, "w").write(new)
