import subprocess
import sys
import os

def check_url(url: str) -> bool:
    """Run curl against the URL and return True if HTTP status is 2xx/3xx."""
    try:
        result = subprocess.run(
            ["curl", "-s", "-o", "/dev/null",
             "-w", "%{http_code}",
             "--max-time", "10", url],
            capture_output=True, text=True, timeout=15
        )
        status = result.stdout.strip()
        print(f"[INFO] URL: {url}")
        print(f"[INFO] HTTP Status: {status}")
        return status.startswith(("2", "3"))
    except subprocess.TimeoutExpired:
        print(f"[ERROR] Timeout while checking {url}")
        return False
    except Exception as e:
        print(f"[ERROR] {e}")
        return False


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.getenv("TARGET_URL", "https://example.com")

    if check_url(target):
        print(f"[SUCCESS] {target} is reachable ✅")
        sys.exit(0)
    else:
        print(f"[FAILURE] {target} is NOT reachable ❌")
        sys.exit(1)
