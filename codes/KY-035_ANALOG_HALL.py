#KY-035 ANALOG HALL
#Cortes Hernandez Yuridia Saray

import machine
import utime

# Configuración del pin de entrada analógica
analog_pin = machine.ADC(26)

# Función para leer el valor analógico del sensor
def read_analog_value():
    raw_value = analog_pin.read_u16()
    return raw_value

# Bucle principal
while True:
    # Leer el valor analógico del sensor
    sensor_value = read_analog_value()

    # Imprimir el valor del sensor
    print("Valor del sensor: ", sensor_value)

    # Esperar un segundo
    utime.sleep(1)

