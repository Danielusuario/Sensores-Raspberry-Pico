# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# OBJETIVO  DE LA PRACTICA:
### Con el sensor KY-015 medir la temperatura y humedad del ambiente.

# SENSOR: 
### KY-015

# CÓDIGO

```Python

from machine import Pin, I2C
import utime as time
from dht import DHT11

while True:
    time.sleep(3)
    pin = Pin(0, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature())
    h = (sensor.humidity())
    print("Temperature: " + str(t))
    print("Humidity: " + str(h))

```

## Autor (es): ANA LIZETH VILLALPANDO PRIETO

[Repositorio] (https://github.com/Danielusuario/Sensores-Raspberry-Pico/)

## Fecha de revisión:  
## 99/99/2023

### PRUEBAS

![](Imagenes/KY015.jpg)

# CONCLUSIONES
La utilización de este sensor es bastante compleja pero es de mucha utilidad en la vida cotidiana.
