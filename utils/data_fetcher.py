
# data_fetcher.py
# Eric Chhun
# 10/16/2025
# 
# Handles fetching and formatting traffic + accident data
# from public APIs for use in the application.
# 

# utils/data_fetcher.py
"""
data_fetcher.py
------------------------------------
Handles fetching and preparing traffic and accident data.
This module can later connect to real-world APIs or databases.

Functions:
    - get_traffic_data(city)
    - get_accident_data(city)
    - get_mock_data()

Supports:
    - Live Api fetching (open Data / gov APIs)
    - Mock data generation for testing 
    - City-specific data retrieval
    
"""

import requests # For real API calls 
import random # random data generation
import datetime # Timestamping

# Example placeholder API endpoint (you can replace later)
TRAFFIC_API_URL = "https://api.example.com/traffic"  # Dummy URL
ACCIDENT_API_URL = "https://api.example.com/accidents"  # Dummy URL


def generate_mock_traffic_data(num_records=10):
    """Generate mock traffic & accident data for local testing."""
    cities = ["San Francisco", "Los Angeles", "New York", "Chicago", "Seattle"]
    traffic_levels = ["Low", "Moderate", "High", "Severe"]
    accident_types = ["Rear-end", "Side-impact", "Head-on", "Rollover"]

    mock_data = []
    for _ in range(num_records):
        city = random.choice(cities)
        level = random.choice(traffic_levels)
        accidents = random.randint(0, 20)
        avg_speed = random.randint(10, 65)
        record = {
            "city": city,
            "traffic_level": level,
            "accidents": accidents,
            "avg_speed": avg_speed,
            "accident_type": random.choice(accident_types),
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        mock_data.append(record)
    return mock_data



def fetch_live_traffic_data(api_key=None):
    """Fetch live traffic data from an external API."""
    try:
        # Example structure: replace URL and params with real API later
        params = {"key": api_key, "region": "US"}
        response = requests.get(TRAFFIC_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[ERROR] Traffic API fetch failed: {e}")
        return []


def fetch_live_accident_data(api_key=None):
    """Fetch live accident data from an external API."""
    try:
        params = {"key": api_key, "region": "US"}
        response = requests.get(ACCIDENT_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[ERROR] Accident API fetch failed: {e}")
        return []



def get_traffic_data(use_mock=True, num_records=10, api_key=None):
    """
    Master function that decides between mock or live data.
    Returns a unified dataset for the app.
    """
    if use_mock:
        print("[INFO] Using mock traffic data.")
        return generate_mock_traffic_data(num_records)
    else:
        print("[INFO] Fetching live traffic data from APIs.")
        traffic = fetch_live_traffic_data(api_key)
        accidents = fetch_live_accident_data(api_key)
        return traffic + accidents if traffic and accidents else []



if __name__ == "__main__":
    print("Testing mock traffic data generator...")
    data = get_traffic_data(use_mock=True, num_records=5)
    for record in data:
        print(record)