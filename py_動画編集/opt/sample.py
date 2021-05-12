import cv2
import os
import glob

videos_list = glob.glob('./movie/*')
video = cv2.VideoCapture(videos_list[0])
interval_sec = 1
out_file = './workdir/1our.mp4'

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH)) # 動画の画面横幅
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 動画の画面縦幅
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) # 総フレーム数
frame_rate = int(video.get(cv2.CAP_PROP_FPS)) # フレームレート(fps)
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # ファイル形式(ここではmp4)
size = (width,height)
writer = cv2.VideoWriter('./result/outtest.mp4', fmt, frame_rate, size)

for i in range(30*60*7):

    ret,frame = video.read()
    writer.write(frame)

writer.release()
video.release()
cv2.destroyAllWindows()
