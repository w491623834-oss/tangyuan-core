import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

# EvoMap check
print("[1/2] EvoMap heartbeat...")
try:
    payload = {
        "protocol": "gep-a2a",
        "protocol_version": "1.0.0",
        "message_type": "heartbeat",
        "message_id": "msg_1741024020_9c4d",
        "sender_id": "node_1d8e95c362098d3e",
        "timestamp": "2026-03-03T20:47:00Z",
        "payload": {}
    }
    r = requests.post("https://evomap.ai/a2a/heartbeat", json=payload, timeout=30)
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"Node status: {data.get('node_status')}")
        print(f"Credits: {data.get('credit_balance')}")
except Exception as e:
    print(f"Error: {e}")

# Check available tasks
print("\n[2/2] Checking available tasks...")
try:
    payload = {
        "protocol": "gep-a2a",
        "protocol_version": "1.0.0",
        "message_type": "fetch",
        "message_id": "msg_1741024030_8b2a",
        "sender_id": "node_1d8e95c362098d3e",
        "timestamp": "2026-03-03T20:47:10Z",
        "payload": {"asset_type": "Capsule", "include_tasks": True}
    }
    r = requests.post("https://evomap.ai/a2a/fetch", json=payload, timeout=30)
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        tasks = data.get('tasks', [])
        print(f"Available tasks: {len(tasks)}")
        for t in tasks[:3]:
            print(f"  - {t.get('title', 'Untitled')[:40]}...")
except Exception as e:
    print(f"Error: {e}")

print("\n[Done] EvoMap check complete.")
