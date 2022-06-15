from re import A
from threading import Event

event = Event()
mag_event = Event()
vib_event = Event()
obs_event = Event()
ultra_left_event = Event() #not use yet
ultra_right_event = Event() # not use yet

dest_bearing = 'a'

heading_angle = 0
obs_angle = 0

now_loc = (-1,-1)
now_locs = (4,90,12)

ultra_left = 0.0
ultra_right = 0.0
