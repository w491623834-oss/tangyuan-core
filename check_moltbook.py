import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

API_KEY = "moltbook_sk_YKiXJXWXr5JG2OqdlkvY0r9XHqXC0670"

# First, let's get available submolts
print("Fetching available submolts...")
try:
    r = requests.get(
        "https://www.moltbook.com/api/v1/submolts",
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=30
    )
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"Submolts: {data}")
except Exception as e:
    print(f"Error: {e}")

# Also try fetching my agent profile
print("\nFetching agent profile...")
try:
    r = requests.get(
        "https://www.moltbook.com/api/v1/agents/me",
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=30
    )
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        print(f"Profile: {r.text[:500]}")
except Exception as e:
    print(f"Error: {e}")
