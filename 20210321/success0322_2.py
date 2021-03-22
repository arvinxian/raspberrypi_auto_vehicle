import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

GPIO.output(16,True)
GPIO.output(21,True)
GPIO.output(20,False)

time.sleep(3)
GPIO.cleanup()
