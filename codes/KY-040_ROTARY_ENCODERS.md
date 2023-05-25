# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

## SENSOR: KY-040 ROTARY ENCODERS
![](https://components101.com/sites/default/files/components/KY-040-Rotary-Encoder-Module.jpg)

## CÓDIGO
```python
import machine
import time

# Configurar el pin GP14 como entrada
switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    # Leer el estado del interruptor
    estado = switch.value()

    if estado == 0:
        print("El interruptor está presionado")
    else:
        print("El interruptor está abierto")

    time.sleep(0.1)
```

### Autor (es): Cortes Hernandez Yuridia Saray 20210554

## PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-040.jpg)
## FECHA DE REVISION:
> 99/99/999

## REPOSITORIO:
>https://github.com/Danielusuario/Sensores-Raspberry-Pico

## CONCLUSION:
> Confusion parasaber si tan solo era girar la pieza del sensor, o tambien aplastarlo, ya que segun mi entender se podia rotar de un lado a otro y tambien presionar, sin embargo se represento lo mostrado.
