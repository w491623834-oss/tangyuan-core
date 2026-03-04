import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

API_KEY = "moltbook_sk_YKiXJXWXr5JG2OqdlkvY0r9XHqXC0670"

# Try different comment endpoints
endpoints = [
    "/api/v1/comments",
    "/api/v1/posts/comments",
    "/api/comments",
]

post_id = "07131357-a299-402d-ae36-39e012c57944"

print("测试评论接口...\n")

# Try post-specific endpoint
url = f"https://www.moltbook.com/api/v1/posts/{post_id}/comments"
print(f"尝试: {url}")

try:
    r = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={"content": "测试评论"},
        timeout=30
    )
    print(f"状态: {r.status_code}")
    print(f"响应: {r.text[:200]}")
except Exception as e:
    print(f"错误: {e}")

# Also check what methods are available
print("\n检查GET接口...")
try:
    r = requests.get(
        url,
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=30
    )
    print(f"GET状态: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        comments = data.get('comments', [])
        print(f"现有评论数: {len(comments)}")
except Exception as e:
    print(f"错误: {e}")
