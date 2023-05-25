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

![Image](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-022IrReceiver.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION: 
> 99/99/9999

# CONCLUSIÓN
Este sensor fue de código corto, en cuanto lo conectamos y lo corrimos, nos detecto una señal infrarroja cerca, por lo cual, esta practica se completo con exito.
