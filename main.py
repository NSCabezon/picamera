import dashcam
import checks
import constant
import convertVideo


def record():
	count = 0

	while (checks.check_space() < constant.SPACE_LIMIT and count < 3):
		dashcam.record()
		count += 1

def convert():
	if checks.check_space() < constant.SPACE_LIMIT:
		convertVideo.convertVideos()

print("What do you want to do?")
print("1 record in chunks of 10 min")
print("2 manually record non converted videos and delete the original")
print("3 both")

val = input("Enter your value: ")
if val == 1:
	record()
elif val == 2:
	convert()
elif val == 3: 
	record()
	convert()
 