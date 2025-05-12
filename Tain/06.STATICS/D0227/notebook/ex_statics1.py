import numpy as np
import matplotlib.pyplot as plt
x_range=np.array([0,1])
def f(x):
    if x_range[0]<=x<=x_range[1]:
        return 2*x
    else:
        return 0
X=[x_range,f]
xs=np.linspace(x_range[0],x_range[1],100)
fig=plt.figure(figsize=(10,5))
plt.plot(xs,[f(x) for x in xs],label='f(x)',color='gray')
plt.hlines(0,-0.2,1.2, alpha=0.3)
plt.vlines(0,-0.2,1.2, alpha=0.3)
plt.vlines(xs.max(),0,2.2,linestyles='--',colors='gray')
xs=np.linspace(0.4,0.6,100)
plt.fill_between(xs,[f(x) for x in xs], label='prob')
plt.show()