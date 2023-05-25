# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# SENSOR: KY-003 HALL MAGNETIC

# CÓDIGO
```python
from machine import Pin
import utime

sensor=Pin(26, Pin.IN)

while True:
    if sensor.value()==1:
        print("Se detecto un campo magnetico")
        utime.sleep(1)   
    else:
        print("Ningun campo detectado")
        utime.sleep(1)
utime.sleep(1)
```

## Autor (es): Rodriguez Ledesma Ricardo

# PRUEBAS

![Image](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-003HallMagnetic.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION: 
> 99/99/9999

# CONCLUSIÓN
Este sensor fue de los mas sencillos, simplemente al conectar el sensor, ya estaba detectando un campo magnetico cerca, debido a que se encontraba el computador cerca del mismo, por lo cual, se logro hacer funcionar el sensor con exito.

