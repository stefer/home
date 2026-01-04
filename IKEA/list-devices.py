import dirigera
import sys

if len(sys.argv) != 3:
    print("Usage: python list-devices.py <IP_ADDRESS> <TOKEN>")
    sys.exit(1)

ip_address = sys.argv[1]
token = sys.argv[2]

dirigera_hub = dirigera.Hub(
    token=token,
    ip_address=ip_address
)
devices = dirigera_hub.get_all_devices()
for device in devices:
    print(f"Device Name: {device.attributes.custom_name}, Type: {device.type}, ID: {device.id}")