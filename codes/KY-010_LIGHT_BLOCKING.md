#KY-010 LIGHT BLOCKING
#Cortes Hernandez Yuridia Saray

import machine

# Configura el pin del sensor KY-010
sensor_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

# Función para manejar la interrupción de luz
def light_interrupt(pin):
    if pin.value() == 0:
        print("¡Se ha detectado la interrupción de luz!")
    else:
        print("Luz restaurada")

# Configura la interrupción en el pin del sensor
sensor_pin.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=light_interrupt)

# Bucle principal
while True:
    pass
