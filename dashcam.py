import picamera
from picamera import Color
import os
import time
import json
import itertools
import constant
import datetime
import checks
import convertVideo

def record():	
	with picamera.PiCamera() as camera:
		camera.resolution = (constant.resolution_width, constant.resolution_height)
		camera.framerate = constant.fps

		now = datetime.datetime.now()
		timestamp = now.strftime("%d-%m-%y__%H-%M-%S")
		
		file_name = constant.videos_path + timestamp + ".h264"
		
		print('Recording to: ' + file_name)

		camera.start_recording(file_name, quality = 20)

		camera.wait_recording(constant.DURATION_SECS)

		camera.stop_recording()
		time.sleep(3)
