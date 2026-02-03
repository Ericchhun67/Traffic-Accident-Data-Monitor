# utils/map_handler.py
"""
map_handler.py
------------------------------------
Handles data formatting for map visualization.

Psudo code:
    get traffic data from db handler
    attach lat/lng coordinates to each record
    return list of records with coordinates and traffic info

Functions:
    - format_map_data()
    - merge_data(traffic, accidents)
    - get_location_summary()
support:
    - attach_coordinates()
    - prepare_map_data()
"""
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import random
from utils.db_handler import get_all_traffic_data, get_city_data
from utils.data_fetcher import get_traffic_data
from utils.db_handler import init_db, insert_bulk_traffic_data
from utils.data_fetcher import get_traffic_data



# dictionary of cities
CITY_COORDS = {
    "San Francisco": (37.7749, -122.4194),
    "Los Angeles": (34.0522, -118.2437),
    "New York": (40.7128, -74.0060),
    "Chicago": (41.8781, -87.6298),
    "Seattle": (47.6062, -122.3321),
    "Houston": (29.7604, -95.3698),
    "Dallas": (32.7767, -96.7970),
    "Miami": (25.7617, -80.1918),
    "Boston": (42.3601, -71.0589),
}

# city -> state (for display on map popups)
CITY_STATES = {
    "San Francisco": "CA",
    "Los Angeles": "CA",
    "New York": "NY",
    "Chicago": "IL",
    "Seattle": "WA",
    "Houston": "TX",
    "Dallas": "TX",
    "Miami": "FL",
    "Boston": "MA",
}

# Levels for traffic intensity
TRAFFIC_LEVELS = ["Low", "Medium", "High"]


def attach_coordinates(data):
    """
    Adds latitude, longitude, and traffic_level to each traffic record.
    Randomizes coordinates slightly to prevent overlap.
    """
    processed = []

    for record in data:
        city = record.get("city", "Unknown")
        base_coords = CITY_COORDS.get(city)

        # Assign coordinates
        if base_coords:
            lat, lng = base_coords
        else:
            lat = random.uniform(25.0, 49.0)
            lng = random.uniform(-124.0, -67.0)

        # Add small offset so markers don’t overlap perfectly
        lat += random.uniform(-0.02, 0.02)
        lng += random.uniform(-0.02, 0.02)

        # Add or ensure traffic level exists
        record["traffic_level"] = record.get("traffic_level", random.choice(TRAFFIC_LEVELS))
        # Add state when available
        record["state"] = record.get("state") or CITY_STATES.get(city, "Unknown")
        record["latitude"] = round(lat, 6)
        record["longitude"] = round(lng, 6)

        processed.append(record)

    print(f"[INFO] Processed {len(processed)} map points with coordinates.")
    return processed


def prepare_map_data(city_filter=None):
    """
    Retrieve and prepare traffic data for rendering on the map.
    If a city_filter is provided, it only returns that city's data.
    """
    try:
        if city_filter:
            print(f"[INFO] Loading traffic data for city: {city_filter}")
            raw_data = get_city_data(city_filter)
        else:
            print("[INFO] Loading all traffic data for map view.")
            raw_data = get_all_traffic_data()

        if not raw_data:
            print("[WARNING] No traffic data found. Returning empty list.")
            return []

        map_data = attach_coordinates(raw_data)
        print(f"[INFO] Prepared {len(map_data)} records for map rendering.")
        return map_data

    except Exception as e:
        print(f"[ERROR] Failed to prepare map data: {e}")
        return []



if __name__ == "__main__":
    print("[TEST] Initializing DB and inserting mock data...")
    init_db()
    mock_data = get_traffic_data(use_mock=True, num_records=5)
    insert_bulk_traffic_data(mock_data)

    print("[TEST] Preparing map data...")
    points = prepare_map_data()
    for point in points:
        print(point)
