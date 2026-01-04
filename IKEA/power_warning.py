import dirigera
import sys
import json
from typing import Any
from datetime import datetime, timedelta
from collections import deque

if len(sys.argv) != 3:
    print("Usage: python power_warning.py <IP_ADDRESS> <TOKEN>")
    sys.exit(1)

ip_address = sys.argv[1]
token = sys.argv[2]

dirigera_hub = dirigera.Hub(
    token=token,
    ip_address=ip_address
)

# Global list to store power events (device_id, timestamp, current_amps, is_on)
# Using deque for efficient removal of old entries
power_events = deque()
RETENTION_HOURS = 4
POWER_THRESHOLD = 0.01  # Amps
MAX_ENGAGEMENTS_PER_HOUR = 5

def cleanup_old_events():
    """Remove events older than RETENTION_HOURS"""
    cutoff_time = datetime.now() - timedelta(hours=RETENTION_HOURS)
    while power_events and power_events[0][1] < cutoff_time:
        power_events.popleft()

def check_excessive_engagements():
    """
    Check for each device if the number of times it has been switched on per hour
    has exceeded MAX_ENGAGEMENTS_PER_HOUR.
    
    Returns:
        dict: Dictionary mapping device_id to count of on-switches for devices 
              that exceeded the threshold
    """
    one_hour_ago = datetime.now() - timedelta(hours=1)
    device_on_counts = {}
    
    # Count "on" events (is_on=True) per device in the last hour
    for device_id, timestamp, current_amps, is_on in power_events:
        if timestamp >= one_hour_ago and is_on:
            device_on_counts[device_id] = device_on_counts.get(device_id, 0) + 1
    
    # Filter devices that exceeded the threshold
    excessive_devices = {
        device_id: count 
        for device_id, count in device_on_counts.items() 
        if count > MAX_ENGAGEMENTS_PER_HOUR
    }
    
    return excessive_devices

def on_message(ws: Any, message: str):
    message_dict = json.loads(message)
    data = message_dict["data"]
    if (message_dict["type"] != "deviceStateChanged" or data["deviceType"] != "outlet"):
        return
    
    id = data["id"]
    attributes = data["attributes"]
    # Check if attribute currentAmp exists and is a doublevalue greater than threshold
    if "currentAmps" not in attributes or not isinstance(attributes["currentAmps"], (int, float)):
        return
    
    threshold = POWER_THRESHOLD
    current_amps = attributes["currentAmps"]
    timestamp = datetime.now()
    is_on = current_amps > threshold
    
    # Add event to global list
    power_events.append((id, timestamp, current_amps, is_on))
    cleanup_old_events()
    
    if is_on:
        print(f"Outlet {id} is ON, AMP is {current_amps} at {timestamp}")
    else:
        print(f"Outlet {id} is OFF, AMP is {current_amps} at {timestamp}")
        
    excessive = check_excessive_engagements()
    if excessive:
        for device_id, count in excessive.items():
            print(f"Warning: Device {device_id} switched on {count} times in the last hour")

def on_error(ws: Any, message: str):
    print(f"ERROR:{message}")

dirigera_hub.create_event_listener(
    on_message=on_message, on_error=on_error
)
