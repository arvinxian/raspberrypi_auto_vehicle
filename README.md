# raspberrypi_auto_vehicle

用树莓派控制直流电机(L298N)
https://www.jianshu.com/p/b970403a647f

# development note
树莓派中GPIO引脚编码的解释
https://www.cnblogs.com/wangha/p/10475719.html
BCM,wiringPi,BOARD使用场合：

BOARD编码和BCM一般都在python库中使用
import RPi.GPIO as GPIO  //引入RPi.GPIO库
GPIO.setmode(GPIO.BCM) //设置引脚编号为BCM编码方式；
GPIO.setmode(GPIO.BOARD) //设置GPIO引脚为BOARD编码方式。
而wiringPi一般用于C++等平台
LIBS += -lwiringPi
#include "wiringPi.h"
wiringPiSetup();



July 25, 2020 

多路pmw信号（多线程）
askpure.com/course_R0LMJUH2-GB2F9NJH-OLCVUSHP-4ZWW9CTB.html

July 27, 2020 

树莓派（九）：多线程基础+控制多台电机
https://blog.csdn.net/weixin_44524040/article/details/90450315



22/03/2021 00:18
Successfully control on tyre1 through raspberry pi

22/03/2021 22:09
Successfully control on tyre2 through raspberry pi