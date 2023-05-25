# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# SENSOR: KY-024 LINEAR HALL

# CÓDIGO
```python
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
```

## Autor (es): Benitez Solorzano Paola

# PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-024%20LINEAR%20HALL.jpg)
![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-024%20LINEAR%20HALL1.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION: 
> 99/99/9999

## CONCLUSION: 
> Este sensor consiste en colocar algo metalico con el fin de que calculara el valor magnetico que tenia este. En este caso se uso un destornillador para hacer esta practica. 
