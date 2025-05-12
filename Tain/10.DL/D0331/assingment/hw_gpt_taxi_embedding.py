import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader

# 1. Load & Preprocess
df = pd.read_csv('../DATA/taxis.csv')
df = df.dropna(subset=["pickup_zone", "dropoff_zone", "pickup", "dropoff", "distance"])
df = df[df["distance"] > 0].reset_index(drop=True)

df["pickup"] = pd.to_datetime(df["pickup"])
df["pickup_hour"] = df["pickup"].dt.hour
df["pickup_sin"] = np.sin(2 * np.pi * df["pickup_hour"] / 24)
df["pickup_cos"] = np.cos(2 * np.pi * df["pickup_hour"] / 24)

df["route"] = df["pickup_zone"] + "_" + df["dropoff_zone"]
df["is_cross_zone"] = (df["pickup_borough"] != df["dropoff_borough"]).astype(int)

route_le = LabelEncoder()
df["route_id"] = route_le.fit_transform(df["route"])

mean_distance = df.groupby(["pickup_zone", "dropoff_zone"])["distance"].mean().reset_index()
mean_distance.rename(columns={"distance": "distance_mean"}, inplace=True)
df = df.merge(mean_distance, on=["pickup_zone", "dropoff_zone"], how="left")

# Features & Target
feature_cols = ["pickup_sin", "pickup_cos", "distance_mean", "is_cross_zone"]
target_col = "distance"

scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_feat = scaler_X.fit_transform(df[feature_cols])
y = scaler_y.fit_transform(df[[target_col]])
route_ids = df["route_id"].values

# 2. Train/Test Split
X_train, X_test, route_train, route_test, y_train, y_test = train_test_split(
    X_feat, route_ids, y, test_size=0.2, random_state=42
)

# 3. PyTorch Dataset
class RouteDataset(Dataset):
    def __init__(self, route_ids, other_features, targets):
        self.route_ids = torch.tensor(route_ids, dtype=torch.long)
        self.other_features = torch.tensor(other_features, dtype=torch.float32)
        self.targets = torch.tensor(targets, dtype=torch.float32)

    def __len__(self):
        return len(self.targets)

    def __getitem__(self, idx):
        return self.route_ids[idx], self.other_features[idx], self.targets[idx]

train_dataset = RouteDataset(route_train, X_train, y_train)
test_dataset = RouteDataset(route_test, X_test, y_test)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64)

# 4. 모델 구성
class RouteEmbeddingModel(nn.Module):
    def __init__(self, num_routes, emb_dim=16):
        super().__init__()
        self.route_emb = nn.Embedding(num_routes, emb_dim)
        self.mlp = nn.Sequential(
            nn.Linear(emb_dim + 4, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )

    def forward(self, route_id, other_feat):
        r = self.route_emb(route_id)
        x = torch.cat([r, other_feat], dim=1)
        return self.mlp(x)

# 5. 학습
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = RouteEmbeddingModel(num_routes=df["route_id"].nunique()).to(device)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)

for epoch in range(50):
    model.train()
    total_loss = 0
    for route_id, features, labels in train_loader:
        route_id, features, labels = route_id.to(device), features.to(device), labels.to(device)

        optimizer.zero_grad()
        output = model(route_id, features)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"[Epoch {epoch+1}] Loss: {total_loss:.4f}")

# 6. 평가 (R²)
model.eval()
y_pred = []
y_true = []

with torch.no_grad():
    for route_id, features, labels in test_loader:
        route_id, features = route_id.to(device), features.to(device)
        output = model(route_id, features)
        y_pred.extend(output.cpu().numpy().flatten())
        y_true.extend(labels.numpy().flatten())

# 역정규화 후 R² 계산
y_pred_inv = scaler_y.inverse_transform(np.array(y_pred).reshape(-1, 1)).flatten()
y_true_inv = scaler_y.inverse_transform(np.array(y_true).reshape(-1, 1)).flatten()
r2 = r2_score(y_true_inv, y_pred_inv)

print(f"\n✅ R² Score on Test Set: {r2:.4f}")
