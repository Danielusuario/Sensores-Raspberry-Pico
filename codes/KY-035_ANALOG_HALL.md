# Depto de Sistemas y Computación
# Ing. En Sistemas Computacionales
# SISTEMAS PROGRAMABLES 23a

## SENSOR: KY-035 ANALOG HALL
![](https://cdn.shopify.com/s/files/1/1509/1638/products/ky-035-magnetischer-hall-sensor-modul-analog-892360_1024x.jpg?v=1679398870)

## CÓDIGO
```python
import machine
import utime

# Configuración del pin de entrada analógica
analog_pin = machine.ADC(26)

# Función para leer el valor analógico del sensor
def read_analog_value():
    raw_value = analog_pin.read_u16()
    return raw_value

# Bucle principal
while True:
    # Leer el valor analógico del sensor
    sensor_value = read_analog_value()

    # Imprimir el valor del sensor
    print("Valor del sensor: ", sensor_value)

    # Esperar un segundo
    utime.sleep(1)
```

### Autor (es): Cortes Hernandez Yuridia Saray 20210554

## PRUEBAS

![](https://github.com/Danielusuario/Sensores-Raspberry-Pico/blob/main/Imagenes/KY-035.jpg)

## FECHA DE REVISION:
> 99/99/999

## REPOSITORIO:
>https://github.com/Danielusuario/Sensores-Raspberry-Pico

## CONCLUSION:
> Conocer si realmente estaba funcionando fue dificil, ya que no se tenia idea si se estaba realizando de la manera correcta al testearlo. 
