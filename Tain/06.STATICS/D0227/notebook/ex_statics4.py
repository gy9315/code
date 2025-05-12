import numpy as np
import matplotlib.pyplot as plt
from scipy import stats,integrate
from scipy.optimize import minimize_scalar
linestyle=['-','--',':']
plt.figure(figsize=(10,5))
xs=np.linspace(-5,5,100)
a=[(0,1),(0,2),(1,1)]
for x,y in zip(a,linestyle):
    rv=stats.norm(x[0],x[1])
    plt.plot(xs,rv.pdf(xs),label=f'N({x[0]},{x[1]**2}')
plt.legend()
plt.show()