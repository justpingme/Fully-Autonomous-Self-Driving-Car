import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
P_A1 = 20
P_A2 = 21
P_A3 = 16
servoPIN = 12
GPIO.setup(P_A1, GPIO.OUT)
GPIO.setup(P_A2, GPIO.OUT)
GPIO.setup(P_A3, GPIO.OUT)
GPIO.output(P_A2, GPIO.LOW)
GPIO.setup(servoPIN, GPIO.OUT)
x=0.002
y=0.002
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(7.5) # Initialization
def forward():
    global x
    GPIO.output(P_A1,GPIO.HIGH)
    for i in range(40000):
        for j in range(1):
            GPIO.output(P_A2,GPIO.HIGH)
            sleep(x)
            GPIO.output(P_A2,GPIO.LOW)
            sleep(x)
        if x > 0.00008:
            x-=0.000001
def backward():
    global y
    GPIO.output(P_A1,GPIO.LOW)
    for i in range(4000):
        for j in range(1):
            GPIO.output(P_A2,GPIO.HIGH)
            sleep(y)
            GPIO.output(P_A2,GPIO.LOW)
            sleep(y)
        if y > 0.00008:
            y-=0.000001
while True:
    forward()
    sleep(1)
    x=0.0008
    backward()
    sleep(1)
    y=0.0008
GPIO.cleanup()

