import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터프레임 생성
data = {'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'y': [1, 3, 2, 5, 7, 6, 8, 9, 7, 10, 11]}
df = pd.DataFrame(data)

# 이동 평균 계산 (윈도우 크기 3)
df['moving_average'] = df['y'].rolling(window=3, min_periods=1).mean()

# 원래 데이터와 이동 평균 추세선 그리기
plt.plot(df['x'], df['y'], label='Original Data')
plt.plot(df['x'], df['moving_average'], linestyle='--', color='r', label='Moving Average')

# 범례 추가
plt.legend()

# 그래프 보여주기
plt.show()

