from machine import PWM, Pin
import time

left = PWM(Pin(0))
right = PWM(Pin(1))

left.freq(50)
right.freq(50)

leftForward = 6500
rightForward = 6500

leftReverse = 2000000
rightReverse = 2000000

servoStop = 9500


def move_in_square():
    for x in range(4):
        
        left.duty_ns(leftReverse)
        right.duty_ns(rightForward)
        time.sleep(.4)

        
        left.duty_ns(0)
        right.duty_ns(0)
        time.sleep(1)

       
        left.duty_ns(leftForward)
        right.duty_ns(rightForward)
        time.sleep(.3)

       
        left.duty_ns(0)
        right.duty_ns(0)
        time.sleep(1)


move_in_square()


left.duty_ns(0)
right.duty_ns(0)

