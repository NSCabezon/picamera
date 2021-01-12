import picamera
import os
import serial
import pynmea2
import time
import json
import itertools
import RPi.GPIO as GPIO
import constant
import datetime
from picamera import Color
import checks

checks.checkFoldersExistance()
checks.check_space()

with picamera.PiCamera() as camera:
	camera.resolution = (1920,1080)
	camera.framerate = 24

	now = datetime.datetime.now()
	timestamp = now.strftime("%d-%m-%y_%H:%M:%S")
	
	file_name = constant.videos_path + timestamp
	
	print('Recording to %s' % file_name)
	print("Time to record: %d secs" % constant.DURATION_SECS)
	
	timeout = time.time() + constant.DURATION_SECS

	camera.start_recording(file_name, quality = 20)

	time.sleep(30)
	camera.stop_recording()
	time.sleep(3)
