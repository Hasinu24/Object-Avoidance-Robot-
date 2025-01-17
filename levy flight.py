from machine import PWM, Pin, ADC
import time
import utime
import random

left = ADC(Pin(27))
right = ADC(Pin(26))
sensor_L = Pin(27, Pin.IN)
sensor_R = Pin(26, Pin.IN)
left_motor = PWM(Pin(1))
right_motor = PWM(Pin(0))

left_motor.freq(50)
right_motor.freq(50)

freq = 50
ms = 1000 / freq

state = 2
oldstate = 0
sTime = 0
step_duration = 0.1 

def timer(d):
    global oldstate, sTime, state
    duration = d
    if oldstate != state:
        sTime = 0
        oldstate = state
        print("test1")
    if sTime < duration:
        sTime += 1
        print(sTime)
        return True
    else:
        sTime = 0
        return False

def distancesensor(trigger, echo):
    global on, off
    trigger = Pin(trigger, Pin.OUT)
    echo = Pin(echo, Pin.IN)
    trigger.low()
    time.sleep(0.1)
    trigger.high()
    time.sleep(0.1)
    trigger.low()

    while echo.value() == 0:
        off = utime.ticks_us()

    while echo.value() == 1:
        on = utime.ticks_us()

    time_passed = on - off
    distance = (time_passed * 0.0343) / 2

    print("distance", distance)
    return distance

def IRsensor():
    leftIR = left.read_u16()
    rightIR = right.read_u16()
    return leftIR, rightIR

def dispins():
    leftds = distancesensor(10, 11)
    rightds = distancesensor(12, 13)
    return leftds, rightds

def servoduty(angle):
    return int(((1.5 / ms) + ((angle / 90) * (0.5 / ms))) * 65535)

def power(leftw, rightw):
    rightw = 0 - rightw
    left_motor.duty_u16(servoduty(leftw))
    right_motor.duty_u16(servoduty(rightw))

def levy_flight(num_steps=1):
    steps = []
    for _ in range(num_steps):
        step_size = random.randint(-100, 100) / 100.0
        steps.append(step_size)
    return steps

def move_levy_flight(num_steps):
    steps = levy_flight(num_steps)
    for step in steps:
        power(20, 20)
        time.sleep(step_duration)
        power(0, 0)
        time.sleep(step_duration)
        power(-20, -20)
        time.sleep(step_duration)
        power(0, 0)
        time.sleep(step_duration)

while True:
    move_levy_flight(num_steps=10)
