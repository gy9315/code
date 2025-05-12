import numpy as np
from sklearn.model_selection import KFold
# [교차검증 K-Fold]
# 데이터부족에 따른 과대적합/과소적합 해결 위한 방법
# 단점: 학습에 시간이 오래 걸림
X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
y = np.array([1, 2, 3, 4])
kf = KFold(n_splits=4)
kf.get_n_splits(X)
print(kf)
for i, (train_index, test_index) in enumerate(kf.split(X)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")