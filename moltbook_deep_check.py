import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

API_KEY = "moltbook_sk_YKiXJXWXr5JG2OqdlkvY0r9XHqXC0670"

print("[Moltbook] 深度检查帖子反馈\n")

# Get all my posts with full details
try:
    r = requests.get(
        "https://www.moltbook.com/api/v1/agents/me/posts",
        headers={"Authorization": f"Bearer {API_KEY}"},
        params={"limit": 20},
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        posts = data.get('posts', [])
        
        print(f"我的帖子总数: {len(posts)}\n")
        
        for p in posts:
            title = p.get('title', 'Untitled')
            post_id = p.get('id', 'N/A')
            upvotes = p.get('upvotes', 0)
            downvotes = p.get('downvotes', 0)
            comments = p.get('comment_count', 0)
            created = p.get('created_at', 'N/A')[:10]
            submolt = p.get('submolt', {}).get('name', 'N/A')
            
            print(f"📌 {title[:60]}")
            print(f"   ID: {post_id}")
            print(f"   社区: {submolt}")
            print(f"   赞:{upvotes} 踩:{downvotes} 评论:{comments}")
            print(f"   发布: {created}")
            
            # Check comments if any
            if comments > 0:
                r2 = requests.get(
                    f"https://www.moltbook.com/api/v1/posts/{post_id}/comments",
                    headers={"Authorization": f"Bearer {API_KEY}"},
                    timeout=30
                )
                if r2.status_code == 200:
                    c_data = r2.json()
                    c_list = c_data.get('comments', [])
                    print(f"   最新评论:")
                    for c in c_list[:2]:
                        author = c.get('author', {}).get('name', 'Unknown')
                        content = c.get('content', '')[:50]
                        print(f"     @{author}: {content}...")
            print()
            
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
