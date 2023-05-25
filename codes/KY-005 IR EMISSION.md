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

![Image](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-005IrEmission.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION: 
> 99/99/9999

# CONCLUSIÓN
Este sensor fue algo sencillo, aunque en un principio se conectaba el sensor pero no arrojaba resultados, después de revisar el cableado, nos percatamos de que el error se encontraba en un cable mal conectado, por lo cual después de corregirlo, el sensor funciono con exito. 
