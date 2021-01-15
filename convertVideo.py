import constant
import os

def convertVideos():
	dirs = os.listdir(constant.videos_path)

	for file in dirs:
		input_file = constant.videos_path + file
		output_file = constant.output_path + file + ".mp4"
		
		if not os.path.exists(output_file):
			print("\nConverting: " + file)
			conversion_command = "MP4Box -add " + input_file + " " + output_file
			print(conversion_command)
			os.system(conversion_command)
			os.remove(input_file)
		else:
			print("File already converted")

	print("Conversion complete.")
	
