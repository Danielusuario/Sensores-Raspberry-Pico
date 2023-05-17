import machine
import time

sensor_pin = machine.Pin(17, machine.Pin.IN)

def calculate_heartbeat():
    heartbeat_count = 0
    heartbeat_start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), heartbeat_start) < 5000:
        if sensor_pin.value() == 1:
            heartbeat_count += 1
        time.sleep_ms(10)
    heartbeat_rate = (heartbeat_count / 5) * 60
    return heartbeat_rate

while True:
    heartbeat_rate = calculate_heartbeat()
    print("Heartbeat rate:", heartbeat_rate)
    time.sleep(1)
