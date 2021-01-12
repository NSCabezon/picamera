import constant
import os

def checkFoldersExistance():
	print("Checking for: " + constant.videos_path)
	if !os.path.exists(constant.videos_path):
		os.makedirs(constant.videos_path)
	
	if !os.path.exists(constant.output_path):
		os.makedirs(constant.output_path)
	
	dirs = os.listdir(constant.videos_path)
	print(dirs)
	dirs.sort
	print(dirs)

checkFoldersExistance()