import picamera
from picamera import Color
import RPi.GPIO as GPIO
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

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7, GPIO.OUT)

		while True:
			GPIO.output(23, True)
			time.sleep(1)
			GPIO.output(23, False)
			time.sleep(1)

		camera.start_recording(file_name, quality = 20)

		camera.wait_recording(constant.DURATION_SECS)

		camera.stop_recording()
		time.sleep(3)
