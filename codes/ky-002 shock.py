import machine
import time

shock_pin = machine.Pin(16, machine.Pin.IN)

while True:
    if shock_pin.value() == 1:
        print("Shock Detected")
    time.sleep(0.1)
