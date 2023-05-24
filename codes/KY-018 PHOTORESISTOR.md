# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# OBJETIVO  DE LA PRACTICA:
### Con el sensor KY-015 medir la temperatura y humedad del ambiente.

# SENSOR: 
### KY-015

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

[Repositorio] (https://github.com/Danielusuario/Sensores-Raspberry-Pico/)

## Fecha de revisión:  
## 99/99/2023

# PRUEBAS

![](https://www.snapon.co.za/images/thumbs/default-image_550.png)
