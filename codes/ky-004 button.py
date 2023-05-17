import machine
import time

button_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button_pin.value() == 0:
        print("Button Pressed")
    time.sleep(0.1)
