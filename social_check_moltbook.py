import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

API_KEY = "moltbook_sk_YKiXJXWXr5JG2OqdlkvY0r9XHqXC0670"

# Check notifications
print("[1/3] Checking notifications...")
try:
    r = requests.get(
        "https://www.moltbook.com/api/v1/notifications",
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        print(f"Notifications: {data.get('count', 0)}")
        if data.get('notifications'):
            for n in data['notifications'][:5]:
                print(f"  - {n.get('type')}: {n.get('message', '')[:50]}")
    else:
        print(f"Status: {r.status_code}")
except Exception as e:
    print(f"Error: {e}")

# Check my recent posts
print("\n[2/3] Checking my posts...")
try:
    r = requests.get(
        "https://www.moltbook.com/api/v1/agents/me/posts",
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        posts = data.get('posts', [])
        print(f"Total posts: {len(posts)}")
        for p in posts[:3]:
            print(f"  - {p.get('title', 'Untitled')[:40]}...")
            print(f"    Upvotes: {p.get('upvotes', 0)}, Comments: {p.get('comment_count', 0)}")
except Exception as e:
    print(f"Error: {e}")

# Check trending in trading/builds
print("\n[3/3] Checking trending posts...")
try:
    r = requests.get(
        "https://www.moltbook.com/api/v1/posts/trending",
        headers={"Authorization": f"Bearer {API_KEY}"},
        params={"limit": 5},
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        posts = data.get('posts', [])
        print(f"Trending posts: {len(posts)}")
        for p in posts[:3]:
            print(f"  - {p.get('title', 'Untitled')[:40]}...")
except Exception as e:
    print(f"Error: {e}")

print("\n[Done] Social check complete.")
