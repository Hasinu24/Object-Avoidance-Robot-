from machine import PWM,Pin
from utime import sleep_ms
import time,utime,random
left = machine.ADC(27)
right = machine.ADC(26)
sensor_L = machine.Pin(27, machine.Pin.IN)
sensor_R = machine.Pin(26, machine.Pin.IN)
left_motor= PWM(Pin(1))
right_motor = PWM(Pin(0))

left_motor.freq(50)
right_motor.freq(50)

freq = 50
ms = 1000/freq

state = 2
oldstate = 0
sTime = 0
step_duration = 0.1 
def timer(d):
    global oldstate,sTime,state
    duration = d
    if oldstate!= state:
        sTime = 0
        oldstate = state
        print("test1")
    if sTime < duration:
        sTime+=1
        print(sTime)
        return True
    else:
        sTime = 0
        return False
    

def distancesensor(trigger,echo):
    global on,off
    trigger = Pin(trigger,Pin.OUT)
    echo = Pin(echo,Pin.IN)
    trigger.low()
    time.sleep(.1)
    trigger.high()
    time.sleep(.1)
    trigger.low()
    
    while echo.value()==0:
        off = utime.ticks_us()
        
    while echo.value() ==1:
        on = utime.ticks_us()
        
        
    time_passed = on - off
    distance = (time_passed*0.0343)/2
    
    print("distance",distance)
    return distance

def IRsensor():
    
    leftIR = left.read_u16()
    rightIR = right.read_u16()
    return leftIR,rightIR
    
def dispins():
    leftds = distancesensor(10,11)
    rightds = distancesensor(12,13)
    
    return leftds,rightds

def servoduty(angle):
    return int(((1.5/ms)+ ((angle/90)*(0.5/ms)))*65535)

def power(leftw,rightw):
    rightw = 0-rightw
    
    left_motor.duty_u16(servoduty(leftw))
    right_motor.duty_u16(servoduty(rightw))
    


        
follow_line = 1
search = 2
veer_behavior=3
obstacle_object_offline=4
random_behavior=5
safe_behavior =6
move_levy_flight=7
recovery_behavior=8
        
def follow_line():
    global state
    leftIR,rightIR = IRsensor()
    if timer(1)==True:
        if((rightIR<850 or rightIR>750)  and (leftIR<550 or leftIR>480)):
           power(90,90)
           state= 2
        elif(rightIR >850 and (leftIR<550 or leftIR>480)):
            power(0,90)
            state =2
        elif((rightIR<850 or rightIR>750) and leftIR>550):
            power(90,0)
            state =2
        else:
            state=5
        
    else:
        state=2
        
        
def search():
    
    global state
    power(0,0)
    leftds,rightds = dispins()
    leftIR,rightIR = IRsensor()
    
    if timer(1)==True:
        power(20,20)
        
        if rightIR<2000 or leftIR <2000:
            power(0,0)
            state =6
        if rightIR>32000 or leftIR>32000:
            if leftds>30 and rightds>30 :
                state = 5
            else:
                 power(0,0)
                 state = 3
        #else:
         #   power(0,0)
          #  state = 6
        
          
    
def safe_behavior(i):
    global state
    left_on_weel=[0,-30,30,0]
    right_on_weel=[0,-30,-30,0]
    time = [0.5,0.2,0.5,2]
    if timer(1) == True:
        power(left_on_weel[i],right_on_weel[i])
        utime.sleep(time[i])
        print("test6")
    else:
        state =2
def recovery_behavior():
    
    print("Entering recovery state...")
    power(-20, 20)  
    time.sleep(0.5)
    power(20, -20)  
    time.sleep(0.5)
    state =7
    move_levy_flight(num_steps=10)
    
        
def levy_flight(num_steps=1):
    steps = []
    for _ in range(num_steps):
        step_size = random.randint(-100, 100) / 100.0
        steps.append(step_size)
    return steps

def move_levy_flight(num_steps):
    global state
    steps = levy_flight(num_steps)
    for step in steps:
        power(20, 20)
        time.sleep(step_duration)
        state =2
        power(0, 0)
        time.sleep(step_duration)
        state =2
        power(-20, -20)
        time.sleep(step_duration)
        state =2
        power(0, 0)
        time.sleep(step_duration)
        state =2
    
def obstacle_object_offline(i):
    global state
    left_on_weel=[0,-30,-30,30,0]
    right_on_weel=[0,-30,30,30,0]
    time=[0.3,0.5,0.3,0.3,0.2]
    if timer(1) == True:
        power(left_on_weel[i],right_on_weel[i])
        utime.sleep(time[i])
        print("test4")
    else:
        state =2
        
def veer_behavior(i):
    global state
    left_on_weel=[-15,15,0,20,0,-15,0,20]
    right_on_weel=[-15,-15,0,20,0,15,0,20]
    time=[0.5,0.3,0.5,0.8,0.5,0.6,1,0.8]
    if timer(1) == True:
        power(left_on_weel[i],right_on_weel[i])
        utime.sleep(time[i])
        print("test3")
    else:
        state =2
             
             
    
         
             
            
f_count=0
def random_behavior():
    global state,f_count
    for x in range(1):
        
        direction= random.choice(['forward','reverse','right','left'])
        
        if direction =='forward' and f_count<5:
            power(15,15)
            time.sleep(0.01)
            state = 2
            search()
            f_count+=1
            
            
        
            
#         elif direction ==' right':
#             power(-20,0)
#             time.sleep(0.2)
#             state =2
#             power(20,20)
#             time.sleep(0.5)
#             state = 2
#             
#             
#         elif direction ==' left':
#             power(-20,0)
#             time.sleep(0.2)
#             state = 2
#             power(20,20)
#             time.sleep(0.5)
#             state = 2
#             
            
            
            
            
            

            

veer_counter=0
obstacle_object_offline_counter=0
safe_behavior_counter = 0
while True:
    try:
        
        print("old state",oldstate," current state",state)
        print(IRsensor())
        leftds,rightds = dispins()
        if state==2:
           search()
        elif state ==6 :
            safe_behavior(safe_behavior_counter)
            if safe_behavior_counter>5:
                safe_behavior_counter=0
                state=2
            else:
                safe_behavior_counter+=1
                print("obstacle_object_offline_counter:",obstacle_object_offline_counter)
                #state = 2   
        elif state==3 :
            veer_behavior(veer_counter)
            leftIR,rightIR = IRsensor()
            if veer_counter >= 7:
                veer_counter=0
                state =2
                search()
            else:
                    if rightIR<2000 or leftIR <2000:
                        power(0,0)
                        state =6
                        
                    else:
                        veer_counter+=1
                        print("veer_counter:",veer_counter)
                                               
        elif state==5 :
            random_behavior()
            
        
                                  
        elif state == 4 :
            obstacle_object_offline(obstacle_object_offline_counter)
            if obstacle_object_offline_counter >= 4:
                obstacle_object_offline_counter=0
                state =2
                
            else:
                
                obstacle_object_offline_counter+=1
                print("obstacle_object_offline_counter:",obstacle_object_offline_counter)
                state =2
                 
            
            
        elif state ==1:
            follow_line()
            
        elif state ==7:
            move_levy_flight(num_steps=10)
            
        elif state ==8:
            recovery_behavior()
            
            
        
       
                             
             
       
        sleep_ms(100)
            
            
    except KeyboardInterrupt:
        break
            
            
    
    
    
    
    
    








