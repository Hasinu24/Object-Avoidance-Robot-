from machine import PWM, Pin
import time
import random

left = PWM(Pin(1))
right = PWM(Pin(0))

left.freq(50)
right.freq(50)

leftForward = 6500
rightForward = 6500

leftReverse = 2000000
rightReverse = 2000000

servoStop = 9500

def random_walk():
      
        
        direction = random.choice(['forward','reverse','right','left'])

        if direction == 'forward':
            left.duty_ns(0)
            right.duty_ns(rightReverse)
            
            time.sleep(.1)

            left.duty_ns(leftForward)
            right.duty_ns(0)
            
            time.sleep(.1)
            
        else:  # direction == 'reverse'
            left.duty_ns(leftReverse)
            right.duty_ns(0)
            time.sleep(.1)
            left.duty_ns(0)
            right.duty_ns(rightForward)
            time.sleep(.1)
        
        

    
        left.duty_ns(0)
        right.duty_ns(0)
        time.sleep(1)  


while True:
    random_walk()
