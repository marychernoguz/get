import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

while True:
    a = GPIO.input(24)
    print(a)
    GPIO.output(21, not(a)b h)