# -*- coding: utf-8 -*-
# “”“
# 作者 : zhangmingyu
# 日期 : 2022年 03月 27日
# ”“”

#调用摄像头或者读取本地视频流进行实时检测

import cv2
import numpy as np

from PIL import Image

from yolo import YOLO

yolo = YOLO()






if  __name__ == '__main__':
    #调用本机摄像头
    capture = cv2.VideoCapture(0)
    #读取本地视频流
    #capture = cv2.VideoCapture("video/video.mp4")
    ref, frame = capture.read()
    while(ref):

        #打开摄像头进行人数检测
        ref, frame = capture.read()
        #颜色格式转换，因为opencv用的是BGR格式而PIL用的是RGB格式，yolo算法使用的PIL库
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(np.uint8(frame))
        frame,count=yolo.detect_image(frame)
        frame = np.array(frame)
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        frame = cv2.putText(frame, "Person: "+str(count), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("video",frame)

        #按 q 退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #保存检测后图片到本地
        #cv2.imwrite("current_local.bmp",frame)


