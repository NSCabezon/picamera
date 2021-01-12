import constant
import os

dirs = os.listdir(constant.videos_path)

for file in dirs:
	input_file = constant.videos_path + file
	output_file = constant.output_path + file
	
	print("Converting: " + file)
	conversion_command = "MP4Box -add " + input_file + " " + output_file + ".mp4"
	print conversion_command
	os.system(conversion_command)

print("Conversion complete.")
	
