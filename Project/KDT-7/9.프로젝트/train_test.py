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
preprocess=transforms.Compose([transforms.Grayscale(),transforms.Resize((100,100)),transforms.transforms.ToTensor()])
imgDS=ImageFolder(root='./kia_images',transform=preprocess)
