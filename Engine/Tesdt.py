import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # set gpio mode to gpio pin using BCM

# acc.. to GPIO PIN 13 19 26 20 21
# pin 40 = pul & 38 = dir for right tb6600
# pin 37 = pul & 35 = dir for left tb6600

L_PUL = 26, 20  # left driver of pull
L_DIR = 19, 21  # left driver of direction
L_ENB = 13, 12  # left  both of enable
STEERING_PIN = 16  # gpio 16 used for steering servo motor

#  set all the gpio pin out
GPIO.setup(L_PUL, GPIO.OUT)
GPIO.setup(L_DIR, GPIO.OUT)
GPIO.setup(R_PUL, GPIO.OUT)
GPIO.setup(R_DIR, GPIO.OUT)
GPIO.setup(L_ENB, GPIO.OUT)
GPIO.setup(R_ENB, GPIO.OUT)
GPIO.setup(STEERING_PIN, GPIO.OUT)



# set the sleep time for one revolution of stepper motor
sleep_time_left = 0.002
sleep_time_right = 0.002

"""
    *** steering cycle value set()
    
    straight = 8.0
    left =  6.0
    right = 11.0
    slight_right = 9.0
    slight left = 7.0
    
    """
# 5.0 left 12.5 right
STEERING_PIN = GPIO.PWM(STEERING_PIN, 50)  # GPIO 17 for PWM with 50Hz
#STEERING_PIN.start(8.0)  # Initialization


def turn_right():
    global sleep_time_left
    GPIO.output(R_ENB, GPIO.LOW)
    GPIO.output(L_ENB, GPIO.LOW)
    GPIO.output(L_DIR, GPIO.HIGH)
    GPIO.output(R_DIR, GPIO.HIGH)
    STEERING_PIN.start(9.0)
    for i in range(3800):
        for j in range(2):
            GPIO.output(L_PUL, GPIO.HIGH)
            GPIO.output(R_PUL, GPIO.HIGH)
            sleep(sleep_time_left)
            GPIO.output(R_PUL, GPIO.LOW)
            GPIO.output(L_PUL, GPIO.LOW)
            sleep(sleep_time_left)
        if sleep_time_left > 0.00008:
            sleep_time_left -= 0.000001

def turn_left():
    global sleep_time_left
    GPIO.output(R_ENB, GPIO.LOW)
    GPIO.output(L_ENB, GPIO.LOW)
    GPIO.output(L_DIR, GPIO.HIGH)
    GPIO.output(R_DIR, GPIO.HIGH)
    STEERING_PIN.start(6.0)
    for i in range(30500):
        for j in range(2):
            GPIO.output(L_PUL, GPIO.HIGH)
            GPIO.output(R_PUL, GPIO.HIGH)
            sleep(sleep_time_left)
            GPIO.output(R_PUL, GPIO.LOW)
            GPIO.output(L_PUL, GPIO.LOW)
            sleep(sleep_time_left)
        if sleep_time_left > 0.00008:
            sleep_time_left -= 0.000001

def steering_straight():
    STEERING_PIN.start(7.5)
    sleep(0.8)

def forward():
    global sleep_time_left
    GPIO.output(R_ENB, GPIO.LOW)
    GPIO.output(L_ENB, GPIO.LOW)
    GPIO.output(L_DIR, GPIO.HIGH)
    GPIO.output(R_DIR, GPIO.HIGH)
    STEERING_PIN.start(7.5)
    sleep(0.8)
    for i in range(9000):
        for j in range(1):
            GPIO.output(L_PUL, GPIO.HIGH)
            GPIO.output(R_PUL, GPIO.HIGH)
            sleep(sleep_time_left)
            GPIO.output(L_PUL, GPIO.LOW)
            GPIO.output(R_PUL, GPIO.LOW)
            sleep(sleep_time_left)
        if sleep_time_left > 0.00008:
            sleep_time_left -= 0.000001


def backward():
    global sleep_time_right
    GPIO.output(R_ENB, GPIO.LOW)
    GPIO.output(L_ENB, GPIO.LOW)
    GPIO.output(L_DIR, GPIO.LOW)
    GPIO.output(R_DIR, GPIO.LOW)
    STEERING_PIN.start(7.5)
    sleep(0.8)
    for i in range(9000):
        for j in range(1):
            GPIO.output(L_PUL, GPIO.HIGH)
            GPIO.output(R_PUL, GPIO.HIGH)
            sleep(sleep_time_right)
            GPIO.output(L_PUL, GPIO.LOW)
            GPIO.output(R_PUL, GPIO.LOW)
            sleep(sleep_time_right)
        if sleep_time_right > 0.00008:
            sleep_time_right -= 0.000001
#STEERING_PIN.start(8.0)

while True:
    forward()
#steering_straight()
#turn_right()
#turn_left()
#backward()
#forward()
#steering_straight()


