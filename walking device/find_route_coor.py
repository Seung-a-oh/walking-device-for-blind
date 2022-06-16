# -*- coding: utf-8 -*-

from collections import deque

class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    # 휴리스틱 함수
    def h(self, n, dest):
        n_floor = n[0];    n_x = n[1];    n_y = n[2]
        dest_floor = dest[0];    dest_x = dest[1];    dest_y = dest[2]
        
        if n_floor - dest_floor == 0:
            x = abs(n_x - dest_x)
            y = abs(n_y - dest_y)

            return x+y
        else:
            x = abs(n_x - dest_x)
            y = abs(n_y - dest_y)

            return x+y+99


    def a_star_algorithm(self, start, stop):

        open_lst = set([start])  # 방문한 적이 있는 노드 목록(이웃이 항상 검사되는 것은 아님)
                                 # start부터 시작됨.
        closed_lst = set([])  # 방문한 노드의 목록(이웃은 항상 검사 완료됨.)

        poo = {}  # 시작부터 다른 모든 노드 까지의 현재 거리를 갖고 있음.
                  # 기본 값은 +무한대 임.
        poo[start] = 0

        par = {}  # 모든 노드의 adjac 매핑을 포함함.
        par[start] = start

        while len(open_lst) > 0:
            n = None

            # f()값이 가장 낮은 노드를 찾는다
            for v in open_lst:
                if n == None or poo[v] + self.h(v,stop) < poo[n] + self.h(n,stop):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop:   # 만약 현재 노드가 stop인 경우 처음부터 다시시작함.
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # 현재 노드의 모든 이웃에 대해 수행함.
            for (m, weight) in self.get_neighbors(n):
                if m not in open_lst and m not in closed_lst:  # 현재 노드가 open_lst와 closed_lst 두 곳에 모두 존재하지 않는 경우
                    open_lst.add(m)                          #현재 노드를 open_lst에 추가함. 
                    par[m] = n
                    poo[m] = poo[n] + weight

               #그렇지 않으면 먼저 n을 방문한 다음 m을 방문하는 것이 더 빠른지 확인함.
                else:  
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n        # 만약 그렇다면 par 데이터와 poo 데이터를 업데이트 함.

                        if m in closed_lst:  # 노드가 closed_lst에 있으면 open_lst로 이동.
                            closed_lst.remove(m)
                            open_lst.add(m)

            open_lst.remove(n)  #open_lst에서 n을 제거하고 closed_lst에 추가함.(그것의 이웃은 모두 검사완료된 상태.)
            closed_lst.add(n)

        print('Path does not exist!')
        return None

#최단경로탐색
adjac_lis = {
    #corner : (72,12)-ml403(C), (62,12)-ml402(C), (45,12)-정수기 앞 코너
    (4,108,12): [((4,100,12), 8)],                                                  
    (4,100,12): [((4,108,12), 8), ((4,90,12), 10)],                                  
    (4,90,12): [((4,100,12), 10), ((4,81,12), 9)],                                  
    (4,81,12): [((4,90,12), 9), ((4,72,12), 9)],                         
    (4,72,12): [((4,81,12), 9), ((4,72,19), 8), ((4,65,12), 7), ((4,65,19), 10)], 
    (4,72,19): [((4,72,12), 8), ((4,65,12), 7)],                                           
    (4,65,19): [((4,72,19), 7), ((4,65,12), 7), ((6,65,19), 99), ((4,72,12), 10)],                                   
    (4,65,12): [((4,65,19), 7), ((4,56,12), 9), ((4,72,12), 7)],              
    (4,56,12): [((4,65,12), 9), ((4,48,12), 8)],                                   
    (4,48,12): [((4,56,12), 8), ((4,45,12), 3)],                                             
    (4,45,12): [((4,48,12), 3), ((4,38,12), 7), ((4,45,2), 10)],                  
    (4,38,12): [((4,45,12), 7)],                                               
    (4,45,2):  [((4,45,12), 10)],
    (6,65,19): [((6,65,13), 7), ((4,65,19), 99)],
    (6,65,13): [((6,65,19), 7), ((6,71,13), 12)],
    (6,71,13): [((6,65,13), 12)],
    (6,56,13): [((6,65,13), 9), ((6,45,13), 11)],
    (6,45,13): [((6,56,13), 11)]
    #(7,65,19): [((7,65,11), 8),((4,65,19),99)],
    #(7,65,11): [((7,65,19),8),((7,71,11),6)],
    #(7,71,11): [((7,65,11), 6),((7,79,11),8)],
    #(7,79,11): [((7,71,11), 8)]                                                 
}

graph1 = Graph(adjac_lis)
# graph1.a_star_algorithm((12,31), (10,19)) #출발지~목적지
# graph1.a_star_algorithm((12,31), (12,13))
# graph1.a_star_algorithm((4,81,12), (7,79,11))
graph1.a_star_algorithm((4,81,12), (6,65,19))