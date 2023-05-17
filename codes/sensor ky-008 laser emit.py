import machine
import time

laser_pin = machine.Pin(16, machine.Pin.OUT)

def turn_on_laser():
    laser_pin.value(1)

def turn_off_laser():
    laser_pin.value(0)

while True:
    turn_on_laser()
    time.sleep(1)
    turn_off_laser()
    time.sleep(1)
