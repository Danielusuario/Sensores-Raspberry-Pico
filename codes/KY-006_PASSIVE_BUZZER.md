# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

## SENSOR: KY-006 PASSIVE BUZZER
![](https://uelectronics.com/wp-content/uploads/AR0026-Sensor-KY-006-Zumbador-Buzzer-2.jpg)

## CÓDIGO
```python
from machine import Pin, PWM
from utime import sleep

ky006 = PWM(Pin(0))
ky006.freq(500)
ky006.duty_u16(1000)
sleep(1)
ky006.duty_u16(0)
```

### Autor (es): Cortes Hernandez Yuridia Saray 20210554

## PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-006.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION: 
> 99/99/9999

## CONCLUSION: 
> En lo personal, para este sensor lo que fue complicado, a aprte de que fue el primer sensor en realizar, la parte fisica para conectar cada cosa a la pico w fue lo mas complicado.
