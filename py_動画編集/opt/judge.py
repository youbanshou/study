import cv2
import os
import glob
import thumbnail
import logging
import re
from natsort import natsorted

logging.basicConfig(filename='./logger.log', level=logging.INFO)
frames_path_list = glob.glob('./workdir/*')




#マッチング判定
def judge_match(frame_path,template_path):
    template = cv2.imread(template_path) #検索元画像ファイルパスを指定
    frame = cv2.imread(frame_path) #検索先画像のファイルパスを指定
    result = cv2.matchTemplate(frame,template, cv2.TM_CCORR_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

    logging.info(str(maxVal)+':'+str(frame_path))
    if 0.90 < maxVal:
        return True
    else:
        return False

#開始画像探索
print('開始画像探索')
startlist = list()
for frame_path in natsorted(frames_path_list):
    ret = judge_match(frame_path,'./start_img.jpg')
    if ret:
        startlist.append(int(re.sub("\\D", "", frame_path)))

#終了画像探索
print('終了画像探索')
endlist = list()
for frame_path in natsorted(frames_path_list):
    ret = judge_match(frame_path,'./end_img.jpg')
    if ret:
        endlist.append(int(re.sub("\\D", "", frame_path)))

num = startlist[0]
for i in startlist[1:]:
    if num + 20 > i:
        startlist.remove(i)
    else:
        num = i

num = endlist[0]
for i in endlist[1:]:
    if num + 30 > i:
        endlist.remove(num)
        num = i
    else:
        num = i

