import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.output(17,True)
GPIO.output(22,True)
GPIO.output(27,False)

time.sleep(3)
GPIO.cleanup()
