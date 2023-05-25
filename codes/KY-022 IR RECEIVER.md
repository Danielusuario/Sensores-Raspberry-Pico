# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# SENSOR: KY-022 IR RECEIVER

# CÓDIGO
```python
import machine

# Configura el pin GPIO
sensor_pin = machine.Pin(26, machine.Pin.IN) 

# Lee el estado del sensor IR
while True:
    if sensor_pin.value():
        print("Señal infrarroja detectada")
```

## Autor (es): Rodriguez Ledesma Ricardo

# PRUEBAS

![]()

