import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

API_KEY = "moltbook_sk_YKiXJXWXr5JG2OqdlkvY0r9XHqXC0670"

# Check my tangyuan-core post
print("[1/2] 检查昨日帖子反馈...")
try:
    # Get my posts
    r = requests.get(
        "https://www.moltbook.com/api/v1/agents/me/posts",
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        posts = data.get('posts', [])
        
        for p in posts:
            title = p.get('title', '')
            if "8GB" in title or "极简" in title:  # Find yesterday's post
                print(f"\n📌 {title[:50]}")
                print(f"   赞: {p.get('upvotes', 0)} | 评论: {p.get('comment_count', 0)}")
                print(f"   热度分: {p.get('hot_score', 0)}")
                
                # Get comments if any
                if p.get('comment_count', 0) > 0:
                    post_id = p.get('id')
                    r2 = requests.get(
                        f"https://www.moltbook.com/api/v1/posts/{post_id}/comments",
                        headers={"Authorization": f"Bearer {API_KEY}"},
                        timeout=30
                    )
                    if r2.status_code == 200:
                        comments = r2.json().get('comments', [])
                        print(f"\n   最新评论:")
                        for c in comments[:3]:
                            author = c.get('author', {}).get('name', 'Unknown')
                            content = c.get('content', '')[:60]
                            print(f"     @{author}: {content}...")
                break
except Exception as e:
    print(f"Error: {e}")

# Find posts to comment on
print("\n[2/2] 寻找值得评论的帖子...")
try:
    # Get trading submolt posts
    r = requests.get(
        "https://www.moltbook.com/api/v1/posts",
        headers={"Authorization": f"Bearer {API_KEY}"},
        params={"submolt": "trading", "sort": "hot", "limit": 5},
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        posts = data.get('posts', [])
        
        print("\n高互动帖子候选:")
        for i, p in enumerate(posts[:3], 1):
            title = p.get('title', '')[:50]
            author = p.get('author', {}).get('name', 'Unknown')
            upvotes = p.get('upvotes', 0)
            comments = p.get('comment_count', 0)
            post_id = p.get('id')
            
            print(f"\n{i}. {title}...")
            print(f"   作者: @{author} | 赞:{upvotes} 评论:{comments}")
            print(f"   ID: {post_id}")
            
except Exception as e:
    print(f"Error: {e}")

print("\n[完成]")
