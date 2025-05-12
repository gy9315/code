import struct
import cv2
import matplotlib.pyplot as plt
import os
import pandas as pd
FILENAME=os.listdir('../hw_D0320/DATA/cat_dog/')
FILEPATH='../hw_D0320/DATA/cat_dog/'
DATA=pd.DataFrame()
for x in FILENAME:
    img=cv2.imread(FILEPATH+x)
    try:
        b,g,r=cv2.split(img)
        if g.shape[0]>100 or g.shape[1]>100:
            g=cv2.resize(g,(100,100),interpolation=cv2.INTER_AREA)
        else:
            g=cv2.resize(g,(100,100),interpolation=cv2.INTER_CUBIC)
        g=cv2.flip(g,2)
        g=g.reshape(1,-1)
        DF=pd.DataFrame(g)
        DF['speices']=x.split('_')[0]
        DATA=pd.concat([DATA,DF])
    except ValueError: pass
    print(x)
DATA.to_csv('dog_cat_test.csv')
print(DATA)