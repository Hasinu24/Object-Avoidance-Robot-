from machine import PWM, Pin
import time

servoForwardLeft=10000
servoForwardRight = 10000
servoStop = 95000
servoReverseLeft = 2000000
servoReverseRight =2000000
left = PWM(Pin(0))
right = PWM(Pin(1))
right.freq(50)
left.freq(50)
left.duty_ns(servoForwardLeft)
right.duty_ns(servoForwardRight)
time.sleep(1)
left.duty_ns(servoReverseLeft)
right.duty_ns(servoReverseRight)
time.sleep(2)
left.duty_ns(servoStop)
right.duty_ns(servoStop)
left.duty_ns(0)
right.duty_ns(0)