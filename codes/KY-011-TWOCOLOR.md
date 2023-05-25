# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

## SENSOR: KY-011 TWO COLORS
![](https://uelectronics.com/wp-content/uploads/2017/06/Ky-011-V2.jpg)

## CÓDIGO
```python

import utime

# Configuración de los pines
pin_rojo = machine.Pin(2, machine.Pin.OUT)
pin_verde = machine.Pin(3, machine.Pin.OUT)

# Función para establecer el color del LED de dos colores
def establecer_color(color_rojo, color_verde):
    pin_rojo.value(color_rojo)
    pin_verde.value(color_verde)

try:
    while True:
        # Enciende el LED en color rojo
        establecer_color(1, 0)  # Rojo
        utime.sleep(1)

        # Enciende el LED en color verde
        establecer_color(0, 1)  # Verde
        utime.sleep(1)

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario.")

finally:
    # Apaga el LED
    establecer_color(0, 0)
```

### Autor (es): Cortes Hernandez Yuridia Saray 20210554

## PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-011%20TWOCOLOR(2).JPG.png)
![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-011%20TWOCOLOR.JPG.png)
## FECHA DE REVISION:
> 99/99/999

## REPOSITORIO:
>https://github.com/Danielusuario/Sensores-Raspberry-Pico

## CONCLUSION:
> ES UN SENSOR SENCILLO DE USAR YA QUE SU FUNCION PRINCIPAL ES PRACTICAMENTE LA DE UN LED NORMAL, SOLO QUE NO ES LA FUNCION DE UN RGB YA QUE SOLO CUENTA CON SOLO DOS COLORES A UTILIZAR.
