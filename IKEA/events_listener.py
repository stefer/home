import dirigera
import sys
import json
from typing import Any

if len(sys.argv) != 3:
    print("Usage: python list-devices.py <IP_ADDRESS> <TOKEN>")
    sys.exit(1)

ip_address = sys.argv[1]
token = sys.argv[2]

dirigera_hub = dirigera.Hub(
    token=token,
    ip_address=ip_address
)

def on_message(ws: Any, message: str):
    message_dict = json.loads(message)
    data = message_dict["data"]
    print(f"Event {message_dict['type']}, attributes: {data['attributes']} \r\n {data}")

def on_error(ws: Any, message: str):
    print(message)

dirigera_hub.create_event_listener(
    on_message=on_message, on_error=on_error
)
