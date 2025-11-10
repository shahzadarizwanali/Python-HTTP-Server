import urllib.request
import json

BASE_URL = "http://127.0.0.1:5000"

with urllib.request.urlopen(f"{BASE_URL}/companies") as response:
    data = json.loads(response.read())
    print("Available companies:", data["companies"])
