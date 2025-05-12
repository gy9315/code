import cv2
import numpy as np
import torch

gray=cv2.imread('../DATA/KakaoTalk_20250207_094909358_01.jpg',cv2.IMREAD_GRAYSCALE)
img=cv2.imread('../DATA/KakaoTalk_20250207_094909358_01.jpg')
list1=[]
for x in [gray,img]:
    y=cv2.resize(x,(50,50))
    list1.append(y)
print(list1[0].shape,list1[1].shape)
img=np.transpose(list1[1],[2,1,0])
list2=np.split(img,2,axis=3)
print(len(list2))
# cv2.imshow('img',img)
# cv2.waitKey()