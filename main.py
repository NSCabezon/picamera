import dashcam
import checks
import constant
import convertVideo

count = 0

while (checks.check_space() < constant.SPACE_LIMIT and count < 3):
	dashcam.record()
	count += 1

if checks.check_space() < constant.SPACE_LIMIT:
	convertVideo.convertVideos()