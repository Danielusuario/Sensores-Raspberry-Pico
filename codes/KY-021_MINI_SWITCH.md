# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

## SENSOR: KY-021 MINI SWITCH
![](https://uelectronics.com/wp-content/uploads/AR0039-Sensor-KY-021-Mini-interruptor-Magnetico-v2.jpg)

## CÓDIGO
```python
import machine
import time

# Configurar el pin GP14 como entrada
switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    # Leer el estado del interruptor
    estado = switch.value()
    #Se determina el estado del interruptor
    if estado == 0:
        print("El interruptor está presionado")
    else:
        print("El interruptor está abierto")

    time.sleep(0.1)
```

### Autor (es): Cortes Hernandez Yuridia Saray 20210554

## PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-021.png)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION:
> 99/99/9999

## CONCLUSION:
> La dificultad aqui ue encontrar un material para poder ponerlo a prueba, sin embargo se puedo con un desarmador.
