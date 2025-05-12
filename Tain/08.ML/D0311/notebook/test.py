import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
np.random.seed(100)
a=np.random.randint(1,100,30)
c=np.random.randint(1,100,30)
lof=LocalOutlierFactor(n_neighbors=2,contamination=0.2)
outlier=lof.fit_predict(a.reshape(-1,1))
# a=a[outlier==1]
# c=c[outlier==1]
# a=(a-a.mean())/a.std()
# c=(c-c.mean())/c.std()
print((a-a.mean()).mean())
print(c.mean())
plt.plot(a,c,'ro')
plt.show()