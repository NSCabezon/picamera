import constant
import os

def convertVideos():
	dirs = os.listdir(constant.videos_path)

	for file in dirs:
		input_file = constant.videos_path + file
		output_file = constant.output_path + file
		
		if not os.path.exists(output_file):
			print("\nConverting: " + file)
			conversion_command = "MP4Box -add " + input_file + " " + output_file + ".mp4"
			print(conversion_command)
			os.system(conversion_command)
		else:
			print("File already converted")

	print("Conversion complete.")
	
