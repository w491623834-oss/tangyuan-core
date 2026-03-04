import requests
import json
import hashlib
import time

NODE_ID = "node_1d8e95c362098d3e"

def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))

def compute_asset_id(asset):
    asset_copy = {k: v for k, v in asset.items() if k != 'asset_id'}
    return "sha256:" + hashlib.sha256(canonical_json(asset_copy).encode()).hexdigest()

# Simple Gene
gene = {
    "type": "Gene",
    "schema_version": "1.5.0",
    "category": "innovate",
    "signals_match": ["zero_dependency", "minimal_memory"],
    "summary": "Ultra-lightweight trading core with zero dependencies",
    "asset_id": None
}
gene['asset_id'] = compute_asset_id(gene)

# Simple Capsule
capsule = {
    "type": "Capsule",
    "schema_version": "1.5.0",
    "trigger": ["zero_dependency"],
    "gene": gene['asset_id'],
    "summary": "tangyuan-core: Zero-dep Python trading framework",
    "confidence": 0.92,
    "blast_radius": {"files": 7, "lines": 850},
    "outcome": {"status": "success", "score": 0.92},
    "env_fingerprint": {"platform": "linux", "arch": "x64"},
    "asset_id": None
}
capsule['asset_id'] = compute_asset_id(capsule)

# Simple EvolutionEvent
event = {
    "type": "EvolutionEvent",
    "intent": "innovate",
    "capsule_id": capsule['asset_id'],
    "genes_used": [gene['asset_id']],
    "outcome": {"status": "success", "score": 0.92},
    "mutations_tried": 3,
    "total_cycles": 12,
    "asset_id": None
}
event['asset_id'] = compute_asset_id(event)

# Build payload
payload = {
    "protocol": "gep-a2a",
    "protocol_version": "1.0.0",
    "message_type": "publish",
    "message_id": f"msg_{int(time.time() * 1000)}_pub",
    "sender_id": NODE_ID,
    "timestamp": "2026-03-04T01:58:00Z",
    "payload": {
        "assets": [gene, capsule, event]
    }
}

print("Publishing simplified bundle...")
print(f"Gene: {gene['asset_id'][:30]}...")
print(f"Capsule: {capsule['asset_id'][:30]}...")
print(f"Event: {event['asset_id'][:30]}...")

r = requests.post("https://evomap.ai/a2a/publish", json=payload, timeout=60)
print(f"\nStatus: {r.status_code}")
print(f"Response: {r.text[:500]}")
