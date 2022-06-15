# -*- coding: utf-8 -*-
import io
import json

Beacon = dict()

#1그룹
beacon1 = dict()
# beacon1["location"] = "108,12"
beacon1["place"] = "ml409"
beacon1["group"] = (4,108,12)
Beacon["00:19:01:73:ec:80"] = beacon1
beacon2 = dict()
# beacon2["location"] = "108,12"
beacon2["place"] = "ml410"
beacon2["group"] = (4,108,12)
Beacon["00:19:01:73:e2:31"] = beacon2

#2그룹
beacon3 = dict()
# beacon3["location"] = "100,12"
beacon3["place"] = "ml407"
beacon3["group"] = (4,100,12)
Beacon["00:19:01:72:9e:d9"] = beacon3
beacon4 = dict()

# beacon4["location"] = "100,12"
beacon4["place"] = "ml412"
beacon4["group"] = (4,100,12)
Beacon["00:19:01:73:ee:62"] = beacon4

#3그룹
beacon5 = dict()
# beacon5["location"] = "90,12"
beacon5["place"] = "ml405"
beacon5["group"] = (4,90,12)
Beacon["00:19:01:70:82:af"] = beacon5
beacon6 = dict()
# beacon6["location"] = "90,12"
beacon6["place"] = "ml413"
beacon6["group"] = (4,90,12)
Beacon["00:19:01:73:ee:74"] = beacon6

#4그룹
beacon7 = dict()
# beacon7["location"] = "81,12"
beacon7["place"] = "ml404"
beacon7["group"] = (4,81,12)
Beacon["00:19:01:73:ec:11"] = beacon7
beacon8 = dict()
# beacon8["location"] = "81,12"
beacon8["place"] = "ml414"
beacon8["group"] = (4,81,12)
Beacon["00:19:01:73:e7:b7"] = beacon8

#6그룹
beacon9 = dict()
# beacon9["location"] = "72,12"
beacon9["place"] = "ml403(C)"
beacon9["group"] = (4,72,12)
Beacon["00:19:01:72:9e:89"] = beacon9
beacon10 = dict()
beacon10["location"] = "72,12"
beacon10["place"] = "ml403(C)"
beacon10["group"] = (4,72,12)
Beacon["00:19:01:73:e7:1b"] = beacon10

#7그룹
beacon11 = dict()
# beacon11["location"] = "72,19"
beacon11["place"] = "exit"
beacon11["group"] = (4,72,19)
Beacon["00:19:01:73:e2:1d"] = beacon11
beacon12 = dict()
# beacon12["location"] = "72,19"
beacon12["place"] = "exit"
beacon12["group"] = (4,72,19)
Beacon["00:19:01:73:ec:a9"] = beacon12

#8그룹
beacon13 = dict()
# beacon13["location"] = "65,19"
beacon13["place"] = "4F_EV"
beacon13["group"] = (4,65,19)
Beacon["00:19:01:73:ee:53"] = beacon13
beacon14 = dict()
# beacon14["location"] = "65,19"
beacon14["place"] = "4F_EV"
beacon14["group"] = (4,65,19)
Beacon["00:19:01:73:ee:4a"] = beacon14

#9그룹
beacon15 = dict()
# beacon15["location"] = "65,12"
beacon15["place"] = "ml402(C)"
beacon15["group"] = (4,65,12)
Beacon["00:19:01:72:9e:c7"] = beacon15
beacon16 = dict()
# beacon16["location"] = "65,12"
beacon16["place"] = "ml415"
beacon16["group"] = (4,65,12)
Beacon["00:19:01:73:ec:30"] = beacon16

#12그룹
beacon17 = dict()
# beacon17["location"] = "56,12"
beacon17["place"] = "ml401"
beacon17["group"] = (4,56,12)
Beacon["00:19:01:70:80:d9"] = beacon17
beacon18 = dict()
# beacon18["location"] = "56,12"
beacon18["place"] = "ml416"
beacon18["group"] = (4,56,12)
Beacon["00:19:01:73:ec:ac"] = beacon18

#13그룹
beacon19 = dict()
# beacon19["location"] = "48,12"
beacon19["place"] = "toilet"
beacon19["group"] = (4,48,12)
Beacon["00:19:01:72:9e:eb"] = beacon19
beacon20 = dict()
# beacon20["location"] = "48,12"
beacon20["place"] = "toilet"
beacon20["group"] = (4,48,12)
Beacon["00:19:01:73:e2:a8"] = beacon20

#14그룹
beacon21 = dict()
# beacon21["location"] = "45,12"
beacon21["place"] = "corner"
beacon21["group"] = (4,45,12)
Beacon["00:19:01:73:e4:c5"] = beacon21
beacon22 = dict()
# beacon22["location"] = "45,12"
beacon22["place"] = "corner"
beacon22["group"] = (4,45,12)
Beacon["00:19:01:73:ee:af"] = beacon22

#15그룹
beacon23 = dict()
# beacon23["location"] = "38,12"
beacon23["place"] = "ml427"
beacon23["group"] = (4,38,12)
Beacon["00:19:01:73:f3:0a"] = beacon23
beacon24 = dict()
# beacon24["location"] = "38,12"
beacon24["place"] = "ml417"
beacon24["group"] = (4,38,12)
Beacon["00:19:01:73:f3:2e"] = beacon24

#16그룹
beacon25 = dict()
# beacon25["location"] = "45,2"
beacon25["place"] = "4F_EV2"
beacon25["group"] = (4,45,2)
Beacon["00:19:01:72:a1:75"] = beacon25
beacon26 = dict()
# beacon26["location"] = "45,2"
beacon26["place"] = "4F_EV2"
beacon26["group"] = (45,2)
Beacon["00:19:01:72:9e:f1"] = beacon26


# ------------------ 6층 -----------------


#17그룹
beacon27 = dict()
beacon27["place"] = "6F_EV"
beacon27["group"] = (6,65,19)
Beacon["00:19:01:73:ec:2f"] = beacon27
beacon28 = dict()
beacon28["place"] = "6F_EV"
beacon28["group"] = (6,65,19)
Beacon["00:19:01:73:e4:83"] = beacon28

'''
beacon27 = dict()
beacon27["place"] = "7F_EV"
beacon27["group"] = (7,65,19)
Beacon["00:19:01:73:ec:2f"] = beacon27
beacon28 = dict()
beacon28["place"] = "7F_EV"
beacon28["group"] = (7,65,19)
Beacon["00:19:01:73:e4:83"] = beacon28
'''

#18그룹
beacon29 = dict()
beacon29["place"] = "ML618(C)"
beacon29["group"] = (6,65,13)
Beacon["00:19:01:73:e3:56"] = beacon29
beacon30 = dict()
beacon30["place"] = "ML618(C)"
beacon30["group"] = (6,65,13)
Beacon["00:19:01:73:ee:36"] = beacon30
'''
beacon29 = dict()
beacon29["place"] = "ML718"
beacon29["group"] = (7,65,11)
Beacon["00:19:01:73:e3:56"] = beacon29
beacon30 = dict()
beacon30["place"] = "ML718"
beacon30["group"] = (7,65,11)
Beacon["00:19:01:73:ee:36"] = beacon30
'''

#19그룹
beacon31 = dict()
beacon31["place"] = "ML618"
beacon31["group"] = (6,71,13)
Beacon["00:19:01:72:a1:7b"] = beacon31
beacon32 = dict()
beacon32["place"] = "ML618"
beacon32["group"] = (6,71,13)
Beacon["00:19:01:72:9e:dd"] = beacon32

#20그룹
beacon33 = dict()
beacon33["group"] = (6,56,13)
Beacon["00:19:01:73:eb:ff"] = beacon33
beacon34 = dict()
beacon34["group"] = (6,56,13)
Beacon["00:19:01:73:f5:c9"] = beacon34

#21그룹
beacon35 = dict()
beacon35["group"] = (6,45,13)
Beacon["00:19:01:73:ee:c3"] = beacon35
beacon36 = dict()
beacon36["group"] = (6,45,13)
Beacon["00:19:01:73:ee:87"] = beacon36


'''
beacon31 = dict()
beacon31["place"] = "7F_C"
beacon31["group"] = (7,71,11)
Beacon["00:19:01:72:a1:1b"] = beacon31
beacon32 = dict()
beacon32["place"] = "7F_C"
beacon32["group"] = (7,71,11)
Beacon["00:19:01:72:9e:dd"] = beacon32
'''
#20그룹
# beacon33 = dict()
# beacon33["place"] = "7F_STARTUP_DOOR"
# beacon33["group"] = (7,79,11)
# Beacon["00:19:01:73:ee:37"] = beacon33
# beacon34 = dict()
# beacon34["place"] = "7F_STARTUP_DOOR"
# beacon34["group"] = (7,79,11)
# Beacon["00:19:01:73:e2:a9"] = beacon34

with io.open('./pair.json', 'wb',
# encoding='utf-8'
)as make_file:
    json.dump(Beacon, make_file)
print("위치 좌표 파일이 현재 위치에 'pair.json'으로 갱신되었습니다.")
