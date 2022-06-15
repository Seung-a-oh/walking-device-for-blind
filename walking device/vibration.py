# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os
LEFT = 12
RIGHT = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LEFT, GPIO.OUT)
GPIO.setup(RIGHT, GPIO.OUT)

def once():
	GPIO.output(LEFT, True)
	time.sleep(3)
	GPIO.output(LEFT, False)

def obstacle():
	GPIO.output(LEFT, True)
	time.sleep(0.2)
	GPIO.output(LEFT, False)

def vib_left():					# time은 회전 각도에 따라
	GPIO.output(LEFT, True)
	os.system('omxplayer ./mp3/vibration/left.mp3')

def vib_right():
	GPIO.output(RIGHT, True)
	os.system('omxplayer ./mp3/vibration/right.mp3')


def vib_stop():
    GPIO.output(LEFT, False)
    GPIO.output(RIGHT, False)

def vib_left_2s():					# time은 회전 각도에 따라
	GPIO.output(LEFT, True)
	os.system('omxplayer ./mp3/vibration/left.mp3')# 좌회전 음성
	#time.sleep(2)
	GPIO.output(LEFT, False)

def vib_right_2s():
	GPIO.output(RIGHT, True)
	os.system('omxplayer ./mp3/vibration/right.mp3') 
	time.sleep(2)
	GPIO.output(RIGHT, False)

def vib_left_4s():					# time은 회전 각도에 따라
	GPIO.output(LEFT, True)
	os.system('omxplayer ./mp3/vibration/left.mp3')
	time.sleep(4)
	GPIO.output(LEFT, False)

def vib_left_for(t):
	GPIO.output(LEFT, True)
	time.sleep(t)
	GPIO.output(LEFT, False)

def vib_right_for(t):
	GPIO.output(RIGHT, True)
	time.sleep(t)
	GPIO.output(RIGHT, False)

def vib_obs_left():					# time은 회전 각도에 따라
	GPIO.output(LEFT, True)
	os.system('omxplayer ./mp3/vibration/obstacle_right_2.mp3')

def vib_obs_right():
	GPIO.output(RIGHT, True)
	
def vib_by_ob_right_for(t):
	GPIO.output(RIGHT, True)
	time.sleep(t)
	GPIO.output(RIGHT, False)

def vib_by_ob_left_for(t):
	GPIO.output(LEFT, True)
	os.system('omxplayer ./mp3/vibration/obstacle_right_2.mp3')
	time.sleep(t)
	GPIO.output(LEFT, False)

def vib_both_for(t):
	GPIO.output(RIGHT, True)
	GPIO.output(LEFT, True)
	time.sleep(t)
	GPIO.output(RIGHT, False)
	GPIO.output(LEFT, False)

# PWM
# myPwm = GPIO.PWM(LEFT, 1000) # LEFT, frequency
# myPwm.start(50)

# Frequency  변경 (Hz)
# myPwm.ChangeFrequency(1500)

# for i in range(100):
# 	myPwm.ChangeDutyCycle(i)	#0~100%
# 	time.sleep(0.02)
	
# myPwm.stop()

if __name__ == "__main__":
	# vib_left_2s()
	# time.sleep(3)
	# vib_left_4s
	# vib_stop()
        #vib_right_2s()
        #vib_by_ob_right_for(0.1)
    vib_stop()
	# time.sleep(1)
	# vib_left()
