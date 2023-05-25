# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# SENSOR: KY-036 TOUCH

# CÓDIGO
```python
import machine
import time

# Configurar el pin de entrada del sensor
sensor_pin = machine.Pin(3, machine.Pin.IN)

# Función para manejar el evento de pulsación
def handle_touch(pin):
    print("¡Tocado!")

# Configurar el evento de interrupción para detectar el toque
sensor_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=handle_touch)

# Bucle principal
while True:
    time.sleep(1)
```

## Autor (es): Benitez Solorzano Paola

# PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-036%20TOUCH.jpg)
![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-036%20TOUCH1.jpg)
![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-036%20TOUCH2.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION: 
> 99/99/9999

## CONCLUSION: 
> Este sensor consiste en tocar la punta de forma redonda que tiene. Lo cual una vez tocando ligeramente esa parte el sensor lo va a detectar y lanzara un mensaje de !Tocado!.
