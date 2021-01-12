import os

if not os.path.exists(output_path):
	os.makedirs(output_path)
	print("Created output folder.")
else:
	print("Output folder found")

i=START_INDEX

dirs = os.listdir(videos_path)

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
	
