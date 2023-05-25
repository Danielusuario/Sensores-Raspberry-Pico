# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# SENSOR: 
## KY-006 PASSIVE BUZZER

# CÓDIGO
```python
from machine import Pin, PWM
from utime import sleep

ky006 = PWM(Pin(0))
ky006.freq(500)
ky006.duty_u16(1000)
sleep(1)
ky006.duty_u16(0)
```

## Autor (es): CORTES HERNANDEZ YURIDIA SARAY 20210554

# PRUEBAS

![](KY-006.jpg)


