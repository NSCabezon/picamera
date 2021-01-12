import os

DURATION_MINS = 60
DURATION_SECS = 60 * DURATION_MINS
SPACE_LIMIT = 80
MAX_FILES = 99999
DELETE_FILES = 10

LED_PIN = 4
SWITCH_PIN = 17
POWER_PIN = 27

folder_root = "/home/pi/"
videos_folder = "videos/"
output_folder = "output/"

videos_path = folder_root + videos_folder
output_path = folder_root + output_folder