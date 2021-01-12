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

# with picamera.PiCamera() as camera:
# 	camera.resolution = (1920, 1080)
# 	camera.framerate = 25

# 	now = datetime.datetime.now()
# 	timestamp = now.strftime("%d-%m-%y_%H:%M:%S")
	
# 	file_name = constant.videos_path + timestamp
# 	file_name2 = constant.videos_path + "video%05d" % 1
	
# 	print('Recording to: ' + file_name)
# 	print("Time to record '%d' secs" % constant.DURATION_SECS)
	
# 	timeout = time.time() + constant.DURATION_SECS

# 	camera.start_recording(file_name2, quality = 20)

# 	time.sleep(30)
# 	camera.stop_recording()
# 	time.sleep(3)

DURATION = 60
SPACE_LIMIT = 80
MAX_FILES = 99999
DELETE_FILES = 10

LED_PIN = 4
SWITCH_PIN = 17
POWER_PIN = 27

folder_root = "/home/pi/"
videos_folder = "videos/"
file_number = 0

if os.path.isfile('config_dashcam.json'):
	f = open('config_dashcam.json', 'r')
	config_dashcam = json.load(f)
	file_number = config_dashcam['file']['number']
	print('Obtained: ')
    	print(file_number)

else:
	print ('File not found. Creating new with 0...')
	file_number = 0
	config_dashcam = {}
	config_dashcam['file'] = { 'number' : file_number }
	with open('config_dashcam.json', 'w') as f:
		json.dump(config_dashcam, f)
	print('Save complete')

if not os.path.exists(videos_folder):
	os.makedirs(videos_folder)
	print ('Created videos folder.')

with picamera.PiCamera() as camera:
	camera.resolution = (1920,1080)
	camera.framerate = 25

 	while file_number < MAX_FILES:
		file_number = file_number + 1
		file_name = folder_root + videos_folder + "video%05d.h264" % file_number
		config_dashcam = {}
		config_dashcam['file'] = { 'number' : file_number }
        	with open('config_dashcam.json', 'w') as f:
	    		json.dump(config_dashcam, f)

		print('Recording to %s' % file_name)
		timeout = time.time() + DURATION

		camera.start_recording(file_name, quality = 20)

		time.sleep(30)
		camera.stop_recording()
		time.sleep(3)
