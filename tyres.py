# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO         # 引入GPIO模块
import time                     # 引入time模块
import threading
from pynput import keyboard

ENA1 = 13                        # 设置GPIO13连接ENA
ENA2 = 16
ENA3 = 17
ENA4 = 18


IN1 = 19                        # 设置GPIO19连接IN1
IN2 = 26                        # 设置GPIO26连接IN2
IN3 = 20
IN4 = 21
IN5 = 27
IN6 = 22
IN7 = 23
IN8 = 24

run_time = 0.1

class Motor:
    def __init__(self, ENA, I1, I2):
        # initiate
        self.ENA = ENA
        self.I1 = I1
        self.I2 = I2


    def setPin(self, enableENA, enableI1, enableI2):
        # initiate GPIO PIN
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.I1, GPIO.OUT)
        GPIO.setup(self.I2, GPIO.OUT)

        GPIO.output(self.ENA, enableENA)
        GPIO.output(self.I1, enableI1)
        GPIO.output(self.I2, enableI2)

    def rest_pin(self):
        # reset GPIO pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ENA, GPIO.IN)
        GPIO.setup(self.I1, GPIO.IN)
        GPIO.setup(self.I2, GPIO.IN)

    def forward(self, run_time):
        Motor.setPin(self, True, True, False)
        time.sleep(run_time)
        self.stop_motor()
        self.rest_pin()
        
    def backward(self, run_time):
        Motor.setPin(self, True, False, True)
        time.sleep(run_time)
        self.stop_motor()
        self.rest_pin()

    def stop_motor(self):
        Motor.setPin(self, False, False, False)

def destory():
    GPIO.cleanup()

def tyre1_move_forward(run_time):
    try:
        # initiation
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ENA1, GPIO.OUT)
        GPIO.setup(IN1, GPIO.OUT)
        GPIO.setup(IN2, GPIO.OUT)

        GPIO.output(IN1, True)
        GPIO.output(IN2, False)
        GPIO.output(ENA1, True)
        time.sleep(run_time)

    finally:
        #GPIO.setmode(GPIO.BCM)
        GPIO.setup(ENA1, GPIO.OUT)
        GPIO.output(ENA1, False)

        GPIO.output(ENA2, False)

def move_left(run_time):
        # go left
        thread1 = threading.Thread(target=tyre1.forward, args=(run_time,))
        thread2 = threading.Thread(target=tyre2.forward, args=(run_time,))
        thread3 = threading.Thread(target=tyre3.forward, args=(run_time,))
        thread4 = threading.Thread(target=tyre4.forward, args=(run_time,))
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()

def move_forward(run_time):
        # go forward
        thread1 = threading.Thread(target=tyre1.forward, args=(run_time,))
        thread2 = threading.Thread(target=tyre2.forward, args=(run_time,))
        thread3 = threading.Thread(target=tyre3.backward, args=(run_time,))
        thread4 = threading.Thread(target=tyre4.backward, args=(run_time,))
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()

def move_right(runtime):
        # go right
        thread5 = threading.Thread(target=tyre1.backward, args=(run_time,))
        thread6 = threading.Thread(target=tyre2.backward, args=(run_time,))
        thread7 = threading.Thread(target=tyre3.backward, args=(run_time,))
        thread8 = threading.Thread(target=tyre4.backward, args=(run_time,))
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()
        thread5.join()
        thread6.join()
        thread7.join()
        thread8.join()

def move_backward(runtime):
        # go backward
        thread5 = threading.Thread(target=tyre1.backward, args=(run_time,))
        thread6 = threading.Thread(target=tyre2.backward, args=(run_time,))
        thread7 = threading.Thread(target=tyre3.forward, args=(run_time,))
        thread8 = threading.Thread(target=tyre4.forward, args=(run_time,))
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()
        thread5.join()
        thread6.join()
        thread7.join()
        thread8.join()
def turn_left(runtime):
        # turn left
        thread1 = threading.Thread(target=tyre1.forward, args=(run_time,))
        thread3 = threading.Thread(target=tyre3.backward, args=(run_time,))
        thread4 = threading.Thread(target=tyre4.forward, args=(run_time,))
        thread1.start()
        thread3.start()
        thread4.start()
        thread1.join()
        thread3.join()
        thread4.join()

def turn_right(runtime):
        # turn right
        thread2 = threading.Thread(target=tyre2.forward, args=(run_time,))
        thread3 = threading.Thread(target=tyre3.forward, args=(run_time,))
        thread4 = threading.Thread(target=tyre4.backward, args=(run_time,))
        thread2.start()
        thread3.start()
        thread4.start()
        thread2.join()
        thread3.join()
        thread4.join()

def move_forward_1(run_time):
        # go forward
        thread1 = threading.Thread(target=tyre1.forward, args=(run_time,))
        thread1.start()
        thread1.join()

def move_forward_2(run_time):
        # go forward
        thread2 = threading.Thread(target=tyre2.forward, args=(run_time,))
        thread2.start()
        thread2.join()

def move_forward_3(run_time):
        # go forward
        thread3 = threading.Thread(target=tyre3.forward, args=(run_time,))
        thread3.start()
        thread3.join()

def move_forward_4(run_time):
        # go forward
        thread4 = threading.Thread(target=tyre4.forward, args=(run_time,))
        thread4.start()
        thread4.join()

def move_backward_1(run_time):
        # go forward
        thread1 = threading.Thread(target=tyre1.backward, args=(run_time,))
        thread1.start()
        thread1.join()

def print_key(key_value):
    print('key_value')


def get_move(key):
    global run_time
    try:
        if key.char == 'k':
            move_forward(run_time)
        if key.char == 'j':
            move_backward(run_time)
        if key.char == 'h':
            move_left(run_time)
            #move_forward_1(run_time)
        if key.char == 'l':
            #move_backward_1(run_time)
            move_right(run_time)
        if key.char == 'a':
            turn_left(run_time)
        if key.char == 'f':
            turn_right(run_time)
        if key.char == '1':
            move_forward_1(run_time)
        if key.char == '2':
            move_forward_2(run_time)
        if key.char == '3':
            move_forward_3(run_time)
        if key.char == '4':
            move_forward_4(run_time)
    except:
        destory()

def on_release(key):
    print("key released\n")
    if key == keyboard.Key.esc:
        destory()
        return False


if __name__ == '__main__':
    
    tyre1 = Motor(ENA1, IN1, IN2) #instantiate class
    tyre2 = Motor(ENA2, IN4, IN3)
    tyre3 = Motor(ENA3, IN6, IN5)
    tyre4 = Motor(ENA4, IN7, IN8)

    '''
    while True:
        direction = input("please input direction:")
        get_move(direction, run_time)
    '''
    while True:
        with keyboard.Listener(
                on_press=get_move, on_release=on_release) as listener:
            listener.join()
    print("all done")

