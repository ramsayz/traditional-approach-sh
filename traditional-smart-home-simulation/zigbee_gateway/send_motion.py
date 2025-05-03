import requests
res = requests.post("http://localhost:5000/motion")
print("Motion Event Sent:", res.json())
