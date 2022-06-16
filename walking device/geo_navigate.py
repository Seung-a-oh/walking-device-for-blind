# -*- coding: utf-8 -*-

from location import *
from find_route_coor import *
from read_magn_data import *
from vibration import *
from graph import adjac_lis as adj
import math
import os
import time
import threading

me = -1             # 내가 보고 있는 방향 각도
want = -1           # 가야하는 방향 각도
change = -1         # 현재 보고 있는 x, y 축 진행 방향 정보 / x=0, y=1
pre_want = -1

route_len = -1
now_index = -1

pre_loc = (-1, -1)
now_loc = (-1, -1)
next_loc = (-1, -1)
evei = 0
graph = Graph(adjac_lis)

def navigate(DEST):
    global now_index
    global pre_loc
    global want
    global me
    global evei
    global pre_want
    global before_coner

    # 전체 초기화 과정
    now_loc = get_loc()
    route = graph.a_star_algorithm(now_loc, DEST)
    route_len = len(route)
    before_corner = 0	
    if route_len > 1:
        want = xy_direction(route[0],route[1])        # 첫 진행 방향 초기화
    # me = get_angle()

    while now_loc != DEST:

        if now_index >= 0:
            pre_loc = now_loc
        now_loc = get_loc()
        #만약 현재 위치가 (시나리오 상의)코너 전 비콘이면 
        if  now_loc == (4, 81, 12):#or now_loc == (6, 65, 19) os.system('omxplayer -o ./mp3/before_corner_left &') print('잠시후 좌회전입니다')
            if before_corner == 10:#4번 감지되면
                os.system('omxplayer ./mp3/vibration/before_corner_right_short.mp3')
                print('잠시후 우회전입니다.')
               # before_corner =0
            before_corner +=1
        if now_loc == (6, 65, 19):
            if before_corner == 4:
                os.system('omxplayer ./mp3/vibration/before_corner_left_short.mp3')
                print('잠시후 좌회전입니다.')
            #os.system('omxplayer ./mp3/vibration/before_corner_left_sp.mp3')
            before_corner += 1 #출력 완료
        # 값이 튄 경우 / 현재 감지한 x,y와 이전 위치의 x,y 값이 3 이상 차이 나면
        if pre_loc != (-1,-1):
            # 나와 내 주변의 이웃한 노드들을 저장해놓고, 값이 그 안에 있지 않으면 튄 값으로 판별
            pre_loc_list = adj[pre_loc]
            if now_loc not in pre_loc_list:
                print("보정 전 현재 위치: "+str(now_loc)+"보정 전 이전 위치: "+str(pre_loc))
                now_loc = route[route.index(pre_loc)+1]
                print("보정 후 현재 위치: "+str(now_loc))
            elif abs(now_loc[0]-pre_loc[0]) >= 10 or abs(now_loc[1]-pre_loc[1]) >= 10:
                now_loc = route[route.index(pre_loc)+1]                                 # 루트 상의 이전(직전에 방문한) 노드의 다음 노드를 넣어줌
                print("out of range!!!")
        
        if now_loc not in route:        # 경로에서 이탈했으면
            now_index = 0
            navigate(DEST)

        # 인덱스 range 초과 방지 하기 위해서
        now_index = route.index(now_loc)

        # 둘의 값이 같다는 것은, 루트의 마지막 즉, 도착지
        # 도착지 처리 해야함.
        if now_index + 1 == route_len:
            next_loc = (-1,-1)
        else:
            next_loc = route[now_index+1]
        # 각도로 진동 발생 부분

        if evei == 0 and now_loc[0] != next_loc[0] and now_loc[1:] == next_loc[1:]:
           print(evei, now_loc, next_loc)
           os.system('omxplayer ./mp3/elev_explan.mp3')
           print('엘리베이터에 도착하였습니다.')
           evei = 1
            
        me = get_angle()
        pre_want = want
        if next_loc != (-1,-1):
            want = xy_direction(now_loc, next_loc) #수정
            # if now_loc == (4,65,19) and next_loc == (6, 65, 19): #4층 엘베 -> 6층 엘베 
            #     pre_want = 260
                 
            if pre_want != want:                          # 코너면,
                before_corner = 0
                print(want)
                if (want-10) >= me or me >= (want+10):    # 내가 보고 있는 방향이 진행 방향이 아니라면,
                    turn_direction = turn(want, me)
                    if turn_direction == 'right':
                        print('right vibration')
                        vib_right()     # 진동을 발생
                        while (want-10) >= me or me >= (want+10):  # 목표 방향 +-10 이내가 될 때 까지
                            me = get_angle()
                            if want > 350 and me <= 10:
                                me += 360
                            print('내가 보고 있는 방향: '+str(me)+' / 가야할 방향: '+str(want))
                            time.sleep(0.2)
                    elif turn_direction == 'left':
                        print('left vibration')
                        vib_left()      # 진동을 발생
                        while (want-10) >= me or me >= (want+10):  # 목표 방향 +-10 이내가 될 때 까지
                            me = get_angle()
                            print('내가 보고 있는 방향: '+str(me)+' / want: '+str(want))
                            time.sleep(0.2)
                vib_stop()
                if now_loc == (4,72,12): # or pre_loc == (4,72,12):
                    os.system('omxplayer ./mp3/vibration/before_elev.mp3')
                    print('잠시후 엘리베이터가 있습니다.')

            if loc.obs_event.is_set():
                print('초음파 방향 맞추기')
                obs_want = get_obs_angle()
                vib_by_ob_left_for(0.1)
                if (obs_want-10) >= me or me >= (obs_want+10):    # 내가 보고 있는 방향이 진행 방향이 아니라면,
                    turn_direction = turn(obs_want, me)
                    if turn_direction == 'right':
                        print('right vibration')
                        vib_obs_right()     # 진동을 발생
                        while (obs_want-10) >= me or me >= (obs_want+10):  # 목표 방향 +-10 이내가 될 때 까지
                            me = get_angle()
                            if obs_want > 350 and me <= 10:
                                me += 360
                            print('내가 보고 있는 방향: '+str(me)+' / 맞춰야 할 방향: '+str(obs_want))
                            time.sleep(0.2)
                    elif turn_direction == 'left':
                        print('left vibration')
                        vib_obs_left()      # 진동을 발생
                        while (obs_want-10) >= me or me >= (obs_want+10):  # 목표 방향 +-10 이내가 될 때 까지
                            me = get_angle()
                            print('내가 보고 있는 방향: '+str(me)+' / 맞춰야 할 방향: '+str(obs_want))
                            time.sleep(0.2)
                loc.obs_event.clear()
                vib_stop()

        print('route:'+str(route))
        # print('pre_want: '+str(pre_want)+' / want:'+str(want)+' / me:'+str(me))
        print("진행 단계: "+str(now_index+1)+" / 전체 단계: "+str(route_len))
        print('이전 위치: '+str(pre_loc)+' / 현재 위치:'+str(now_loc)+" / 다음 위치: "+str(next_loc))
        # print('ALIVE THREAD: '+str(threading.active_count()))
        print('--------------------------')
        
        # event set 취소 하는 방법 -> event.clear()
        time.sleep(0.5)

    return 1


# 내가 가야할 방향을 좌표로 계산
def want_direction(now, next):
    x1 = now[1];    y1 = now[2]
    x2 = next[1];    y2 = next[2]
    x = x1 - x2;         y = y1 - y2

    diag = math.sqrt(x**2 + y**2)
    result = math.acos(diag/abs(x))
    degree = math.degrees(result)

    if x > 0 and y == 0:         # 서측  
        return 270          
    elif x < 0 and y == 0:      # 동측
        return 90           
    elif y > 0 and x == 0:      # 남측      
        return 180          
    elif y < 0 and x == 0:      # 북측    
        return 0            
    elif x < 0 and y < 0:       # 1사분면
        return 270 - degree
    elif x < 0 and y > 0:       # 4사분면
        return 270 + degree
    elif x > 0 and y < 0:       # 2사분면
        return 90 - degree
    elif x > 0 and y > 0:       # 3사분면
        return 90 + degree


# 방향 왼쪽으로 도는게 빠른지, 오른쪽으로 도는게 빠른지
def turn(want, me):                 
    if want >= me:
        left = 360 + me - want
        right = want - me
    elif want <= me:
        left = me - want
        right = 360 + want - me

    if right >= left:
        return 'left'
    else:
        return 'right'
