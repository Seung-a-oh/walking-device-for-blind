# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import *
from vibration import *
import threading
import loc
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
print("초음파 거리 측정기")

GPIO.setup(PIR1, GPIO.IN)
GPIO.setup(PIR2, GPIO.IN)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("초음파 출력 초기화")
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
    detect_clean(10)

    while True:
        GPIO.output(TRIG, False)
        time.sleep(0.5)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # GPIO.output(TRIG, True)
        # time.sleep(0.00001)
        # GPIO.output(TRIG, False)
        # time.sleep(0.00001)

        while GPIO.input(ECHO) == 0:
            start = time.time()
        
        while GPIO.input(ECHO) == 1:
            stop = time.time()

        check_time = stop - start
        distance = check_time * 34300 / 2
#        print("Distance : %.1f cm " % distance)
#        print(detect_count)
        time.sleep(0.2)

        if loc.vib_event.is_set():
            return

        now = loc.now_loc
        if now != (4,65,19):
            if GPIO.input(PIR1) and distance > 50 and distance < 110 :
                print('사람 감지')
                os.system('omxplayer ./mp3/pir.mp3')
            elif (distance < 120):
                detect_count = detect_count+1
                if detect_count > 0:
                    
                    print("우측에 장애물 있음")

                    vib_by_ob_left_for(0.1)

                    sleep(0.2)
                    vib_by_ob_right_for(0.8)

                    detect_count = 0
                    # loc.vib_event.set()
        # else:
        #         print("장애물 없음")
    #except KeyboardInterrupt:
    #    print("거리 측정 완료")
    GPIO.cleanup()


if __name__ == "__main__":
    detect_obstacle()




