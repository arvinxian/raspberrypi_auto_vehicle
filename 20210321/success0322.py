import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

pwm = GPIO.PWM(2,0.2)

pwm.start(90)
GPIO.output(3,True)
GPIO.output(4,False)

try:
    while True:
        pwm.ChangeDutyCycle(90)
        time.sleep(5)
        pwm.ChangeDutyCycle(30)
        time.sleep(5)
except keyboardInterrupt:
    print("STOP")

except:
    print("other errors")

finally:
    GPIO.cleanup()
