import torch
import numpy as np
import cv2
a=[[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]],[[21,22,23,24,25],[26,27,28,29,30]]]
a=torch.tensor(a)
# [3,2,5]
# layer 반환값, 배치사이즈, embedding
# print(a.permute(1,0,2))
# 배치사이즈 , layer 반환값, embedding
img=cv2.imread('../09.VISION/DATA/img/KakaoTalk_20250207_094909358_01.jpg')
# 1400, 1050, 3
img1=np.array(img)
img_list=[]
for x in np.split(img1,3,axis=2):
    x=np.transpose(x,(2,0,1))
    x=np.squeeze(x,0)
    img_list.append(x)
x=np.stack([img_list[-1],img_list[1],img_list[0]])     
