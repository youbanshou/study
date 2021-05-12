import cv2
import os
import glob
import logging

#すべてのフレームで切り分け(使ってない)
def save_all_frames(video_path,dir_path,basename,ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return
    
    os.makedirs(dir_path,exist_ok=True)
    base_path=os.path.join(dir_path,basename)
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret,frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path,str(n).zfill(digit),ext),frame)
            n +=1
        else:
            return

#sec秒ごとにフレーム分け
def  save_all_sec_interval(video_path,frame):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return
    
    os.makedirs('./workdir', exist_ok=True)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    len_sec = round(frame / fps)


    cap.set(cv2.CAP_PROP_POS_FRAMES,round(fps * 147))
    
    ret,frame = cap.read()
    if ret:
        result_path = os.path.join('workdir', '147' +'.jpg')
        frame_trim = trim_img_ratio(frame)
        frame_trim_gray = cv2.cvtColor(frame_trim, cv2.COLOR_BGR2GRAY)
        ret2, frame_trim_binary = cv2.threshold(frame_trim_gray, 68, 255, cv2.THRESH_BINARY)
        print(ret2)
        cv2.imwrite(result_path,frame_trim_binary)

def trim_img_ratio(img):
    left = 0.35
    right = 0.35
    top = 0.43
    down = 0.47
    left_edge = int(img.shape[1] * left)
    right_edge = int(img.shape[1] - img.shape[1] * right)
    top_edge = int(img.shape[0] * top)
    down_edge = int(img.shape[0] - img.shape[0] * down)
    return img[top_edge:down_edge,left_edge:right_edge]




interval_sec = 1
videos_list = glob.glob('./movie/*')

if __name__=='__main__':
    for video_path in videos_list:
        save_all_sec_interval(video_path,147)