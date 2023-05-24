# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# OBJETIVO  DE LA PRACTICA:
### Con el sensor KY-017 medir el mercurio en el ambiente.

# SENSOR: 
### KY-017

# CÓDIGO

```Python

import machine
import utime

sensor_pin = machine.Pin(7, machine.Pin.IN)

def detect_mercury():
    mercury_detected = False

    while True:
        if sensor_pin.value() == 0:
            mercury_detected = True
            print("Mercury detected!")
        else:
            mercury_detected = False

        utime.sleep(1)

detect_mercury()
  
```

## Autor (es): ANA LIZETH VILLALPANDO PRIETO

[Repositorio] (https://github.com/Danielusuario/Sensores-Raspberry-Pico/)

## Fecha de revisión:  
## 99/99/2023

# PRUEBAS

![](Imagenes/KY015.jpg)
