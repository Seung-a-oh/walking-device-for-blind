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
    #try:
    # detect_clean(10)

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
#        print(detect_count)
        time.sleep(0.1)

        now = get_locs()
        print("ultra now loc: " + str(now))
        if now == (6,71,13):
            loc.vib_event.set()
        if loc.vib_event.is_set():
            return
        if now != (4,65,19) or now != (6,65,19) or now != (4,72,12):
            # if GPIO.input(PIR2) and distance > 150 and distance < 200 :
            # #if GPIO.input(PIR2):
            #     print('사람 감지')
            #     os.system('omxplayer ./mp3/pir.mp3')
            if (distance < 140):
                # detect_count = detect_count+1
                # if detect_count > 0: 
                    
                    print("우측에 장애물 있음")

                    vib_by_ob_left_for(0.1)
                    sleep(0.2)
                    vib_by_ob_right_for(0.8)
                    # detect_count = 0
                    # loc.vib_event.set()
        # else:
        #         print("장애물 없음")
    #except KeyboardInterrupt:
    #    print("거리 측정 완료")
    GPIO.cleanup()


if __name__ == "__main__":
    detect_obstacle()



