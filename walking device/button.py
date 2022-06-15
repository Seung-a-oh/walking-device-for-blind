# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os
import loc
# from ttts import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Start_Pin = 7

floor = 21     # music   -> 2
room = 16     # music   -> 2

GPIO.setup(Start_Pin, GPIO.IN)
GPIO.setup(floor, GPIO.IN)
GPIO.setup(room, GPIO.IN)


# if f_cnt != 0 and r_cnt != 0:
    
# desination_coor = {
#     'ML604': (6,65,13), 
#     'startup': (6,71,13), 
#     'parking_lot6': (6,65,19), 
#     'toilet': (4,48,12),
#     'parking_lot4': (4,65,19),
#     'ground': (4,45,2),
#     'ML416': (4,56,12),
#     'ML417': (4,38,12),
#     'working': (4,72,12)
# }


desination_coor = {
    'ML604': {'location':(6,65,13),'bearing':'n'},
    'startup': {'location':(6,71,13),'bearing':'e'}, 
    'parking_lot6': {'location':(6,65,19),'bearing':'n'}, 
    'toilet': {'location':(4,48,12),'bearing':'n'},
    'parking_lot4': {'location':(6,65,19),'bearing':'n'},
    'ground': {'location':(4,45,2),'bearing':'e'},
    'ML416': {'location':(4,56,12),'bearing':'s'},
    'ML417': {'location':(4,38,12),'bearing':'s'},
    'working': {'location':(4,72,12),'bearing':'n'}
}

def set_dest():
    f_cnt = 4
    r4_cnt = 0
    r6_cnt = 0

    room_4 = ['toilet','parking_lot4','ground','ML416','ML417','working']
    room_6 = ['parking_lot6','ML604','startup']

    while True:
        if GPIO.input(floor) == 0:
            if f_cnt == 4:
                os.system('omxplayer ./mp3/button/floor_4.mp3')
                f_cnt = 7
            elif f_cnt == 7:
                os.system('omxplayer ./mp3/button/floor_7.mp3')
                f_cnt = 4
        if GPIO.input(room) == 0:
            if f_cnt == 7:
                os.system('omxplayer ./mp3/button/'+room_4[r4_cnt]+'.mp3')
                r4_cnt += 1
                if r4_cnt == 6:
                    r4_cnt = 0
            elif f_cnt == 4:
                os.system('omxplayer ./mp3/button/'+room_6[r6_cnt]+'.mp3')
                r6_cnt += 1
                if r6_cnt == 3:
                    r6_cnt = 0

        if GPIO.input(Start_Pin) == 0:
            break
    
    if f_cnt == 4:
        if r6_cnt >= 1:
            # print(room_6[r6_cnt-1])
            loc.dest_bearing = desination_coor[room_6[r6_cnt-1]['bearing']]
            return desination_coor[room_6[r6_cnt-1]['location']]
        else:
            loc.dest_bearing = desination_coor['startup']['bearing']
            return desination_coor['startup']['location']
    elif f_cnt == 7:
        if r4_cnt >= 1:
            # print(room_4[r4_cnt-1])
            loc.dest_bearing = desination_coor[room_4[r4_cnt-1]['bearing']]
            return desination_coor[room_4[r4_cnt-1]['location']]
        else:
            loc.dest_bearing = desination_coor['working']['bearing']
            return desination_coor['working']['location']


def detect_start():
    start_time = time.time()

    while True:
        if time.time() - start_time > 60:   # 1분 이상 버튼을 안누르면
            return 0
        if GPIO.input(Start_Pin) == 0:
            print("시작 버튼 눌림")
            os.system('omxplayer ./mp3/button/start_on.mp3')
            return 1
        else:
            print("--시작 버튼 감지 파트--")
            time.sleep(0.2)

if __name__ == "__main__":
    print(set_dest())
    # print(desination_coor['toilet'])
