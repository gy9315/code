import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

img=cv2.imread('../DATA/img/gray.png',cv2.IMREAD_GRAYSCALE)
# img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
t,value=cv2.threshold(img,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
value=cv2.cvtColor(value,cv2.COLOR_BGR2RGB)
value1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,5)
value1=cv2.cvtColor(value1,cv2.COLOR_BGR2RGB)
value2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,5)
value2=cv2.cvtColor(value2,cv2.COLOR_BGR2RGB)
# cv2.imshow('bin',value2)
# cv2.waitKey()
# cv2.destroyAllWindows()
fig,axes=plt.subplots(1,3)
for x,y in zip(axes.flatten(),[value,value1,value2]):
    x.imshow(y)
    x.set_title('바보')
    x.set_xticks([])
    x.set_yticks([])
plt.show()