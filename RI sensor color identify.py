from machine import Pin
from utime import sleep_ms

left = machine.ADC(27)
right = machine.ADC(26)


def color_range(sensor):
    value = sensor.read_u16()
    if value < 500:
        return value
    elif value < 700:
        return value
    else:
        return value

while True:
    try:
        left_color = color_range(left)
        right_color = color_range(right)
        
        print("Left sensor:", left_color,"Right sensor:", right_color)
        
        
        sleep_ms(1000)
        
    except keyboardInterrupt:
         break
        
        
        
        
            
