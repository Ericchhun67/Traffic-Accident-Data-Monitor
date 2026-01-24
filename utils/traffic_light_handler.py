# utils/traffic_light_handler.py
"""
traffic_light_handler.py
------------------------------------
Simulates an intersection traffic light system.
Controls lights for north-south and east-west lanes,
so cars stop or go accordingly.

Functions:
    - get_intersection_state()
    - update_lights()
    - get_light_color(direction)
    - run_intersection_cycle()
"""

import time


lights = {
    "north_south": "GREEN",   # cars going vertically
    "east_west": "RED"        # cars going horizontally
}

# Timers (in seconds)
light_durations = {
    "GREEN": 7,
    "YELLOW": 2,
    "RED": 7
}

# Track when the light last changed
last_switch_time = time.time()


def update_lights():
    """
    Automatically updates both light directions based on timing.
    The two lights always have opposite states.
    """
    global lights, last_switch_time
    now = time.time()
    elapsed = now - last_switch_time

    current_main = lights["north_south"]

    if elapsed >= light_durations[current_main]:
        # Change north-south → next color
        if current_main == "GREEN":
            lights["north_south"] = "YELLOW"
            lights["east_west"] = "RED"
        elif current_main == "YELLOW":
            lights["north_south"] = "RED"
            lights["east_west"] = "GREEN"
        elif current_main == "RED":
            lights["north_south"] = "GREEN"
            lights["east_west"] = "RED"

        last_switch_time = now
        print(f"🚦 Lights updated: NS={lights['north_south']}, EW={lights['east_west']}")



def get_light_color(direction):
    """
    Returns current color for a given direction (north_south or east_west).
    """
    update_lights()
    return lights.get(direction, "RED")


def get_intersection_state():
    """
    Returns full intersection light state.
    Example:
    {
        "north_south": "GREEN",
        "east_west": "RED",
        "timestamp": 1705273200.0
    }
    """
    update_lights()
    return {
        "north_south": lights["north_south"],
        "east_west": lights["east_west"],
        "timestamp": time.time()
    }



def run_intersection_cycle(cycles=5):
    """
    Runs multiple light cycles to test timing.
    """
    print("Starting intersection traffic light simulation... 🚦")
    for _ in range(cycles):
        state = get_intersection_state()
        print(f"NS={state['north_south']} | EW={state['east_west']}")
        time.sleep(1)


if __name__ == "__main__":
    run_intersection_cycle(25)