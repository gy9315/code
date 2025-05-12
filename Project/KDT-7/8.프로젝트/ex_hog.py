import os
import cv2
from skimage.feature import hog
import numpy as np
import pandas as pd
filename=os.listdir('./DATA/test/')
filename.sort(key=lambda x: int(''.join([y for y in x if y.isnumeric()])))
a=range(0,len(filename)-13,13)
b=range(13,len(filename),13)
data_list=[]
for x,y in zip(a,b):
    data_list.append(filename[x:y])
data_list.extend([filename[len(filename)-13:]])
# =========================================================================
hog_list=[]
for data in data_list:
    hog_file_list=[]
    for file in data:
        path='./DATA/test/'+file
        img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        img=cv2.resize(img,(100,100))
        hog1=hog(img,orientations=9,pixels_per_cell=(8,8),cells_per_block=(2,2),feature_vector=True)
        hog_file_list.append(np.mean(hog1))
    hog_list.append(hog_file_list)
    
DF=pd.DataFrame(hog_list)
# DF['damage']=1
DF.to_csv('./DATA/test_damage_nomask.csv',index=None)
