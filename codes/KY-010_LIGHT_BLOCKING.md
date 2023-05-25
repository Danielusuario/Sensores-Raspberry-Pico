# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

## SENSOR: KY-010 LIGHT BLOCKING
![](https://arduinomodules.info/wp-content/uploads/ky-010_Photo_interrupter_arduino_module.jpg)

## CÓDIGO
```python
import machine

# Configura el pin del sensor KY-010
sensor_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

# Función para manejar la interrupción de luz
def light_interrupt(pin):
    if pin.value() == 0:
        print("¡Se ha detectado la interrupción de luz!")
    else:
        print("Luz restaurada")

# Configura la interrupción en el pin del sensor
sensor_pin.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=light_interrupt)

# Bucle principal
while True:
    pass
```

### Autor (es): Cortes Hernandez Yuridia Saray 20210554

## PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-010.jpg)

## FECHA DE REVISION:
> 99/99/999

## REPOSITORIO:
>https://github.com/Danielusuario/Sensores-Raspberry-Pico

## CONCLUSION:
> Para este saber la funcion como tal y llevarla a cabo para saber si realmente funcionaba fue la dificultad.
