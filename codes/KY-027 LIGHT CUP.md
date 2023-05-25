# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# OBJETIVO  DE LA PRACTICA:
### Con el sensor KY-027 medir la intensidad de la luz y encender y apagar el led cuando eso suceda

# SENSOR: 
### KY-020

# CÓDIGO

```Python

import machine
import utime

sensor_pin = machine.Pin(15, machine.Pin.IN)
led_pin = machine.Pin(0, machine.Pin.OUT)

def measure_light_intensity():
    while True:
        light_intensity = sensor_pin.value()
        print("Light intensity:", light_intensity)

        if light_intensity > 0: 
            led_pin.on()
        else:
            led_pin.off()

        utime.sleep(1)

measure_light_intensity()

```

## Autor (es): ANA LIZETH VILLALPANDO PRIETO

[Repositorio](https://github.com/Danielusuario/Sensores-Raspberry-Pico/)

## Fecha de revisión:  
## 99/99/2023

### PRUEBAS

## Circuito
![Image](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-027%20LIGHT%20CUP.jpg)

## Corrida
![Image](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-027%20LIGHT%20CUP1.jpg)

# CONCLUSIONES
Un sensor que es de ayuda y me imagino podria ser de aviso en caso de sismos, al momento de realizar la implementacion
fue bastante dificil pero con un esfuerzo se pudo lograr
