#Sensor Linear hall KY-024
#Benitez Solorzano Paola

import machine
import time

# Configurar el pin ADC0 (GP26) como entrada analógica
adc = machine.ADC(26)

while True:
    # Leer el valor analógico del pin ADC0 y convertirlo a voltaje
    sensor_value = adc.read_u16()
    voltage = sensor_value * 3.3 / 65535  # Rango de conversión de 16 bits

    # Imprimir el valor analógico y el voltaje en la consola
    print("Valor analógico:", sensor_value)
    print("Voltaje:", voltage, "V")

    # Esperar 1 segundo antes de la siguiente lectura
    time.sleep(1)
