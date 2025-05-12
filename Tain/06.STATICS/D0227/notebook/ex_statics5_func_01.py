import numpy as np
import matplotlib.pyplot as plt
from scipy import stats,integrate
from scipy.optimize import minimize_scalar
from collections import Counter
a=np.array([1,2,3,4,5,6,7,7,4,5,6,8])
pmf={x:y/len(a)for x,y in Counter(a).items()}
fig,axes=plt.subplots(1,2,figsize=(10,6))
print(pmf.get(1)+pmf.get(2))
kde=stats.gaussian_kde(a)
axes[0].plot(pmf.keys(),pmf.values())
print(kde)
x,y=integrate.quad(kde,1,3)
print(x)
xs=np.linspace(1,8,100)

axes[1]=plt.plot(xs,kde(xs))
xs=np.linspace(1,3,100)
axes[1]=plt.fill_between(xs,kde(xs))

plt.show()
