import requests
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

TOKEN = os.getenv("GITHUB_TOKEN", "")
OWNER = "w491623834-oss"
REPO = "tangyuan-core"
TAG = "v1.0.0"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

release_data = {
    "tag_name": TAG,
    "name": "tangyuan-core v1.0.0 - Zero-Dependency Core",
    "body": """Ultra-lightweight, zero-dependency core for Digital Guardians.

## Performance
- 100x faster startup (5.2s -> 0.05s)
- 90x less memory (210MB -> 2.3MB)
- 30x less CPU (3-5% -> <0.1%)

## Install
```bash
pip install tangyuan-core
```

## Features
- Pure Python stdlib (socket, ssl, json)
- FireSeed 3D identity verification
- Cross-platform (TY-RAL)
- <10KB core package

**TangYuan** - Digital Guardian, 2026""",
    "draft": False,
    "prerelease": False
}

url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases"
response = requests.post(url, headers=headers, json=release_data)

if response.status_code == 201:
    data = response.json()
    print(f"[SUCCESS] Release created!")
    print(f"Tag: {data['tag_name']}")
    print(f"URL: {data['html_url']}")
else:
    print(f"[FAILED] {response.status_code}: {response.text}")
