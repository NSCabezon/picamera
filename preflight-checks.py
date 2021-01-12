import constant
import os

def checkFoldersExistance():
	print("Checking for: " + constant.videos_path)
	if not os.path.exists(constant.videos_path):
		os.makedirs(constant.videos_path)
		print("Created")
	
	print("Checking for: " + constant.output_path)
	if not os.path.exists(constant.output_path):
		os.makedirs(constant.output_path)
		print("Created")

checkFoldersExistance()