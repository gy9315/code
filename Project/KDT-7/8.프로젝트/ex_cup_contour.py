import cv2
import os
filename=os.listdir('./DATA/test/')
for name in filename:
    img=cv2.imread(f'./DATA/test/'+name,cv2.IMREAD_GRAYSCALE)
    clahe=cv2.createCLAHE(clipLimit=3,tileGridSize=(16,16))
    img=clahe.apply(img)
    img=cv2.Canny(img,120,250)
    a,b=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # x=cv2.selectROI('a',img,None,None)
    # print(x)
    list1=[]
    for idx,con in enumerate(a):
        # print(con)
        area=cv2.contourArea(con)
        list1.append(area)
        if area<1:
            continue
        x,y,w,h=cv2.boundingRect(con)
        extent = area / (w * h)
        if 35<x<180 and 150<y<265  and extent>0.02:pass
            # print(extent)
            # print(con)
            # img1=cv2.rectangle(img,(x,y),(x+w,y+h),(0,),-1)
            # cv2.drawContours(img,a,idx,(0,),thickness=cv2.FILLED)
            # cv2.imshow('img',img)
            # cv2.waitKey()
    cv2.imwrite("./DATA/test/"+name.split('.')[0]+'.jpg',img)
            
    # list1.sort(reverse=True)
    # print(list1)