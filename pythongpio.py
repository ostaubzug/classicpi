#gpio board
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)

while True:
    if GPIO.input(13) == 1:
        print("13")
        time.sleep(0.5)
    if GPIO.input(19) == 1:
        print("19")
        time.sleep(0.5)
    if GPIO.input(26) == 1:
        print("26")
        time.sleep(0.5)
#test 13 19 26