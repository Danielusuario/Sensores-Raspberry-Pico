#KY-031 TAP MODULE
#Cortes Hernandez Yuridia Saray

import machine
import utime

# Configuración del pin
sensor_pin = machine.Pin(2, machine.Pin.IN)

# Función para detectar los golpes
def detectar_golpe(pin):
    print("¡Golpe detectado!")

# Configurar interrupción en el pin
sensor_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=detectar_golpe)

# Bucle principal
while True:
    utime.sleep(1)
