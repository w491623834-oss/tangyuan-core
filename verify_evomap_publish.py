import requests

print("验证EvoMap发布...\n")

# Check my assets
r = requests.get("https://evomap.ai/a2a/assets?source_node_id=node_1d8e95c362098d3e")
if r.status_code == 200:
    data = r.json()
    assets = data.get('assets', [])
    
    # Find the new assets
    new_assets = [a for a in assets if 'tangyuan' in str(a.get('summary', '')).lower() or 'zero' in str(a.get('summary', '')).lower()]
    
    print(f"总资产数: {len(assets)}")
    print(f"tangyuan相关资产: {len(new_assets)}\n")
    
    for a in new_assets[-3:]:  # Show last 3
        print(f"Type: {a.get('asset_type')}")
        print(f"Summary: {a.get('summary', 'N/A')[:60]}...")
        print(f"Status: {a.get('status')}")
        print(f"GDI: {a.get('gdi_score', 0)}")
        print(f"Asset ID: {a.get('asset_id')[:30]}...")
        print()
