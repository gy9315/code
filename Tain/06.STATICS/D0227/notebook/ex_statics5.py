import numpy as np
import matplotlib.pyplot as plt
from scipy import stats,integrate
from scipy.optimize import minimize_scalar
def Ex(lam):
    x_range=[0,np.inf]
    def f(x):
        if x>0:
            return lam*np.exp(-lam*x)
        else:
            return 0
    return x_range,f
def E(X,g=lambda x:x):
    x_range,f=X
    def integrand(x):
        return g(x) * f(x)
    return integrate.quad(integrand,-np.inf,np.inf)[0]

def V(X,g=lambda x:x):
    x_range,f=X
    mean=E(X,g)
    def integrand(x):
        return (g(x)-mean)**2*f(x)
    return integrate.quad(integrand,-np.inf,np.inf)[0]
y_range=np.array([3,5])

def check_prob(X):
    x_range,f=X
    f_min=minimize_scalar(f).fun
    assert f_min>=0,'density function is minus value'
    prob_sum=np.round(integrate.quad(f,-np.inf,np.inf)[0],6)
    assert prob_sum==1,f'sum of probablity is {prob_sum}'
    print(f'expected value{E(X):3f}')
    print(f'variance{V(X):3f}')
    
lam=3
X=Ex(lam)
print(check_prob(X))

plt.figure(figsize=(10,5))
xs=np.linspace(0,3,100)
for lam in (1,2,3):
    rv=stats.expon(scale=1/lam)
    plt.plot(xs,rv.pdf(xs))
plt.show()