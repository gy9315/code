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
# imgx=cv2.flip(img,0)
# drawImage(1,1,[imgx])
# imgy=cv2.flip(img,-1)
# drawImage(1,1,[imgy])
# 200,200,800,1000

# convert컬러
# cv2.cvtColor('객체명',cv2.COLOR_RGB2BGR)
# ===========================================================
# 상대크기 조율
img40=cv2.getRotationMatrix2D((700,525),-40,1)
rot=cv2.warpAffine(img,img40,(1400,1050),None,None,cv2.BORDER_REFLECT)
drawImage(1,1,[rot])