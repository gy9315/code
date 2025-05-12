import matplotlib.pyplot as plt
import random as rd
import numpy as np
import pandas as pd
rd.seed(100)
list1=[rd.randrange(1,100) for x in range(10)]
list2=[rd.randrange(1,100) for x in range(10)]
DF=pd.DataFrame({'a':list1,'b':list2})
print(DF.corr())
a=np.polyfit(list1,list2,1)
print(a)
poly_1d=np.poly1d(a)
print(poly_1d)
xs=np.linspace(min(list1),max(list1))
ys=poly_1d(xs)
print(xs)
plt.plot(list1,list2,'o')
plt.plot(xs,ys,'-')
plt.show()
print(np.linspace(1,7,6,retstep=True))