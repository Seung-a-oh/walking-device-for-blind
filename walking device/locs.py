from threading import Event

event = Event()
mag_event = Event()
vib_event = Event()
ultra_left_event = Event() #not use yet
ultra_right_event = Event() # not use yet
heading_angle = 0
now_loc = (4,90,12)
ultra_left = 0.0
ultra_right = 0.0
