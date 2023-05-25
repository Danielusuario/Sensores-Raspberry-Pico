# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# SENSOR: KY-012 BUZZER

# CÓDIGO
```python
from machine import Pin, PWM
from utime import sleep

ky012 = PWM(Pin(0))
ky012.freq(500)
ky012.duty_u16(1000)
sleep(1)
ky012.duty_u16(0)
```

## Autor (es): Benitez Solorzano Paola

# PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-012%20BUZZER.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION: 
> 99/99/9999

## CONCLUSION: 
> Este sensor fue el primero, se parecia mucho al pasive buzzer de que ambos mostraban un ruido al momento de encenderlo. 
