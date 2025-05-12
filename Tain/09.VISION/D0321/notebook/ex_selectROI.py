import cv2
import numpy
img=cv2.imread('../DATA/img/gray.png')
x,y,w,h=cv2.selectROI('gray',img,False)
print(x,y,w,h)
cv2.imshow('gray',img)
a=cv2.waitKey()
if a==32:
    cv2.destroyWindow('gray')
slicing=img[y:y+h,x:x+w]
cv2.imshow('new',slicing)
cv2.waitKey()
cv2.destroyAllWindows()
