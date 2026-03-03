import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

package_name = "tangyuan-core"
url = f"https://pypi.org/pypi/{package_name}/json"

print(f"Checking PyPI for '{package_name}'...")
try:
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        version = data['info']['version']
        release_date = data['urls'][0]['upload_time']
        print(f"[SUCCESS] Package found on PyPI!")
        print(f"Version: {version}")
        print(f"Upload Time: {release_date}")
        print(f"URL: https://pypi.org/project/{package_name}/")
    else:
        print(f"[INFO] Package not found yet (Status: {r.status_code}).")
        print("It might take a few minutes to propagate, or the upload failed.")
except Exception as e:
    print(f"[ERROR] {e}")
