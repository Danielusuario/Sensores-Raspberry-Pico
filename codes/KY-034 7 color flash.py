import machine
import time

red_pin = machine.Pin(16, machine.Pin.OUT)
green_pin = machine.Pin(17, machine.Pin.OUT)
blue_pin = machine.Pin(18, machine.Pin.OUT)

def set_color(red, green, blue):
    red_pin.value(red)
    green_pin.value(green)
    blue_pin.value(blue)

while True:
    set_color(1, 0, 0) # Red
    time.sleep(1)
    set_color(0, 1, 0) # Green
    time.sleep(1)
    set_color(0, 0, 1) # Blue
    time.sleep(1)
    set_color(1, 1, 0) # Yellow
    time.sleep(1)
    set_color(1, 0, 1) # Magenta
    time.sleep(1)
    set_color(0, 1, 1) # Cyan
    time.sleep(1)
    set_color(1, 1, 1) # White
    time.sleep(1)
