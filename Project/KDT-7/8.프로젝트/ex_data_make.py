import cv2
import numpy as np
import os
filename=os.listdir('./DATA/normal_nomask/')
count1=0
for number in range(100):
    for x in filename:
        path='./DATA/normal_nomask/'+x
        img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        # cv2.imshow('img',img)
        # cv2.waitKey()
        a,b=img.shape
        count=np.random.randint(10,100,1)
        # print(count)
        for num in range(0,count[0]):
            c=np.random.randint(0,a)
            d=np.random.randint(0,b)
            img[c,d]=255
        img=cv2.resize(img,(100,100))
        cv2.imwrite(f'./DATA/normal_nomask_train/normal{str(count1)}_{x.split(".")[0]}.jpg',img)
        
        # print('./DATA/normal_mask/damage'+str(count1)+'_'+x.split('.')[0])
    count1+=1
        # cv2.imshow('img',img)
        # cv2.waitKey()