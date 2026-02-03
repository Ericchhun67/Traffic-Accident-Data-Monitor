# utils/simulation_handler.py
"""
simulation_handler.py
------------------------------------
Handles car movement, traffic light logic, and flow updates for the
Traffic Flow Simulation page.

Functions:
    - get_traffic_light_state()
    - update_car_positions()
    - run_simulation_step()
"""

import random
import time

# ligght cycle and timing definitions 
light_cycle = ["RED", "GREEN", "YELLOW"]
light_timer = {"RED": 5, "GREEN": 6, "YELLOW": 2}
current_light = "RED"
last_switch = time.time()

# A function to get the current traffic light state
def get_traffic_light_state():
    """
    Returns the current traffic light color based on time elapsed.
    Automatically switches between RED -> GREEN -> YELLOW -> RED.
    """
    # global variables to track current light and last switch time
    global current_light, last_switch
    now = time.time()
    elapsed = now - last_switch

    # If the current light duration has passed, move to the next
    if elapsed >= light_timer[current_light]:
        # find the next light in the cycle
        current_index = light_cycle.index(current_light)
        # get the next light in the cycle
        next_light = light_cycle[(current_index + 1) % len(light_cycle)]
        # update global variables for current light and last switch time
        current_light = next_light
        last_switch = now
        # print light change for debugging
        print(f"🚦 Light changed to {current_light}")
    # return the current light color
    return current_light

# A function to update car positions based on light state
def update_car_positions(car_positions, speed=2):
    """
    Moves cars based on current light color.

    Args:
        car_positions (list): Current positions of cars on the road (pixels).
        speed (int): Movement speed per simulation step.

    Returns:
        Updated list of car positions.
    """
    
    # get current traffic light state
    light = get_traffic_light_state()
    # list to hold updated car positions in an empty list
    updated_positions = []
    # iterate through each car position and update based on light
    for pos in car_positions:
        # if light is green, 
        if light == "GREEN":
            new_pos = pos + speed  # Move forward
        # if light is yellow,
        elif light == "YELLOW":
            new_pos = pos + (speed * 0.5)  # Slow down
        else:
            new_pos = pos  # Stop on RED light
        # append new position to updated positions list
        updated_positions.append(new_pos)
    # return the updated car positions
    return updated_positions

# A function to run one step of the traffic simulation
def run_simulation_step(car_positions):
    """
    Simulates one step of traffic movement.
    Returns updated car positions + light state.
    """
    # update car positions based on current light state
    new_positions = update_car_positions(car_positions)
    return {
        "light": get_traffic_light_state(),
        "car_positions": new_positions
    }



if __name__ == "__main__":
    # cars start at positions 0, 30, 60 declared in a list
    car_positions = [0, 30, 60]
    # print starting message to the console
    print("Starting Traffic Simulation... 🚗💨")
    # loop to run multiple simulation steps
    for _ in range(20):
        # run one simulation step and get the new state and 
        # store in state variable
        state = run_simulation_step(car_positions)
        car_positions = state["car_positions"]
        print(f"Light: {state['light']}, Cars: {car_positions}")
        time.sleep(1)