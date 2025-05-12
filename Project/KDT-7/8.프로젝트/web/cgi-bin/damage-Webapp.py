import cgi, os.path
import joblib, sys, codecs
import cgitb; cgitb.enable()
import cv2
import numpy as np
import pandas as pd
from pydoc import html
from skimage.feature import hog
from sklearn.preprocessing import MinMaxScaler
import time

# ----------------------
# Output encoding for web
# ----------------------
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# ----------------------
# Pre-trained model load
# ----------------------
model_path = r'C:\Users\gy931\OneDrive\Desktop\KDT-7\8.프로젝트(7조)\web\cgi-bin\damage.pkl'
model = joblib.load(model_path)

# ----------------------
# Utility Functions
# ----------------------
def split_video(video):
    import cv2
    camera=cv2.VideoCapture(video)
    time.sleep(0.1)
    count=0
    _,img=camera.read()
    new_list=[]
    while True:
        ret,img=camera.read()
        if ret:
            new=img[320:320+385,409:409+284]
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
    return DF

# ----------------------
# Show upload form
# ----------------------
def show_form(msg=""):
    print("Content-Type: text/html; charset=utf-8")
    print("""
    <html><body>
    <h1>컵 손상 여부 예측</h1>
    <form enctype='multipart/form-data' method='POST'>
    <p>동영상 업로드: <input type='file' name='video'></p>
    <p><input type='submit' value='판정'></p>
    <p>{}</p>
    </form>
    </body></html>
    """.format(html.escape(msg)))

# ----------------------
# Main logic
# ----------------------
form = cgi.FieldStorage()
if 'video' not in form:
    show_form()
else:
    fileitem = form['video']
    if not fileitem.file:
        show_form("파일 업로드 실패")
    else:
        # 동영상 파일 저장
        filepath = os.path.join(os.path.dirname(__file__), "uploaded_video.mp4")
        with open(filepath, 'wb') as f:
            f.write(fileitem.file.read())

        # 영상 분석 및 예측
        # cap = cv2.VideoCapture(filepath)
        new_list=split_video(filepath)
        # count = 0
        # new_list = []
        # while True:
        #     ret, frame = cap.read()
        #     if not ret: break
        #     if count % 30 == 0 and len(new_list) < 13:
        #         new_list.append(frame)
        #     count += 1
        # cap.release()

        processed = contour_Canny(new_list)
        hog_df = trans_HOG(processed)
        print("new_list 개수:", len(new_list))              # → 13개 이상 나와야 함
        print("HOG shape:", hog_df.shape)                  # → (1, 13) 나와야 함
        print("HOG DF:", hog_df.head())    
        prediction = model.predict(hog_df)[0]
        label = "정상" if prediction == 0 else "파손"

        show_form(f"판정 결과: {label}")
