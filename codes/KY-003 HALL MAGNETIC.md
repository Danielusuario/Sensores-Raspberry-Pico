from machine import Pin
import utime

sensor=Pin(26, Pin.IN)

while True:
    if sensor.value()==1:
        print("Se detecto un campo magnetico")
        utime.sleep(1)   
    else:
        print("Ningun campo detectado")
        utime.sleep(1)
utime.sleep(1)
