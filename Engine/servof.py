import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
servoPIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
    while True:
    p.ChangeDutyCycle(5.0)
    time.sleep(0.8)
    p.ChangeDutyCycle(8.0)
    time.sleep(0.8)
    p.ChangeDutyCycle(10)
    time.sleep(0.8)
    p.ChangeDutyCycle(11.0)
    time.sleep(0.8)
    p.ChangeDutyCycle(10)
    time.sleep(0.8)
    p.ChangeDutyCycle(8.0)
    time.sleep(0.8)
    p.ChangeDutyCycle(5.0)
    time.sleep(0.8)


except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

