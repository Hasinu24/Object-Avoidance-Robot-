from machine import Pin
import time
import utime
trigger = Pin(10,Pin.OUT)
echo = Pin(11,Pin.IN)
trigger1 = Pin(13,Pin.OUT)
echo1 = Pin(12,Pin.IN)
def distancesensor():
    trigger.low()
    time.sleep(.2)
    trigger.high()
    time.sleep(.2)
    trigger.low()

    while echo.value()==0:
        off = utime.ticks_us()
       
    while echo.value()==1:
        on = utime.ticks_us()
             
    time_passed = on - off
             
    distance = (time_passed * 0.0343)/2
             
    print("the distance is :",distance," cm")
         
def distancesensor1():
    trigger1.low()
    time.sleep(.2)
    trigger1.high()
    time.sleep(0.2)
    trigger1.low()

    while echo1.value()==0:
        off = utime.ticks_us()
       
    while echo1.value()==1:
        on = utime.ticks_us()
             
    time_passed = on - off
             
    distance2 = (time_passed * 0.0343)/2
             
    print("the distance2 is :",distance2," cm")
                  
while True:
    distancesensor()
    
    print('read')
    time.sleep(.1)
