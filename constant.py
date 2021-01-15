import os

#### CAMERA ####
resolution_width = 1280
resolution_height = 720
fps = 24

MINUTES_TO_RECORD = 10
DURATION_SECS = 60 * MINUTES_TO_RECORD
SPACE_LIMIT = 80  #percent

#### LEDS ####
LED_PIN = 4
SWITCH_PIN = 17
POWER_PIN = 27

#### PATHS ####
folder_root = "/home/pi/"
videos_folder = "videos/"
output_folder = "output/"

videos_path = folder_root + videos_folder
output_path = folder_root + output_folder