import cv2
camera=cv2.VideoCapture('./DATA/damage(2).mp4')
count=0
_,img=camera.read()
idx=cv2.selectROI('a',img,None,None)
print(idx)
new=img[idx[1]:idx[1]+idx[3],idx[0]:idx[0]+idx[2]]
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
        if not count%30:pass
            # cv2.imwrite(f'./DATA/test/{count}.jpg',new)
        count+=1
    else: pass
