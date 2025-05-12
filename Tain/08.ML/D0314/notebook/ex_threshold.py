from sklearn.preprocessing import Binarizer
from sklearn.linear_model import LogisticRegression
import numpy as np
x=[[1,-1,2],[2,0,0],[0,1.1,1.2]]
b=Binarizer(threshold=1.1)
print(b.fit_transform(x))
