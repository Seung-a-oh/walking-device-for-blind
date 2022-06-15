# -*- coding: utf-8 -*-

from threading import Thread
import RPi.GPIO as GPIO
import time
import os

# from ttts import *
from button import *

PIR1 = 23
PIR2 = 24
GPIO.setup(PIR1, GPIO.IN)
GPIO.setup(PIR2, GPIO.IN)

def detecting_people():
    while True:
        if GPIO.input(PIR1) or GPIO.input(PIR2):
            print(GPIO.input(PIR1),GPIO.input(PIR2))
            
            os.system('omxplayer ./mp3/find_user/start_first.mp3')
            os.system('omxplayer ./mp3/find_user/explan_first1.mp3')
            time.sleep(3)
            os.system('omxplayer ./mp3/find_user/explan_first2.mp3')
            # txt_reader("ment1")         # 장치가 여기있음을 홍보
            print('---PIR 감지 후 버튼 입력 대기 중---')
            if detect_start() == 1:
               os.system('omxplayer ./mp3/find_user/dest_button_explan.mp3')
                # txt_reader("ment2")     # 사용 방법 안내
               return 1
        else:
            print("---주변에 사용자 없음---")
            time.sleep(0.1)


# pir로 사람 감지 후, 2번 방송. 
# if 방송 중에 시작 누르면 방송 종료 후 시작
