# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

## SENSOR: KY-031 TAP MODULE
![](https://m.media-amazon.com/images/I/51ikIa1F-JL._AC_UF1000,1000_QL80_.jpg)

## CÓDIGO
```python
import machine
import utime

# Configuración del pin
sensor_pin = machine.Pin(2, machine.Pin.IN)

# Función para detectar los golpes
def detectar_golpe(pin):
    print("¡Golpe detectado!")

# Configurar interrupción en el pin
sensor_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=detectar_golpe)

# Bucle principal
while True:
    utime.sleep(1)
```

### Autor (es): Cortes Hernandez Yuridia Saray 20210554

## PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-031.png)


## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION:
> 99/99/9999

## CONCLUSION:
> La finalidad de este sensor es detectar choques, por lo que al recibir un impacto este reacciona y lanza un mensaje donde avisa que ha resivido un golpe.
