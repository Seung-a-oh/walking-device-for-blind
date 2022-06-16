# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import *
from vibration import *
import threading
import loc
from location import *
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#TRIG = 25 #좌측
#ECHO = 8
TRIG = 22
ECHO = 27

PIR1 = 23
PIR2 = 24
#TRIG2 = 22 #우측
#ECHO2 = 27

GPIO.setup(PIR1, GPIO.IN)
GPIO.setup(PIR2, GPIO.IN)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(1.5)

global detect_count
detect_count = 0

def detect_clean(cho):
    global detect_count
    timer = threading.Timer(cho, detect_clean)
    detect_count = 0
    

def detect_obstacle():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    global detect_count


    while True:
        GPIO.output(TRIG, False)
        time.sleep(0.1)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)


        while GPIO.input(ECHO) == 0:
            start = time.time()
        
        while GPIO.input(ECHO) == 1:
            stop = time.time()

        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm " % distance)
        time.sleep(0.1)

        now = get_loc()
        if now == (6,71,13):
            loc.vib_event.set()
        if loc.vib_event.is_set():
            return
        if detect_count == 0:
            if (distance < 140):                        
                    print("우측에 장애물 있음")

                    vib_by_ob_left_for(0.1)
                    sleep(0.2)
                    vib_by_ob_right_for(0.8)
                    loc.obs_event.set()
                    detect_count = 1

    GPIO.cleanup()


if __name__ == "__main__":
    detect_obstacle()



