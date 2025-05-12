import cv2
import numpy as np
import matplotlib.pyplot as plt
# 데이터 준비
device_id=0 # 기기에 연결된 카메라 번호
video_file='../DATA/video/'
# 카메라 연결
camera=cv2.VideoCapture(device_id)
# camera=cv2.VideoCapture(f"{video_file}big_buck.avi")
print(camera.isOpened())
while True:
    ret,img=camera.read()
    if ret:
        cv2.imshow('[]',img)
        key=cv2.waitKey(10)
        if key==27:
            break
    else: pass
## 카메라 해제 및 영상 출력창 닫기
camera.release()
cv2.destroyAllWindows()