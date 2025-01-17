from machine import Pin, PWM, ADC
from utime import sleep_ms
import time
import utime


oldState =0
state =0
sTime =0
def timer(d)
global oldState # We declare as global so we can modify
global sTime # Time like a stopwatch, 1,2,3,4 etc
duration = d # How long we want our state to last


if oldState != state: # if our current state is diffrent to the last state we reset the timer to 0 and update the old state

sTime = 0
oldState = state
if sTime < duration: # if the timer is less than the duration i.e., if sTime
=6 and our duration in 10, return true to say the timer has not been reached
sTime+=1 # adds one to our time
return True
else: # else if sTime is = or > then duration we return false
return False
def stateZero(DSleft,DSright)
if DSleft < 100 or DSright < 100:
return 1 #In python, once a return happens the functions exits.
if timer(10) == True: #Note this is an if Not an elif, however given the
above, this cannot run if the previous is true so an elseif could also work here
move(90,90)
return 0
else #This currently does nothing. However we could use this to
change states once the tiemr runs out.
return 0 # Once this state ends, due to not transitioning to
another state and not resseting our controller the robot will stop and be stuck in
an endless loop. This will be fixed as you add more states.
def stateOne()
if timer(5) == True:
move(90,-90)
return 1
else:
return 0
while True:
DSleft,DSright = ReadDS()
IRleft,IRright = readIR()
if state == 0:
state = stateZero(DSleft,DSright)
elif state ==1:
state = stateOne()
sleep(1) #Sleep the controller for one second. Note outside of sleeps in the
DS/IR sesnors, you should avoid sleeps in your functions? Why do you think this is
the case?

