from machine import Pin
import time

gp_led = 14  # Define GP de LED
gp_sensor = 15 # Define GP de sensor

led = Pin(gp_led, Pin.OUT) # El LED se lo define como salida
sensor = Pin(gp_sensor, Pin.IN) # El sensor se lo define como de entrada

estado = 0
val = 0

while True:
    val = sensor.value()  # lee valor del sensor

    if val == 1:  
        led.on()  

        if estado == 0:
            print("Movimiento Detectado!")
            estado = 1  # actualiza variable a Alto
    else:
        led.off()  

        if estado == 1:
            print("Movimiento Detenido!")
            estado = 0  # actualiza la variable a Bajo

    time.sleep(0.2)
    
