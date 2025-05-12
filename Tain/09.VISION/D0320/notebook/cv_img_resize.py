import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
FILE_PATH='../DATA/img/'
FILENAME=os.listdir(FILE_PATH)
# img=cv2.imread(FILE_PATH+FILENAME[1],cv2.IMREAD_COLOR_RGB)
# print(f'size: {img.size}, shape: {img.shape}')
# downimg=cv2.resize(img,(100,100),interpolation=cv2.INTER_AREA)
# print(f'size: {downimg.size}, shape: {downimg.shape}')
# # ===========================================================
# upimg1=cv2.resize(img,(700,700),interpolation=cv2.INTER_LINEAR)
# upimg2=cv2.resize(img,(700,700),interpolation=cv2.INTER_CUBIC)
# cv2.imshow('img',img)
# cv2.imshow('downimg',downimg)
# cv2.imshow('upimg1',upimg1)
# cv2.imshow('upimg2',upimg2)
# cv2.waitKey()
# cv2.destroyAllWindows()

def drawImage(row,col,imglst):
    fig,axes=plt.subplots(row,col)
    axes=axes.flatten() if col >1 else [axes]
    for ax,img in zip(axes, imglst):
        ax.imshow(img)
        ax.set_title(f'{img.shape}')
    plt.tight_layout()
    plt.show()

# drawImage(1,3,[downimg,upimg1,upimg2])
# convert컬러
# cv2.cvtColor('객체명',cv2.COLOR_RGB2BGR)
# ===========================================================
# 상대크기 조율
img=cv2.imread(FILE_PATH+FILENAME[1],cv2.IMREAD_COLOR_RGB)
print(f'size: {img.size}, shape: {img.shape}')
downimg=cv2.resize(img,None,None,0.5,0.5,interpolation=cv2.INTER_AREA)
print(f'size: {downimg.size}, shape: {downimg.shape}')
# ===========================================================
upimg1=cv2.resize(img,None,None,2,2,interpolation=cv2.INTER_LINEAR)
upimg2=cv2.resize(img,None,None,2,2,interpolation=cv2.INTER_CUBIC)
drawImage(1,3,[downimg,upimg1,upimg2])
