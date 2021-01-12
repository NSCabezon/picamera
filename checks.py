import constant
import os
import psutil

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
		del_file_path = constant.folder_root + constant.videos_folder + "video%05d.h264" % i
		i = i + 1
		if os.path.exists(del_file_path):
			print ('Deleting: ' + del_file_path)
			os.remove(del_file_path)
			files_deleted = files_deleted + 1

			if(files_deleted >= constant.DELETE_FILES):
				break
	print('Completed.')

def check_space():
	print("Disk usage %f" % psutil.disk_usage(".").percent)
	if psutil.disk_usage(".").percent > constant.SPACE_LIMIT:
		clear_space()
