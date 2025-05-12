import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
FILE_PATH='../DATA/img/'
FILENAME=os.listdir(FILE_PATH)
img=cv2.imread(FILE_PATH+FILENAME[1],cv2.IMREAD_COLOR_RGB)
# cv2.imshow('[',img)
# cv2.waitKey()
# cv2.destroyAllWindows()
print(f'size: {img.size}, shape: {img.shape}')


def drawImage(row,col,imglst):
    fig,axes=plt.subplots(row,col)
    axes=axes.flatten() if col >1 else [axes]
    for ax,img in zip(axes, imglst):
        ax.imshow(img)
        ax.set_title(f'{img.shape}')
    plt.grid()
    plt.tight_layout()
    plt.show()


roi=img[200:800,200:1000]
# cv2.imshow('[',roi)
# cv2.waitKey()
# cv2.destroyAllWindows()
# print(roi.shape)
cv2.rectangle(img,(200,200),(800,1000),(255,0,0),100)
drawImage(1,1,[img])
# 200,200,800,1000

# convert컬러
# cv2.cvtColor('객체명',cv2.COLOR_RGB2BGR)
# ===========================================================
# 상대크기 조율
