import numpy as np
# choose method사용
# 행단위로 가져오는데 
# tuple형태는 열단위로 가져옴
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.choose(tuple([2,1,0]),x))
print(np.choose(1,x))
# item를 활용하여 검색
print(x.item(1))
print(x.item(1,2))
# take method
# item과 take은 단순 1열로 인덱스로 가져옴
print(x.take([3,4]))
print(x.take([[1,2],[2,1]]))
print(x.take((0,1,2)))
# where은 인덱스값을 들고 오는 것
print(x[np.where(x>4)])
# 그냥은 boolen 인덱스
print((x>4) & (x<7))
