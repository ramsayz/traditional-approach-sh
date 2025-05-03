import requests
res = requests.post("http://localhost:5000/proximity")
print("Proximity Event Sent:", res.json())
