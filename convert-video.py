import os
import constant

dirs = os.listdir(constant.videos_path)
print(dirs)
dirs.sort
print(dirs)

for file in dirs:
	input_file = videos_path + "/" + file
	output_file = output_path + "/" + file
		
	print("Checking for existance of:  <<" + file + ">>")

	if os.path.exists(input_file):
		print("Converting: " + input_file)
		conversion_command = "MP4Box -add " + input_file + " " + output_file + ".mp4"
		print conversion_command
		os.system(conversion_command)
	else: 
		print("File <" + input_file + "> does not exist")

print("Conversion complete.")
	
