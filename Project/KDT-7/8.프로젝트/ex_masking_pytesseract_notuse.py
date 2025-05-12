import cv2
import pytesseract
from pytesseract import Output
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def mask_text_areas(image_path, save_path=None, min_conf=5):
    # 이미지 불러오기
    img = cv2.imread(image_path)
    b,g,r=cv2.split(img)
    clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(16,16))
    enhanced = clahe.apply(g)
    gray = cv2.Canny(enhanced,150, 200)

    # OCR로 텍스트 정보 얻기
    d = pytesseract.image_to_data(gray, output_type=Output.DICT)

    for i in range(len(d['text'])):
        text = d['text'][i].strip()
        conf = d['conf'][i]

        try:
            if float(conf) > min_conf and text != '':
                print(d['text'])
                x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
                # 검정 박스로 덮기
                cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 0), -1)
        except ValueError:
            continue  # conf 값이 이상할 때 대비

    # 저장
    if save_path:
        cv2.imwrite(save_path, gray)
    return img

# 예시 실행
masked_img = mask_text_areas(
    image_path='./DATA/damage_cup/102.jpg',
    save_path='111_masked.jpg',
    min_conf=60  # 신뢰도 기준
)
