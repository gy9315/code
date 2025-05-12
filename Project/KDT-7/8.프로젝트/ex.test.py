import cv2
import numpy as np
img=cv2.imread('./DATA/KakaoTalk_20250324_140515498.jpg',cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img,(500,500))
img1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,C=3)
# cv2.imshow('a',img1)
# cv2.waitKey()
# cv2.destroyAllWindows()
# new=cv2.selectROI('a',img1,False)
# print(new)
new=img1[255:255+67,109:109+63]
fill=np.full_like(new,245,dtype='uint8')
print(fill.shape)
for x in range(1000):
    a=np.random.randint(0,67)
    b=np.random.randint(0,63)
    fill[a,b]=20
img1[255:255+67,109:109+63]=fill
print(img.shape)

for x in range(0,360,10):
    rm=cv2.getRotationMatrix2D((250,250),x,1)
    a=cv2.warpAffine(img1,rm,(500,500))
    cv2.imshow('new',a)
    cv2.waitKey()
    cv2.destroyAllWindows()   
# # new=cv2.resize(new,(400,400))
# cv2.imshow('new',img1)

# cv2.waitKey()
# cv2.destroyAllWindows()

# img1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,C=3)

