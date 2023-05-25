#KY-032 AVOIDANCE
#Cortes Hernandez Yuridia Saray


import machine
import time

sensor_pin = machine.Pin(7, machine.Pin.IN)
enable_pin = machine.Pin(6, machine.Pin.OUT)

enable_pin.value(1)  # Habilitar el sensor

while True:
    if sensor_pin.value() == 0:
        print("¡Obstáculo detectado!")
    else:
        print("Camino despejado")
    time.sleep(0.1)

