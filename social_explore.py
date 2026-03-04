import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

API_KEY = "moltbook_sk_YKiXJXWXr5JG2OqdlkvY0r9XHqXC0670"

# Find quant-related agents to connect with
print("[社交] 搜索量化交易相关帖子...")

try:
    # Search in trading submolt
    r = requests.get(
        "https://www.moltbook.com/api/v1/posts",
        headers={"Authorization": f"Bearer {API_KEY}"},
        params={"submolt": "trading", "limit": 10},
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        posts = data.get('posts', [])
        print(f"Trading社区帖子: {len(posts)}")
        
        # Find posts to engage with
        for p in posts[:5]:
            title = p.get('title', '')
            author = p.get('author', {}).get('name', 'Unknown')
            upvotes = p.get('upvotes', 0)
            
            print(f"\n  📌 {title[:50]}...")
            print(f"     作者: {author} | 赞: {upvotes}")
            
            # Skip my own posts
            if author == "TangYuanAssistant":
                print("     [跳过: 自己的帖子]")
                continue
                
            # High engagement posts worth commenting
            if upvotes >= 5:
                print("     [建议: 高互动帖子，值得评论]")
                # Could comment here
                
except Exception as e:
    print(f"Error: {e}")

# Check agents submolt
print("\n[社交] 搜索Agent技术帖子...")
try:
    r = requests.get(
        "https://www.moltbook.com/api/v1/posts",
        headers={"Authorization": f"Bearer {API_KEY}"},
        params={"submolt": "agents", "limit": 5},
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        posts = data.get('posts', [])
        print(f"Agents社区帖子: {len(posts)}")
        for p in posts[:3]:
            print(f"  - {p.get('title', '')[:40]}...")
except Exception as e:
    print(f"Error: {e}")

print("\n[完成] 社交侦察完成")
