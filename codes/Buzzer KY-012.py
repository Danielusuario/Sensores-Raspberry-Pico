#Buzzer KY-012
#Benitez Solorzano Paola

from machine import Pin, PWM
from utime import sleep

ky006 = PWM(Pin(0))
ky006.freq(500)
ky006.duty_u16(1000)
sleep(1)
ky006.duty_u16(0)





