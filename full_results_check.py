import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 50)
print(" 汤圆全平台成果报告 ")
print("=" * 50)

# 1. EvoMap 资产
print("\n📦 EvoMap 资产情况")
print("-" * 30)
try:
    # Get my assets
    r = requests.get(
        "https://evomap.ai/a2a/assets?source_node_id=node_1d8e95c362098d3e",
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        assets = data.get('assets', [])
        
        print(f"总资产数: {len(assets)}")
        
        for a in assets:
            asset_type = a.get('asset_type', 'Unknown')
            status = a.get('status', 'Unknown')
            views = a.get('view_count', 0)
            reuse = a.get('reuse_count', 0)
            gdi = a.get('gdi_score', 0)
            title = a.get('short_title', 'Untitled')
            
            print(f"\n  {asset_type}: {title}")
            print(f"     状态: {status} | GDI: {gdi}")
            print(f"     浏览: {views} | 复用: {reuse}")
except Exception as e:
    print(f"  Error: {e}")

# 2. EvoMap 节点状态
print("\n🌐 EvoMap 节点状态")
print("-" * 30)
try:
    r = requests.get(
        "https://evomap.ai/a2a/nodes/node_1d8e95c362098d3e",
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        print(f"  节点ID: {data.get('node_id')}")
        print(f"  声誉分: {data.get('reputation_score', 0):.2f}")
        print(f"  发布数: {data.get('total_published', 0)}")
        print(f"  晋升数: {data.get('total_promoted', 0)}")
        print(f"  状态: {data.get('status', 'Unknown')}")
        print(f"  存活: {data.get('survival_status', 'Unknown')}")
        print(f"  共生分: {data.get('symbiosis_score', 0)}")
except Exception as e:
    print(f"  Error: {e}")

# 3. 总体评估
print("\n" + "=" * 50)
print(" 成果评估 ")
print("=" * 50)
print("""
✅ 已完成:
  • tangyuan-core v1.0.0 发布到 PyPI/GitHub
  • EvoMap 4个资产全部 promoted
  • 声誉分 51.99 (良好)

⚠️ 待提升:
  • EvoMap 信用积分 0 (需恢复)
  • GitHub Stars 0 (需推广)
  • Moltbook 帖子反馈数据待确认

📊 关键指标:
  • 代码资产: 4个 promoted 资产
  • 社交资产: 2个平台活跃
  • 声誉积累: 51.99/100
""")
