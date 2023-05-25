# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

## SENSOR: KY-032 AVOIDANCE
![](https://uelectronics.com/wp-content/uploads/2017/06/arduino-ky-032-modulo-sensor-de-evasion-de-obstaculos-v4.png)

## CÓDIGO
```python
import machine
import time

#Se definen los pines correspondientes para la entrada y salida de la senial
sensor_pin = machine.Pin(7, machine.Pin.IN)
enable_pin = machine.Pin(6, machine.Pin.OUT)

enable_pin.value(1)  # Habilita el sensor

#Evalua el sensor
while True:
    if sensor_pin.value() == 0:
        print("¡Obstáculo detectado!")
    else:
        print("Camino despejado")
    time.sleep(0.1)
```

### Autor (es): Cortes Hernandez Yuridia Saray 20210554

## PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-032.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION:
> 99/99/9999

## CONCLUSION:
> Este es un sensor que detecta obstalucos, sin embargo al momento de ponerlo a prueba lo complicado fue que detectara el propio objeto, ya que la mayoria de las veces a pesar de monstrar una cosa este no lo detectaa, hasta que se hizo algo de lo que no se dio cuenta y lo detectaba.
