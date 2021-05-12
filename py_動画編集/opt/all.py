import cv2
import os
import glob
import thumbnail
import judge
import logging

logging.basicConfig(filename='./logger.log', level=logging.DEBUG)



frames_path_list = glob.glob('./workdir/*')


for video_path in videos_list:
    save_all_sec_interval(video_path,interval_sec)
    




