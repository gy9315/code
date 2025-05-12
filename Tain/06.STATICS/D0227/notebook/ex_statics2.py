import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

y_range=np.array([3,5])
def g(y):
    if y_range[0] <=y<=y_range[1]:
        return (y-3)/2
    else:
        return 0
def G(y):
    return integrate.quad(g,-np.inf,y)[0]

ys=np.linspace(y_range[0],y_range[1],100)
plt.figure(figsize=(10,5))
plt.plot(ys,[g(y) for y in ys],label='g(y)')
plt.plot(ys,[G(y) for y in ys],label='G(y)')
plt.show()