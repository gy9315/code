import torch
import torch.nn
import torch.nn.functional as F
from torchvision.datasets import ImageFolder
from torch.utils.data import Dataset,DataLoader
from torchvision.transforms import transforms
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from utils import *
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
import numpy as np


imgDS=cat_canny_hog(test_data_convert('./KakaoTalk_20250404_134002401_01.jpg'))
x,a=model_test(imgDS,'./model.pkl')
model_dict={0: 'EV6',1: 'EV9',2: 'K3',3: 'K5',4: 'K7',5: 'K8',6: 'K9',7: '니로', 8: '레이', 9: '모닝', 10: '모하비', 11: '셀토스',
12: '스토닉',13: '스팅어', 14: '스포티지',15: '쏘렌토',16: '쏘울', 17: '카니발',18: '카렌스',19: '포르테', 20: '프라이드'}
for idx, prob in enumerate(a.squeeze(0).squeeze(0)):
    label = model_dict[idx]
    print(f"{label:10}: {prob:.2%}")
