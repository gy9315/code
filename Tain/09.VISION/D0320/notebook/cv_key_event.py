# event: 사용자들의 마우스나 키보드로 발생하는 동작들
# ex) 마우스: 클릭,드래그, 마우스 누르기 & 떼기, 더블 클릭
# ex) 키보드: 입력한 키 값들 알파벳, 숫자, 기호 ...
import cv2
import matplotlib.pyplot as plt
import numpy as np
import struct
import os
FILE_NAME=os.listdir('../DATA/img/')
FILE_PATH='../DATA/img/'
file_list=[]
for x in FILE_NAME:
    if os.path.isfile(FILE_PATH+x):
        file_list.append(FILE_PATH+x)
for x in file_list:        
    color_img=cv2.imread(x)
    try:
        print(f'제목: {x}')
        print(f'차원: {color_img.ndim}')
        print(f'타입: {color_img.dtype}')
        print(f'shape: {color_img.shape}')
    except:
        pass
# 이미지 출력 및 이벤트 체크
    # cv2.imshow('[]',color_img)
    # key=cv2.waitKey()
    # if key==27:
    #     cv2.destroyAllWindows()
# ==============================================
img=cv2.imread(file_list[0])
b,g,r=cv2.split(img)
print(f'차원: {b.ndim}, shape: {b.shape}')
print(f'차원: {g.ndim}, shape: {g.shape}')
print(f'차원: {r.ndim}, shape: {r.shape}')
