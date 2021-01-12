import picamera
from picamera import Color
import os
import time
import json
import itertools
import constant
import datetime
import checks

def record():	
	with picamera.PiCamera() as camera:
		camera.resolution = (1920,1080)
		camera.framerate = 25

		now = datetime.datetime.now()
		timestamp = now.strftime("%d-%m-%y__%H-%M-%S")
		
		file_name = constant.videos_path + timestamp + ".h264"
		
		print('Recording to: ' + file_name)

		camera.start_recording(file_name, quality = 20)

		camera.wait_recording(constant.DURATION_SECS)
		
		camera.stop_recording()
		time.sleep(3)

checks.checkFoldersExistance()
val = checks.check_space()

print("Percentage: %f" % val)

while checks.check_space() < constant.SPACE_LIMIT:
	record()