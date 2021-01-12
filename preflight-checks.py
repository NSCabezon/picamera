import constant
import os

def checkFoldersExistance():
	print("Checking for existance of: " + constant.videos_path)
	if not os.path.exists(constant.videos_path):
		os.makedirs(constant.videos_path)
		print("Created")
	else:
		print("Exists, no need to create it")
	
	print("Checking for existance of: " + constant.output_path)
	if not os.path.exists(constant.output_path):
		os.makedirs(constant.output_path)
		print("Created")
	else:
		print("Exists, no need to create it")

def clear_space():
	print('Clearing space...')
	i = 0
	files_deleted = 0
	while i < MAX_FILES:
		del_file_path = folder_root + videos_folder + "video%05d.h264" % i
		i = i + 1
		if os.path.exists(del_file_path):
			print ('Deleting: ' + del_file_path)
			os.remove(del_file_path)
			files_deleted = files_deleted + 1

			if(files_deleted >= DELETE_FILES):
				break
	print('Completed.')

def check_space():
	if(psutil.disk_usage(".").percent > SPACE_LIMIT):
		clear_space()

checkFoldersExistance()

check_space()
