import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

GPIO.output(13,True)
GPIO.output(19,True)
GPIO.output(26,False)

time.sleep(3)
GPIO.cleanup()
