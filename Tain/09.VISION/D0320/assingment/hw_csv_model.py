import struct
import cv2
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
FILENAME=os.listdir('../hw_D0320/DATA/cat_dog/')
FILEPATH='../hw_D0320/DATA/cat_dog/'
DATA=pd.DataFrame()
for x in FILENAME:
    img=cv2.imread(FILEPATH+x)
    b,g,r=cv2.split(img)
    g=cv2.resize(g,(100,100),interpolation=cv2.INTER_CUBIC)
    for r in list(range(0,180,10))+list(map(lambda x:-x,range(0,180,10))):
        ra=cv2.getRotationMatrix2D((50,50),r,1)
        new=cv2.warpAffine(g,ra,(100,100))
        # cv2.imshow('g',new)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        new=new.reshape(1,-1)
        DF=pd.DataFrame(new)
        DF['speices']=x.split('_')[0]
        # print(DF)
        DATA=pd.concat([DATA,DF])
        # else:pass
        print(x,r)
DATA.to_csv('dog_cat.csv')
# print(DATA)