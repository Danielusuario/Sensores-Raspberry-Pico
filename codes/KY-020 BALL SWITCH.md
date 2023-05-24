# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# OBJETIVO  DE LA PRACTICA:
### Con el sensor KY-020 medir la intensidad de la luz y encender y apagar el led cuando eso suceda

# SENSOR: 
### KY-020

# CÓDIGO

```Python

import machine
#Configuración del pin
pin_interruptor = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
  if pin_interruptor.value() == 1:
    print("El interruptor de bola esta activado")
  else:
    print("El interruptor de bola esta desactivado")
```

## Autor (es): ANA LIZETH VILLALPANDO PRIETO

[Repositorio] (https://github.com/Danielusuario/Sensores-Raspberry-Pico/)

## Fecha de revisión:  
## 99/99/2023

### PRUEBAS

![Imagen prueba 1](Imagenes/KY015.jpg)
![Imagen prueba 2](Imagenes/KY015.jpg)

# CONCLUSIONES
