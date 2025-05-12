import cv2
import numpy as np
import matplotlib.pyplot as plt
filepath='../DATA/PNG.png'
img=cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
# 이미지 로딩 및 저장
print(f'type: {img.dtype}')
print(f'차원: {img.ndim}')
print(f'shape: {img.shape}')
save_name=f'../DATA/gray.png'
cv2.imwrite(save_name,img)