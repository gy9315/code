import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

img=cv2.imread('../DATA/img/gray.png',cv2.IMREAD_GRAYSCALE)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(img.shape)
b=np.zeros_like(img)
b[img>127]=255
b=np.uint8(b)
# cv2.imshow('bin',b)
# cv2.waitKey()
fig,axes=plt.subplots(3,2)
for x,y in zip(axes.flatten(),range(0,255,50)):
    c=cv2.threshold(img,y,255,cv2.THRESH_BINARY)
    x.imshow(c[1])
    x.set_title('바보')
    x.set_xticks([])
    x.set_yticks([])
plt.show()