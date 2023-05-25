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

[Link del Repositorio](https://github.com/Danielusuario/Sensores-Raspberry-Pico/)

## Fecha de revisión:  
## 99/99/2023

### PRUEBAS

## Circuito
![Image](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-015%20TEMP%20AND%20HUMIDITY.jpg)

## Corrida
![Image](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-015%20TEMP%20AND%20HUMIDITY%201.jpg)

# CONCLUSIONES
Fue bastante dificil de utilizar, ademas de hacer que marcara la temperatura y humedad debido a unos errores de sintaxis e instancias de clase
al momento de usarlo aplique calor pero no marcaba la temperatura.
