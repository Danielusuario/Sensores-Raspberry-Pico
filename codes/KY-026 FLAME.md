# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# SENSOR: KY-026 FLAME

# CÓDIGO
```python
from machine import Pin
import utime

flame_sensor = Pin(16, Pin.IN)
utime.sleep(2)

while True:
   if flame_sensor.value() == 1:
       print("Flame Detected")
       utime.sleep(3)
   else:
       print("No Flame")
       utime.sleep(1)
utime.sleep(0.1)
```

## Autor (es): Benitez Solorzano Paola

# PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-028%20DIGITAL%20TEMPERATURE.jpg)
![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-028%20DIGITAL%20TEMPERATURE1.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION: 
> 99/99/9999

## CONCLUSION: 
> Este sensor fue muy sencillo y muy divertido por hacer, ya que solo requeria un encendedor para indicar si hay fuego o no.
