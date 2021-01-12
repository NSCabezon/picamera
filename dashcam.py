import picamera
import os
import time
import json
import itertools
import constant
import datetime
from picamera import Color
import checks

def record():	
	with picamera.PiCamera() as camera:
		camera.resolution = (1920,1080)
		camera.framerate = 25

		now = datetime.datetime.now()
		timestamp = now.strftime("%d-%m-%y__%H-%M-%S")
		
		file_name = constant.videos_path + timestamp + ".h264"
		
		print('Recording to: ' + file_name)
		
		timeout = time.time() + constant.DURATION_SECS

		camera.start_recording(file_name, quality = 20)

		time.sleep(30)
		camera.stop_recording()
		time.sleep(3)

checks.checkFoldersExistance()
checks.check_space()

# record()