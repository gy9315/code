def split_video(video):
    import cv2
    camera=cv2.VideoCapture(video)
    count=0
    _,img=camera.read()
    idx=cv2.selectROI('a',img,None,None)
    print(idx)
    new=img[idx[1]:idx[1]+idx[3],idx[0]:idx[0]+idx[2]]
    new_list=[]
    while True:
        ret,img=camera.read()
        if ret:
            new=img[idx[1]:idx[1]+idx[3],idx[0]:idx[0]+idx[2]]
            cv2.imshow('a',new)
            key=cv2.waitKey(1)
            if key==27:
                cv2.destroyAllWindows()
                break
            print(count)
            if not count%30:
                new_list.append(new)
            count+=1
        else:
            cv2.destroyAllWindows()
            break
    return new_list[:13]

def contour_Canny(new_list):
    import cv2
    import os
    img_list=[]
    for img_file in new_list:
        img=cv2.cvtColor(img_file,cv2.COLOR_BGR2GRAY)
        clahe=cv2.createCLAHE(clipLimit=3,tileGridSize=(16,16))
        img=clahe.apply(img)
        img=cv2.Canny(img,120,250)
        a,b=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # x=cv2.selectROI('a',img,None,None)
        # print(x)
        list1=[]
        for idx,con in enumerate(a):
            area=cv2.contourArea(con)
            list1.append(area)
            if area<1:
                continue
            x,y,w,h=cv2.boundingRect(con)
            extent = area / (w * h)
            if 35<x<180 and 150<y<265  and extent>0.02:pass
                # img1=cv2.rectangle(img,(x,y),(x+w,y+h),(0,),-1)
                # cv2.drawContours(img,a,idx,(0,),thickness=cv2.FILLED)
        img_list.append(img)
    return img_list

def trans_HOG(img_list):
    import os
    import cv2
    from skimage.feature import hog
    import numpy as np
    import pandas as pd
    a=range(0,len(img_list)-13,13)
    b=range(13,len(img_list),13)
    data_list=[]
    for x,y in zip(a,b):
        data_list.append(img_list[x:y])
    data_list.extend([img_list[len(img_list)-13:]])
    # =========================================================================
    hog_list=[]
    for data in data_list:
        hog_file_list=[]
        for img_data in data:
            img=cv2.resize(img_data,(100,100))
            hog1=hog(img,orientations=9,pixels_per_cell=(8,8),cells_per_block=(2,2),feature_vector=True)
            hog_file_list.append(np.mean(hog1))
        hog_list.append(hog_file_list)   
    DF=pd.DataFrame(hog_list)
    print(DF)
    return DF


a=split_video('./DATA/normal(1).mp4')
img_list=contour_Canny(a)
test=trans_HOG(img_list)


from sklearn.utils import all_estimators 
from sklearn.metrics import classification_report,precision_score,recall_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegressionCV
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
normal=pd.read_csv('./DATA/normal_cup.csv')
normal_nomask=pd.read_csv('./DATA/normal_nomask_cup.csv') 
damage=pd.read_csv('./DATA/damage_cup.csv') 
damage_nomask=pd.read_csv('./DATA/damage_nomask_cup.csv') 
dataDF=pd.concat([normal,normal_nomask,damage,damage_nomask])
print(dataDF.shape)
featureDF=dataDF.iloc[:,:-1]
scale=MinMaxScaler()
featureDF=scale.fit_transform(featureDF.values)
targetSR=dataDF.iloc[:,-1]
#=======================================================
# test=pd.read_csv('./DATA/test_damage.csv')
#=======================================================
test=scale.transform(test.values)
x_train,x_test,y_train,y_test=train_test_split(featureDF,targetSR.values,stratify=targetSR)
model=QuadraticDiscriminantAnalysis(reg_param=0.001)
model.fit(x_train,y_train)
a=model.predict(test)
label="정상" if a[0]==0 else "파손"
print(label)
