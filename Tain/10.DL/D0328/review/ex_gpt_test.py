import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader
import time
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

# 1. 데이터 로딩
DF = pd.read_csv('../DATA/fashion-mnist_train.csv')
x = DF.iloc[:, 1:].values.astype(np.float32) / 255.0  # 정규화
y = DF['label'].values.astype(np.int64)

x_train, _, y_train, _ = train_test_split(x, y, test_size=0.2, stratify=y)

x_train_tensor = torch.tensor(x_train)
y_train_tensor = torch.tensor(y_train)

train_data = TensorDataset(x_train_tensor, y_train_tensor)
train_loader = DataLoader(train_data, batch_size=512, shuffle=True)

# 2. 모델 정의
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 1024)
        self.fc2 = nn.Linear(1024, 512)
        self.fc3 = nn.Linear(512, 256)
        self.fc4 = nn.Linear(256, 10)
        self.dropout = nn.Dropout(0.3)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = F.relu(self.fc3(x))
        x = self.dropout(x)
        return self.fc4(x)

# 3. 학습 함수
def train(device):
    model = MLP().to(device)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    criterion = nn.CrossEntropyLoss()

    model.train()
    start = time.time()

    for epoch in range(30):
        total_loss = 0
        correct = 0
        total = 0
        for x_batch, y_batch in train_loader:
            x_batch, y_batch = x_batch.to(device), y_batch.to(device)

            optimizer.zero_grad()
            outputs = model(x_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            pred = torch.argmax(outputs, dim=1)
            correct += (pred == y_batch).sum().item()
            total += y_batch.size(0)

        acc = correct / total * 100
        print(f"[{device}] Epoch {epoch+1}: Loss={total_loss:.4f}, Acc={acc:.2f}%")

    elapsed = time.time() - start
    print(f"🕒 Total time on {device}: {elapsed:.2f} seconds\n")
    return elapsed

# 4. CPU & GPU 실험
cpu_time = train(torch.device('cpu'))

if torch.cuda.is_available():
    gpu_time = train(torch.device('cuda'))
else:
    print("⚠️ CUDA is not available. Run only on CPU.")