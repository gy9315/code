import cv2
import os
filename=os.listdir('./DATA/normal_cup/')
while True:
    for x in filename:
        path='./DATA/normal_cup/'+x
        img = cv2.imread(path)
        b,g,r=cv2.split(img)
        clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(16,16))
        enhanced = clahe.apply(g)
        edges = cv2.Canny(enhanced,150, 200)
        # roi=cv2.selectROI('img',edges,None,None)
        # print(roi)
        cv2.imshow('Edges',edges[130:291,15:175])
        key=cv2.waitKey(100)
        if key==27:
            cv2.destroyAllWindows()
            break
    if key==27:
        break
