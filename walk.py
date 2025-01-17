from machine import PWM, Pin
import time

left = PWM(Pin(1))
right = PWM(Pin(0))

left.freq(50)
right.freq(50)

leftForward = 6500
rightForward = 6500

leftReverse = 2000000
rightReverse = 2000000

servoStop = 9500


def move_in_square():
    for x in range(1):
        
        left.duty_ns(0)
        right.duty_ns(rightForward)
        time.sleep(.1)

        
        left.duty_ns(0)
        right.duty_ns(0)
        time.sleep(1)

       
        left.duty_ns(leftReverse)
        right.duty_ns(0)
        time.sleep(.1)

       
        left.duty_ns(0)
        right.duty_ns(0)
        time.sleep(1)


while True:
    move_in_square()

