import json
import os

LEADERBOARD_FILE = 'leaderboard.json'
SETTINGS_FILE = 'settings_car.json'

def load_leaderboard():
    # 1. Check if file exists
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    
    # 2. Check if file is empty (0 bytes)
    if os.path.getsize(LEADERBOARD_FILE) == 0:
        return []

    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            data = json.load(f)
            # Ensure the data is a list before sorting
            if not isinstance(data, list):
                return []
            return sorted(data, key=lambda x: x['score'], reverse=True)[:10]
    except (json.JSONDecodeError, ValueError):
        # If the file is corrupted, return empty list
        return []

def save_score(name, score, distance):
    scores = load_leaderboard()
    scores.append({"name": name, "score": score, "distance": int(distance)})
    # Sort and keep only the top 10
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:10]
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(scores, f, indent=4) # indent=4 makes the JSON file readable for humans

def load_settings():
    default = {"sound": True, "car_color": "red", "difficulty": "Medium"}
    if not os.path.exists(SETTINGS_FILE) or os.path.getsize(SETTINGS_FILE) == 0:
        return default
    try:
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    except:
        return default

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)