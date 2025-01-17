from machine import Pin

from utime import sleep_ms


sensor_L = machine.Pin(27, machine.Pin.IN)
sensor_R = machine.Pin(26, machine.Pin.IN)


while True:
    try:
        # Read color values
        sensor_value_L = sensor_L.value()
        sensor_value_R = sensor_R.value()

        # Check color value for sensor L
        if sensor_value_L == 0:
            print("Sensor L: Black detected")
        else:
            print("Sensor L: White detected")
        
        # Check color value for sensor R
        if sensor_value_R == 0:
            print("Sensor R: Black detected")
        else:
            print("Sensor R: White detected")
            
        # Additional functionality
        # For example, let's add a delay of 500 milliseconds after detecting the color for sensor R
        sleep_ms(500)

        

    except KeyboardInterrupt:
        print("Program stopped by user.")
        break


