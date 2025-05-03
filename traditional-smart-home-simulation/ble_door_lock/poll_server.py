import requests
import time

while True:
    res = requests.get("http://localhost:5000/check").json()
    print("Polling Result:", res)
    if res.get("unlock"):
        print("🚪 Door Unlocked")
    time.sleep(5)
