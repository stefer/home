# home

Home automation experiments

Ideas:

- Turn off water pump when basement floor is flooded
- Warn when water pump runs too often (need to fill air into the tank)

## Turn off water pump when basement floor is flooded

I Used an IKEA water sensor to turn off an IKEA smart plug. However, I need a fixed electrical solution for turning off the water pump.

## Warn when water pump runs too often

I can use a smart plug to monitor the power consumption of the water pump. If it runs too often, I can send a notification. I can use an IKEA smart plug to experiment with this idea.

Using the `events_listener.py` script in the `IKEA` folder, I can listen for events from the IKEA Dirigera hub.

This event is sent when the load of the smart plug changes:

```json
 {
    "id":"bcf40546-ab91-4787-a0bc-fdf9570d351b",
    "time":"2026-01-04T21:45:00.153Z",
    "specversion":"3.178.0",
    "source":"urn:com:ikea:homesmart:iotc:zigbee",
    "type":"deviceStateChanged",
    "data":{
        "id":"37fd72f2-de40-4b61-803b-8b6914d403a7_1",
        "type":"outlet",
        "deviceType":"outlet",
        "createdAt":"2026-01-03T17:14:19.000Z",
        "isReachable":true,
        "lastSeen":"2026-01-04T21:45:00.000Z",
        "attributes":{
            "currentAmps":0.01600000075995922
        },
        "remoteLinks":[]
    }
}
```

## Getting started

I use [Leggin/dirigera python library](https://github.com/Leggin/dirigera) to control IKEA Dirigera devices.

Use this command to generate a token for the IKEA Dirigera hub:

```bash
generate-token
```

It will ask for the IP address of the hub and instruct you to press the button on the hub.
