import requests
from typing import Any, Dict, Optional

BASE_URL = "https://jsonplaceholder.typicode.com"


def list_posts() -> Optional[Dict[str, Any]]:
    try:
        r = requests.get(f"{BASE_URL}/posts", timeout=5)
        r.raise_for_status()
        return r.json()[:5]  # return first 5 for demo
    except requests.RequestException as e:
        print("Error fetching posts:", e)
        return None


def get_post(post_id: int) -> Optional[Dict[str, Any]]:
    try:
        r = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=5)
        if r.status_code == 404:
            print("Post not found")
            return None
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        print("Error fetching post:", e)
        return None


def create_post(payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    try:
        r = requests.post(f"{BASE_URL}/posts", json=payload, timeout=5)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        print("Error creating post:", e)
        return None


def main():
    print("Listing posts (first 5):")
    posts = list_posts()
    if posts:
        for p in posts:
            print(f"- {p['id']}: {p['title']}")

    print("\nGet post with id=1")
    post = get_post(1)
    if post:
        print(post)

    print("\nCreate a new post")
    new = create_post({"title": "Demo Post", "body": "Hello from assignment", "userId": 1})
    if new:
        print("Created:", new)


if __name__ == "__main__":
    main()
