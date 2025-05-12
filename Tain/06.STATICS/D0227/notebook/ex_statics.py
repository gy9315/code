import numpy as np
import matplotlib.pyplot as plt
a=np.random.choice(range(10),3,replace=False)
print(a)
a=np.random.normal(70,5,400)
print(a.mean())
# plt.figure(figsize=(10,6))
# plt.hist(a,bins=10,range=(0,100),density=True)
plt.xlim(50,100)
# plt.show()
b=[np.random.choice(a,20).mean() for x in range(10000)]
b=np.array(b)
plt.figure(figsize=(10,6))
plt.hist(b,bins=100,range=(0,100),density=True)
plt.xlim(50,100)
plt.axvline(a.mean(),color='k')
# print(b.mean())
plt.show()