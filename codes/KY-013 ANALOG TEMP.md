# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# SENSOR: KY-013 ANALOG TEMP

# CÓDIGO
```python
import machine

# Configura el pin ADC
sensor_pin = machine.ADC(26) 

# Lee el valor del sensor
sensor_value = sensor_pin.read_u16()

# Calcula la temperatura en grados Celsius
voltage = sensor_value * 3.3 / 65535  # Convierte el valor ADC a voltaje
temperature = (voltage - 0.5) * 100  # Convierte el voltaje a temperatura

# Muestra el valor de la temperatura
print("Temperatura: {:.2f}°C".format(temperature))
```

## Autor (es): Rodriguez Ledesma Ricardo

# PRUEBAS

![Image](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-013AnalogTemp.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION: 
> 99/99/9999

# CONCLUSIÓN
Este sensor también fue sencillo, ya que funciona como es un sensor de temperatura, simplemente al verificar los cables y el código, al correrlo ya nos habia arrojado un resultado inmediato.


