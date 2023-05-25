# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# SENSOR: KY-005 IR EMISSION

# CÓDIGO
```python
from machine import Pin
from utime import sleep_ms
ir=Pin(21,Pin.IN)
while True:
    try:
        print(ir.value())
        sleep_ms(100)
        
    except KeyboardInterrupt:
        break
```

## Autor (es): Rodriguez Ledesma Ricardo

# PRUEBAS

![]()

