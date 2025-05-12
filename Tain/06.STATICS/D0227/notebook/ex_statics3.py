import numpy as np
import matplotlib.pyplot as plt
from scipy import stats,integrate
from scipy.optimize import minimize_scalar
linestyle=['-','--',':']
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
    
def ploy_prob(X,x_min,y_min):
    x_range,f=X
    def F(x):
        return integrate.quad(f,-np.inf,x)[0]
    xs=np.linspace(x_min,y_min,100)
    plt.figure(figsize=(10,5))
    plt.plot(xs,[f(y) for y in xs],label='f(x)')
    plt.plot(xs,[F(y) for y in xs],label='F(x)')
    plt.show()
    
rv=stats.norm(2,0.5)
print(rv.pdf(2))

a=np.linspace(0,4,100)
plt.plot(a,[rv.pdf(x) for x in a])
plt.show()

a=[1,2,3,4,5,6]
b=[1,1,1,4,1,1]
c=([[x+y for x in a] for y in b])
print(c)