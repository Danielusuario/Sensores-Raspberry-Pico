#KY-021 MINI SWITCH
#Cortes Hernandez Yuridia Saray

import machine
import time

# Configurar el pin GP14 como entrada
switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    # Leer el estado del interruptor
    estado = switch.value()

    if estado == 0:
        print("El interruptor está presionado")
    else:
        print("El interruptor está abierto")

    time.sleep(0.1)


