import cv2
import numpy as np
import matplotlib.pyplot as plt
# 이미지 불러오기
img=cv2.imread('../DATA/KakaoTalk_20250207_094909358_01.jpg',cv2.IMREAD_COLOR_RGB)
print(f'type: {img.dtype}')
print(f'차원: {img.ndim}')
print(f'shape: {img.shape}')
# --------------------------
# plt.imshow(img)
# cv2.imshow('myDog',img)
# cv2.waitKey()  # 지정한 시간 후 닫기(입력값 X: 무한대기)
# cv2.destroyAllWindows() # 프로그램 종료
# plt.show()
# ==================================================================================
# gray flag이용
# ==================================================================================
# grayimg=cv2.imread('../DATA/KakaoTalk_20250207_094909358_01.jpg',cv2.IMREAD_GRAYSCALE)
# print(f'type: {grayimg.dtype}')
# print(f'차원: {grayimg.ndim}')
# print(f'shape: {grayimg.shape}')
# cv2.imshow('myDog',grayimg)
# cv2.waitKey()  # 지정한 시간 후 닫기(입력값 X: 무한대기)
# cv2.destroyAllWindows() # 프로그램 종료