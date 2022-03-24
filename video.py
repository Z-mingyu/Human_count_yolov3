import base64
import cv2
import numpy as np
import time
import requests
from PIL import Image

from yolo import YOLO

yolo = YOLO()


#空调类，记录空调的权限和开关状态
class AirConditioner(object):
    def __init__(self):
        self.authority=False
        self.status="off"
    def authorize(self):
        self.authority=True
    def Turn_on(self):
        if self.authority:
            self.status="on"


#给服务器传数据
def post():
    #当前人数大于教室人数的1/3，则给予空调控制权（这里假设检测教室最多能容纳60人）
    if count/60>1/3:
        AC.authorize()
    url = "http://124.70.164.60/upload"
    files = {'file': ('current.bmp', open('current.bmp', 'rb'))}
    params = {'num': count, 'status': AC.status}
    r = requests.post(url,params=params,files=files)
if  __name__ == '__main__':
    #空调对象
    AC = AirConditioner()
    capture = cv2.VideoCapture(0)
    while(True):
        #打开摄像头进行人数检测
        ref,frame=capture.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(np.uint8(frame))
        frame,count=yolo.detect_image(frame)
        frame = np.array(frame)
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        frame = cv2.putText(frame, "Person: "+str(count), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        #base64_data = base64.b64encode(frame)
        cv2.imwrite("current.bmp",frame)
        # url = "http://hymplus.ltd/upload"
        # files = {'file': ('current.bmp', base64_data, 'image/png')}
        # params = {'num': count, 'status': AC.status}
        # r = requests.post(url, params=params, files=files)

        # 10分钟检测一次并将数据传给服务器
        post()
        time.sleep(600)

