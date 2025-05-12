import torch
import torch.nn
import torch.nn.functional as F
from torchvision.datasets import ImageFolder
from torch.utils.data import Dataset,DataLoader
from torchvision.transforms import transforms
import matplotlib.pyplot as plt
from PIL import Image
from cat_dog_utils import *
preprocess=transforms.Compose([transforms.Resize((50,50)),transforms.ToTensor()])
imgDS=ImageFolder(root='../DATA/img',transform=preprocess)
print(imgDS.classes)
imgDL=DataLoader(imgDS)
# img,target=imgDL
a=[]
b=[]
for img,target in imgDL:
    a.append(img[0][1,:,:].tolist())
    b.append(target.item())
feature=torch.tensor(a,dtype=torch.float32)
target=torch.tensor(b,dtype=torch.int64)
print(target.unique())
CNN_train(feature,target)