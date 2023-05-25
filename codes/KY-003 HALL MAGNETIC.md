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

![]()

