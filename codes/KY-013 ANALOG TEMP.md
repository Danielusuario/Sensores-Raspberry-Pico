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

![]()

