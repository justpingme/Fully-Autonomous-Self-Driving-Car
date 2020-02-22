import RPi.GPIO as GPIO
from time import sleep
import EngineDirection as En_Dir
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
servoPIN = 12
GPIO.setup(servoPIN, GPIO.OUT)
t_sleep = 0.002
p = GPIO.PWM(servoPIN, 50)  # GPIO 12 for PWM with 50Hz
p.start(7.5)  # Initialization
"""
    Steering command      

5.0 sharp left
6.0 sharp slight left
7.0 slight left
8.0 straight
9.0 slight right
10.0 sharp slight right
11.0 sharp right

A1 = HIGH (forward) DIR cmd
A1 = LOW (backward) DIR cmd

"""


def gpio_setup():
    global PUL, DIR, ENB
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    PUL = 20
    DIR = 21
    ENB = 16
    GPIO.setup(PUL, GPIO.OUT)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)

    GPIO.output(ENB, GPIO.LOW)


# def steering(cycle):
#     print("steering function")
#     p.ChangeDutyCycle(cycle)
#     sleep(0.8)


def continue_straight():  # forward move
    global t_sleep
    print("continue straight function")
    gpio_setup()
    p.ChangeDutyCycle(8.0)
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(40000):
        for j in range(1):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(t_sleep)
            GPIO.output(PUL, GPIO.LOW)
            sleep(t_sleep)
        if t_sleep > 0.00008:
            t_sleep -= 0.000001


def backward():
    print("backward function called")
    gpio_setup()
    global t_sleep
    GPIO.output(DIR, GPIO.LOW)
    for i in range(4000):
        for j in range(1):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(t_sleep)
            GPIO.output(PUL, GPIO.LOW)
            sleep(t_sleep)
        if t_sleep > 0.00008:
            t_sleep -= 0.000001


def turn_left():
    print("turn left function")
    gpio_setup()
    global t_sleep
    p.ChangeDutyCycle(5.0)
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(3800):
        for j in range(1):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(t_sleep)
            GPIO.output(PUL, GPIO.LOW)
            sleep(t_sleep)
        if t_sleep > 0.00008:
            t_sleep -= 0.000001


def turn_right():
    print("turn right function")
    gpio_setup()
    global t_sleep
    p.ChangeDutyCycle(11.0)
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(3800):
        for j in range(1):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(t_sleep)
            GPIO.output(PUL, GPIO.LOW)
            sleep(t_sleep)
        if t_sleep > 0.00008:
            t_sleep -= 0.000001


def keep_left():
    print("keep left function")
    gpio_setup()
    global t_sleep
    p.ChangeDutyCycle(7.0)
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(1000):
        for j in range(1):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(t_sleep)
            GPIO.output(PUL, GPIO.LOW)
            sleep(t_sleep)
        if t_sleep > 0.00008:
            t_sleep -= 0.000001


def keep_right():
    print("keep right function")
    gpio_setup()
    global t_sleep
    p.ChangeDutyCycle(10.0)
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(1000):
        for j in range(1):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(t_sleep)
            GPIO.output(PUL, GPIO.LOW)
            sleep(t_sleep)
        if t_sleep > 0.00008:
            t_sleep -= 0.000001


def slight_left():
    print("slight left function")
    gpio_setup()
    global t_sleep
    p.ChangeDutyCycle(7.0)
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(3800):
        for j in range(1):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(t_sleep)
            GPIO.output(PUL, GPIO.LOW)
            sleep(t_sleep)
        if t_sleep > 0.00008:
            t_sleep -= 0.000001


def slight_right():
    print("slight right function")
    gpio_setup()
    global t_sleep
    p.ChangeDutyCycle(9.0)
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(3800):
        for j in range(1):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(t_sleep)
            GPIO.output(PUL, GPIO.LOW)
            sleep(t_sleep)
        if t_sleep > 0.00008:
            t_sleep -= 0.000001


def continues_onto():
    print("continue onto same function")
    continue_Straight()


def atRoundabout():
    print("At Round About take et_sleepit function")


def make_u_turn():
    print("make u turn function")


def sharpRight():
    print("sharp right function")
    gpio_setup()
    global t_sleep
    p.ChangeDutyCycle(5.0)
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(4800):
        for j in range(1):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(t_sleep)
            GPIO.output(PUL, GPIO.LOW)
            sleep(t_sleep)
        if t_sleep > 0.00008:
            t_sleep -= 0.000001


def sharpLeft():
    print("sharp left function")
    gpio_setup()
    global t_sleep
    p.ChangeDutyCycle(11.0)
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(4800):
        for j in range(1):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(t_sleep)
            GPIO.output(PUL, GPIO.LOW)
            sleep(t_sleep)
        if t_sleep > 0.00008:
            t_sleep -= 0.000001


GPIO.cleanup()
