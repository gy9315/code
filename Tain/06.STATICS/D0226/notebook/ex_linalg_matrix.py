import numpy as np
# choose method사용
# 행단위로 가져오는데 
# tuple형태는 열단위로 가져옴
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.linalg.det(x))
a=1*np.linalg.det(x[1:,1:])
b=2*np.linalg.det(x[1:,::2])
c=3*np.linalg.det(x[1:,:2])
print(a-b+c)
print(np.linalg.inv(x))