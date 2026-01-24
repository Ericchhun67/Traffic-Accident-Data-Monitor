# utils/alert_handler.py
"""
alert_handler.py
------------------------------------
Generates alerts based on traffic and accident data.

Pseudo Code:
    - 

Functions:
    - get_alerts()
    - detect_accident_alerts()
    - detect_traffic_alerts()
    - summarize_alerts()
"""

import os, sys
from datetime import datetime, timedelta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.db_handler import get_all_traffic_data, get_accident_data


# -------------------------------------------------------------------
# TRAFFIC ALERTS
# -------------------------------------------------------------------
def analyze_traffic_conditions(threshold=70):
    """
    Detects cities where average congestion exceeds threshold.
    Returns list of traffic congestion alerts.
    """
    data = get_all_traffic_data()
    if not data:
        print("[WARN] No traffic data for alert analysis.")
        return []

    alerts = []
    for record in data:
        city = record.get("city", "Unknown")
        avg_speed = record.get("avg_speed", 0)
        accidents = record.get("accidents", 0)

        # Simple condition: high congestion + low average speed
        if avg_speed < threshold or accidents > 5:
            alert_msg = f"⚠️ Heavy traffic in {city}: avg speed {avg_speed} km/h, accidents {accidents}."
            alerts.append({
                "type": "traffic",
                "city": city,
                "message": alert_msg,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return alerts


# -------------------------------------------------------------------
# ACCIDENT ALERTS
# -------------------------------------------------------------------
def analyze_accident_spikes(days=3, spike_threshold=3):
    """
    Detects if accident counts exceed spike threshold over the last N days.
    Returns list of critical alerts.
    """
    data = get_accident_data(days=days)
    if not data:
        print("[WARN] No accident data for alert analysis.")
        return []

    city_counts = {}
    for record in data:
        city = record.get("city", "Unknown")
        city_counts[city] = city_counts.get(city, 0) + 1

    alerts = []
    for city, count in city_counts.items():
        if count >= spike_threshold:
            alerts.append({
                "type": "accident",
                "city": city,
                "message": f"🚨 Accident spike detected in {city}: {count} accidents in the last {days} days.",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return alerts


# -------------------------------------------------------------------
# COMBINED ALERT GENERATION
# -------------------------------------------------------------------
def generate_alerts():
    """
    Combines accident and traffic alerts into one list.
    """
    traffic_alerts = analyze_traffic_conditions()
    accident_alerts = analyze_accident_spikes()
    all_alerts = traffic_alerts + accident_alerts

    if not all_alerts:
        print("[INFO] No alerts generated. System stable.")
    else:
        print(f"[INFO] {len(all_alerts)} alerts generated.")

    return all_alerts


# -------------------------------------------------------------------
# TEST BLOCK
# -------------------------------------------------------------------
if __name__ == "__main__":
    print("[TEST] Running alert detection system...\n")

    alerts = generate_alerts()
    for alert in alerts:
        print(f"[{alert['type'].upper()}] {alert['message']} ({alert['timestamp']})")