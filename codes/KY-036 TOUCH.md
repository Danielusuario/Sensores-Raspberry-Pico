#Sensor touch KY-036
#Benitez Solorzano Paola

import machine
import time

# Configurar el pin de entrada del sensor
sensor_pin = machine.Pin(3, machine.Pin.IN)

# Función para manejar el evento de pulsación
def handle_touch(pin):
    print("¡Tocado!")

# Configurar el evento de interrupción para detectar el toque
sensor_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=handle_touch)

# Bucle principal
while True:
    time.sleep(1)
