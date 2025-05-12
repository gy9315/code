import torch
import torch.nn as nn
import torch.functional as F
x_train=torch.randn(2,3)
y_train=torch.randint(1,5,(2,1))
# print(x_train.shape);print(y_train.shape)

# 선형 결함층(Full connected layer: FC)
layer=nn.Linear(3,1) # 입력 feature 수, target 수, perceptron 수
output=layer(x_train)
# print(layer.weight)
nn.init.xavier_uniform_(layer.weight)
for x in layer.parameters():
    print(x)
# print(layer.weight)
# print(layer.bias)