# home

Home automation experiments

Ideas:

- Turn off water pump when basement floor is flooded
- Warn when water pump runs too often (need to fill air into the tank)

## Turn off water pump when basement floor is flooded

I Used an IKEA water sensor to turn off an IKEA smart plug. However, I need a fixed electrical solution for turning off the water pump.

## Warn when water pump runs too often

I can use a smart plug to monitor the power consumption of the water pump. If it runs too often, I can send a notification. I can use an IKEA smart plug to experiment with this idea.

## Getting started

I use [Leggin/dirigera python library](https://github.com/Leggin/dirigera) to control IKEA Dirigera devices.

Use this command to generate a token for the IKEA Dirigera hub:

```bash
generate-token
```

It will ask for the IP address of the hub and instruct you to press the button on the hub.
