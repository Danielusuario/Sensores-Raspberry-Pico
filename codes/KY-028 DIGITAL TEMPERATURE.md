# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

# SENSOR: KY-028 DIGITAL TEMPERATURE

# CÓDIGO
```python
import machine
import utime

# Configura el pin del sensor KY-028
sensor_pin = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Bucle principal
while True:
    # Lee el valor del sensor
    sensor_value = sensor_pin.value()

    # Calcula la temperatura en grados Celsius
    voltage = (sensor_value / 65535) * 3.3  # Convierte el valor a voltaje (0-3.3V)
    temperature = (voltage - 0.5) * 100  # Convierte el voltaje a temperatura en grados Celsius

    # Imprime el valor de la temperatura
    print("Temperatura: {:.2f} °C".format(temperature))

    # Espera 1 segundo antes de la siguiente lectura
    utime.sleep(1)
```

## Autor (es): Benitez Solorzano Paola

# PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-028%20DIGITAL%20TEMPERATURE.jpg)
![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-028%20DIGITAL%20TEMPERATURE1.jpg)

## REPOSITORIO: 
> https://github.com/Danielusuario/Sensores-Raspberry-Pico

## FECHA DE REVISION: 
> 99/99/9999

## CONCLUSION: 
> En lo personal, este sensor no se pudo observar mucho de su funcionalidad porque necesita estar en cambios de temperatura muy notables. Como frio o calor.







    
