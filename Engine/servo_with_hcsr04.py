import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

TRIG1 = 13 #forward
TRIG2 = 15 #back
ECHO1 = 16 #for
ECHO2 = 11  # back
servoPIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

def distance_cal1():
    print ("Distance Measurement In Progress front")
    
    GPIO.setup(TRIG1,GPIO.OUT)
    
    GPIO.setup(ECHO1,GPIO.IN)
    
    GPIO.output(TRIG1, False)
    
    print ("Waiting For Sensor To Settle device in for front sensor")
    
    time.sleep(0.09)
    
    GPIO.output(TRIG1, True)
    
    time.sleep(0.00001)
    
    GPIO.output(TRIG1, False)
    
    
    while GPIO.input(ECHO1)==0:
        pulse_start1 = time.time()
    while GPIO.input(ECHO1)==1:
        pulse_end1 = time.time()
    pulse_duration1 = pulse_end1 - pulse_start1
    distance1 = pulse_duration1 * 17150
    distance1 = round(distance1, 2)
    print ("Distance1:",distance1,"cm")
    print()


def distance_cal2():
    global pulse_end2
    print ("Distance Measurement In Progress rear")
    
    GPIO.setup(TRIG2,GPIO.OUT)
    
    GPIO.setup(ECHO2,GPIO.IN)
    
    GPIO.output(TRIG2, False)
    
    print ("Waiting For Sensor To Settle device in for rear sensor")
    
    time.sleep(0.09)
    
    GPIO.output(TRIG2, True)
    
    time.sleep(0.00001)
    
    GPIO.output(TRIG2, False)
    
    
    while GPIO.input(ECHO2)==0:
        pulse_start2 = time.time()
    while GPIO.input(ECHO2)==1:
        pulse_end2 = time.time()
    pulse_duration2 = pulse_end2 - pulse_start2
    distance2 = pulse_duration2 * 17150
    distance2 = round(distance2, 2)
    print ("Distance1:",distance2,"cm")
    print()


try:
    while(True):
        p.ChangeDutyCycle(5)
        distance_cal1()
        distance_cal2()
        time.sleep(0.02)
        p.ChangeDutyCycle(7.5)
        distance_cal1()
        distance_cal2()
        time.sleep(0.02)
        p.ChangeDutyCycle(10)
        distance_cal1()
        distance_cal2()
        time.sleep(0.02)
        p.ChangeDutyCycle(12.5)
        distance_cal1()
        distance_cal2()
        time.sleep(0.02)
        p.ChangeDutyCycle(10)
        distance_cal1()
        distance_cal2()
        time.sleep(0.02)
        p.ChangeDutyCycle(7.5)
        distance_cal1()
        distance_cal2()
        time.sleep(0.02)
        p.ChangeDutyCycle(5)
        distance_cal1()
        distance_cal2()
        time.sleep(0.02)
        p.ChangeDutyCycle(2.5)
        distance_cal1()
        distance_cal2()
        time.sleep(0.02)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

