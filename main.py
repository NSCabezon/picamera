import dashcam
import checks
import constant
import convertVideo

from gpiozero import Servo
from gpiozero import LED
from time import sleep

def record():
	count = 0

	while (checks.check_space() < constant.SPACE_LIMIT and count < 3):
		dashcam.record()
		count += 1

def convert():
	if checks.check_space() < constant.SPACE_LIMIT:
		convertVideo.convertVideos()

def moveServo():
	print("Trying to move servo at GPIO 14")
	led = LED(23)
	led.on()
	servo = Servo(14)
	servo.value = -1
	sleep(2)
	servo.value = 0
	sleep(2)
	servo.value = 1
	sleep(2)
	led.off()

print("What do you want to do?")
print("1 record in chunks of 10 min")
print("2 manually record non converted videos and delete the original")
print("3 both")
print("4 move servo at 14")

val = input("Enter your value: ")
if val == 1:
	record()
elif val == 2:
	convert()
elif val == 3: 
	record()
	convert()
elif val == 4:
	moveServo()
 