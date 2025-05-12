import numpy as np
import matplotlib.pyplot as plt
from scipy import stats,integrate
from scipy.optimize import minimize_scalar
from collections import Counter
list=[1,2,3,4,5]
prob=[1/15,2/15,3/15,4/15,5/15]
a=np.random.choice(list,1000,p=prob)
plt.hist(a,bins=5,density=True,range=(1,7))
plt.show()
