# -*- coding: utf-8 -*-
from graph import adjac_lis as adj
from threading import Thread
from location import *
# import loc
import threading
from find_route_coor import *
from ultra_sa import *
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


def navigate():
    global now_index
    global pre_loc
    global want
    global me
    global evei
    global pre_want

    now_loc = get_locs()
    route = graph.a_star_algorithm((4,90,12), (6,71,13))
    route_len = len(route)
    if route_len > 1:
        want = xy_direction(route[0],route[1])        # 첫 진행 방향 초기화

    while now_loc != (6,71,13):
        
        if now_index >= 0:
            pre_loc = now_loc
        now_loc = get_locs()
        #만약 현재 위치가 (시나리오 상의)코너 전 비콘이면 
        # 값이 튄 경우 / 현재 감지한 x,y와 이전 위치의 x,y 값이 3 이상 차이 나면
        if pre_loc != (-1,-1):
            # 나와 내 주변의 이웃한 노드들을 저장해놓고, 값이 그 안에 있지 않으면 튄 값으로 판별
            pre_loc_list = adj[pre_loc]
            if now_loc not in pre_loc_list:
                print("보정 전 현재 위치: "+str(now_loc)+" 보정 전 이전 위치: "+str(pre_loc))
                now_loc = route[route.index(pre_loc)+1]
                print("보정 후 현재 위치: "+str(now_loc))
            elif abs(now_loc[0]-pre_loc[0]) >= 10 or abs(now_loc[1]-pre_loc[1]) >= 10:
                now_loc = route[route.index(pre_loc)+1]     # 루트 상의 이전(직전에 방문한) 노드의 다음 노드를 넣어줌
                print("out of range!!!")
        
        if now_loc not in route:        # 경로에서 이탈했으면
            now_index = 0
            # navigate((6,71,13))

        # 인덱스 range 초과 방지 하기 위해서
        if now_loc != (-1,-1):
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
            evei = 1
            
        pre_want = want
        if next_loc != (-1,-1):
            want = xy_direction(now_loc, next_loc) #수정
            # if now_loc == (4,65,19) and next_loc == (6, 65, 19): #4층 엘베 -> 6층 엘베 
            #     pre_want = 260
                
            if pre_want != want:                          # 코너면,
                print('pre_want와 want가 다릅니다.')

        
        # print('route:'+str(route))
        print('pre_want: '+str(pre_want)+' / want:'+str(want))
        # print("진행 단계: "+str(now_index)+" / 전체 단계: "+str(route_len))
        print('이전 위치: '+str(pre_loc)+' / 현재 위치:'+str(now_loc)+" / 다음 위치: "+str(next_loc))
        print('--------------------------')
        
        time.sleep(0.5)
    return 1
    
def xy_direction(now, next):
    global pre_want
    floor = now[0]
    x1 = now[1];    y1 = now[2]
    x2 = next[1];    y2 = next[2]
    x = x1 - x2;         y = y1 - y2

    if now[0]-next[0] != 0:
        if x==0 and y==0:
            pre_want = 260      # 6층 남쪽 각도 리턴
            return 260
    if floor == 4:            # 4층 회전
        if x > 0 and y == 0:           # x 좌표가 감소했으면
            return 43         # 서측
        elif x < 0 and y == 0:
            return 213        # 동측
        elif y > 0 and x == 0:         
            return 293        # 남측
        elif y < 0 and x == 0:         
            return 145        # 북측
        else:
            return 90         # 북서
    else:                     # 7층 회전
        if x > 0 and y == 0:      
            return 15         # 서측 4
        elif x < 0 and y == 0:
            return 190         # 동측 3  / 293,258
        elif y > 0 and x == 0:         
            return 260         # 남측 2 / 204,180
        elif y < 0 and x == 0:         
            return 97         # 북측 1 / 119
        else:               
            return 50        # 남서

def turn(want, me):         # 방향 맞출 때 왼쪽으로 도는게 빠른지, 오른쪽으로 도는게 빠른지
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


if __name__ == "__main__":
    location_thread = Thread(target=location_thread)
    location_thread.daemon = True
    location_thread.start()
    vth = Thread(target=detect_obstacle)
    vth.daemon = True
    vth.start()
    navigate()
