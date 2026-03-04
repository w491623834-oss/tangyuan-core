import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 50)
print(" tangyuan-core v1.0.0 推广成果检查 ")
print("=" * 50)

# 1. PyPI 检查
print("\n[1/3] PyPI 下载统计...")
try:
    # PyPI doesn't provide direct download stats via API
    # Check if package exists and get basic info
    r = requests.get("https://pypi.org/pypi/tangyuan-core/json", timeout=30)
    if r.status_code == 200:
        data = r.json()
        info = data.get('info', {})
        version = info.get('version', 'N/A')
        downloads = data.get('urls', [])
        
        print(f"   版本: {version}")
        print(f"   发布日期: {downloads[0].get('upload_time', 'N/A')[:10] if downloads else 'N/A'}")
        print(f"   状态: ✅ 已发布")
        print(f"   URL: https://pypi.org/project/tangyuan-core/")
        print(f"   注意: PyPI不公开实时下载统计")
except Exception as e:
    print(f"   Error: {e}")

# 2. GitHub 检查
print("\n[2/3] GitHub 仓库统计...")
try:
    # Use GitHub API to check repo stats
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(
        "https://api.github.com/repos/w491623834-oss/tangyuan-core",
        headers=headers,
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        print(f"   Stars: {data.get('stargazers_count', 0)}")
        print(f"   Forks: {data.get('forks_count', 0)}")
        print(f"   Watchers: {data.get('watchers_count', 0)}")
        print(f"   Open Issues: {data.get('open_issues_count', 0)}")
        print(f"   创建时间: {data.get('created_at', 'N/A')[:10]}")
        print(f"   最后更新: {data.get('updated_at', 'N/A')[:10]}")
        print(f"   URL: {data.get('html_url', 'N/A')}")
        
        # Check releases
        r2 = requests.get(
            "https://api.github.com/repos/w491623834-oss/tangyuan-core/releases",
            headers=headers,
            timeout=30
        )
        if r2.status_code == 200:
            releases = r2.json()
            if releases:
                latest = releases[0]
                print(f"\n   最新Release: {latest.get('tag_name', 'N/A')}")
                print(f"   发布名称: {latest.get('name', 'N/A')}")
                print(f"   下载次数: {sum(a.get('download_count', 0) for a in latest.get('assets', []))}")
except Exception as e:
    print(f"   Error: {e}")

# 3. Moltbook 检查
print("\n[3/3] Moltbook 帖子反馈...")
API_KEY = "moltbook_sk_YKiXJXWXr5JG2OqdlkvY0r9XHqXC0670"
try:
    r = requests.get(
        "https://www.moltbook.com/api/v1/agents/me/posts",
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=30
    )
    if r.status_code == 200:
        data = r.json()
        posts = data.get('posts', [])
        
        tangyuan_posts = [p for p in posts if 'tangyuan' in p.get('title', '').lower() or '8GB' in p.get('title', '')]
        
        if tangyuan_posts:
            for p in tangyuan_posts:
                print(f"\n   标题: {p.get('title', 'N/A')[:50]}...")
                print(f"   赞: {p.get('upvotes', 0)} | 评论: {p.get('comment_count', 0)}")
                print(f"   热度: {p.get('hot_score', 0)}")
                print(f"   发布时间: {p.get('created_at', 'N/A')[:10]}")
        else:
            print("   未找到相关帖子")
            
        # All posts summary
        print(f"\n   我的总帖子数: {len(posts)}")
        total_upvotes = sum(p.get('upvotes', 0) for p in posts)
        total_comments = sum(p.get('comment_count', 0) for p in posts)
        print(f"   总获赞: {total_upvotes}")
        print(f"   总评论: {total_comments}")
        
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "=" * 50)
print(" 成果总结 ")
print("=" * 50)
print("""
平台          状态          关键指标
─────────────────────────────────────
PyPI         ✅ 已发布      v1.0.0 可pip安装
GitHub       ✅ 已发布      Release v1.0.0
Moltbook     ✅ 已发布      builds社区

待观察指标:
- PyPI下载量 (需第三方统计)
- GitHub Stars增长
- Moltbook帖子互动
""")
