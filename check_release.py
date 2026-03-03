import requests
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

TOKEN = os.getenv("GITHUB_TOKEN", "")
OWNER = "w491623834-oss"
REPO = "tangyuan-core"

headers = {"Authorization": f"token {TOKEN}"}
url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"

r = requests.get(url, headers=headers)
if r.status_code == 200:
    data = r.json()
    print(f"[OK] Release found!")
    print(f"Tag: {data['tag_name']}")
    print(f"Name: {data['name']}")
    print(f"URL: {data['html_url']}")
else:
    print(f"[INFO] No release found yet (Status: {r.status_code})")
    # Try listing all releases
    url_all = f"https://api.github.com/repos/{OWNER}/{REPO}/releases"
    r2 = requests.get(url_all, headers=headers)
    if r2.status_code == 200 and len(r2.json()) > 0:
        print(f"[OK] Found {len(r2.json())} releases.")
        print(f"Latest: {r2.json()[0]['name']} - {r2.json()[0]['html_url']}")
    else:
        print("[FAIL] No releases found.")
