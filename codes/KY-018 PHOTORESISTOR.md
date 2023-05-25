# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# OBJETIVO  DE LA PRACTICA:
### Con el sensor KY-018 medir la luz / luminiscencia en el ambiente.

# SENSOR: 
### KY-018

# CÓDIGO

```Python

import machine
import time

#Configuración del pin
pin_fotoresistor = machine.ADC(26)

while True:
  valor_analogico = pin_fotoresistor.read_u16()
  print("Valor analógico: ", valor_analogico)
  time.sleep(1)
  
```

## Autor (es): ANA LIZETH VILLALPANDO PRIETO

[Link del Repositorio](https://github.com/Danielusuario/Sensores-Raspberry-Pico/)

## Fecha de revisión:  
## 99/99/2023

# PRUEBAS

![Image](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-018%20FOTORESISTOR.png)

# CONCLUSIONES
La utilización de este sensor no fue sencillo de realizar, pero buscando en diferentes foros y videos se pudo lograr con exito, ademas este es bastante util
y lo utilizamos en diferentes aparatos tecnologicos sin darnos cuenta.

