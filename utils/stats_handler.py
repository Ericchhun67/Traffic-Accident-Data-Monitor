#
# stats_handler
#
# Eric Chhun
# 12/16/2025
# utils/stats_handler.py
"""
stats_handler.py
------------------------------------
Handles data analysis and statistics for traffic and accidents.

psudo code:
    - get overall traffic stats from db handler
    - get city-specific traffic stats from db handler 
    - get accident stats from db handler
    - compute trends over time 
    - summarize data for reporting 

Functions:
    - get_accident_stats()
    - get_traffic_stats()
    - calculate_city_summary()
    - calculate_accident_trends()
"""

import statistics
from datetime import datetime
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.db_handler import get_all_traffic_data, get_city_data, get_accident_data

# A function to summarize traffic stats for a specific city
def summarize_city_traffic(city_name):
    """Summarize traffic stats for a given city."""
    # get city traffic data from db handler and store in data variable
    data = get_city_data(city_name)
    # if no data is found, print warning message and return None stating
    # no traffic data for the city
    if not data:
        print(f"[WARN] No traffic data for {city_name}")
        return None
    # compute total records, average speed, and average accidents
    total_records = len(data)
    avg_speed = round(statistics.mean([d.get("avg_speed", 0) for d in data]), 2)
    avg_accidents = round(statistics.mean([d.get("accidents", 0) for d in data]), 2)
    # return summary dictionary with city name, total records, average speed, 
    # and average accidents
    return {
        "city": city_name,
        "total_records": total_records,
        "average_speed": avg_speed,
        "average_accidents": avg_accidents
    }

# A function to summarize accident data over the last N days
def summarize_accidents(days=7):
    """Summarize accident data over the last N days."""
    # get accident data from db handler for the specified number of days
    data = get_accident_data(days=days)
    
    if not data:
        print("[WARN] No accident data available.")
        return None
    # get the length of data and store in total variable
    total = len(data)
    # compute number of fatal accidents
    fatal = sum(1 for r in data if r.get("fatal", 0))
    # declare empty dictionary to hold daily counts
    daily = {}
    # interate through each record and count accidents per day
    for rec in data:
        date = rec.get("date", datetime.today().strftime("%Y-%m-%d"))
        # increment daily count for the data into a array
        daily[date] = daily.get(date, 0) + 1
    # return summary dictionary with total accidents
    return {
        "total_accidents": total,
        "fatal_accidents": fatal,
        "trend": sorted(daily.items())
    }

# A function to compute trend in accident counts over time
def compute_trend_over_time(days=30):
    """Compute percentage change in accident count vs previous period."""
    # get current and previous accident data from db handler
    current = get_accident_data(days=days)
    previous = get_accident_data(days=days * 2)
    # if no data found for current or previous period,
    if not current or not previous:
        # return trend 0 and status no data
        return {"trend": 0, "status": "No data"}
    # get lengths of current and previous data and store into 
    # curr_total and prev_total variables
    curr_total = len(current)
    prev_total = len(previous) - curr_total
    # if previous total is less than or equal to 0,
    if prev_total <= 0:
        # return trend 0 and status stable
        return {"trend": 0, "status": "Stable"}
    # compute precentage change and determine status increase 
    change = ((curr_total - prev_total) / prev_total) * 100
    # determine status based on change value
    status = "Increase" if change > 0 else "Decrease"
    # return trend dictionary with change and status
    return {"trend": round(change, 2), "status": status}

# A function to provide overall summary of traffic data
def overall_summary():
    """Return overall summary of traffic data."""
    # get all traffic data from db handler and store in traffic_data variable
    traffic_data = get_all_traffic_data()
    # if no traffic data found, print warning message and return None
    if not traffic_data:
        print("[WARN] No traffic data found.")
        return None

    total_records = len(traffic_data)
    cities = {t["city"] for t in traffic_data if t.get("city")}
    avg_speed = round(statistics.mean([t.get("avg_speed", 0) for t in traffic_data]), 2)
    avg_accidents = round(statistics.mean([t.get("accidents", 0) for t in traffic_data]), 2)

    return {
        "total_records": total_records,
        "unique_cities": len(cities),
        "average_speed": avg_speed,
        "average_accidents": avg_accidents
    }


if __name__ == "__main__":
    print("[TEST] Running statistics analysis...")
    print(summarize_city_traffic("San Francisco"))
    print(summarize_accidents(7))
    print(compute_trend_over_time())
    print(overall_summary())