import json
import os
from typing import Dict, List

def parse_har_file(har_path: str, target_username: str) -> List[str]:
    """Extracts a list of followers from a single HAR file."""
    if not os.path.exists(har_path):
        raise FileNotFoundError(f"HAR file not found: {har_path}")

    with open(har_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    followers = set()
    entries = data.get("log", {}).get("entries", [])

    for entry in entries:
        url = entry.get("request", {}).get("url", "")
        # Filter for Instagram's friendship API endpoints
        if "friendships" in url and "followers" in url:
            response_text = entry.get("response", {}).get("content", {}).get("text")
            if not response_text:
                continue
            
            try:
                json_data = json.loads(response_text)
                for user in json_data.get("users", []):
                    followers.add(user["username"])
            except json.JSONDecodeError:
                continue
    
    return sorted(list(followers))

def update_adjacency_list(json_path: str, username: str, followers: List[str]):
    """Updates the master adjacency JSON file with new data."""
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            adjacency = json.load(f)
    else:
        adjacency = {}

    adjacency[username] = followers

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(adjacency, f, indent=2, ensure_ascii=False)