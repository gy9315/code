import numpy as np
import matplotlib.pyplot as plt
# a=np.random.choice(range(10),3,replace=False)
# print(a)
# a=np.random.normal(70,5,400)
# print(a.mean())
# plt.figure(figsize=(10,6))
# plt.hist(a,bins=10,range=(0,100),density=True)
# plt.xlim(50,100)
# # plt.show()
# b=[np.random.choice(a,20).mean() for x in range(10000)]
# b=np.array(b)
# plt.figure(figsize=(10,6))
# plt.hist(b,bins=100,range=(0,100),density=True)
# plt.xlim(50,100)
# plt.axvline(a.mean(),color='k')
# # print(b.mean())
# plt.show()
xs=np.arange(2,13)
ys=np.arange(1,7)
set_y=ys/21
prob=[(((ys[((x-ys)>=1) & ((x-ys)<=6)]).sum())) for x in xs]
# print((prob))
prob=[]
for x in xs:
    prob_o=[]
    for y in ys:
        if x-y>=1 and x-y<=6:
            prob_o.append(y*(x-y)/442)
    prob.append(sum(prob_o))
print(sum(prob))
# 더하기 조합확률
# 1/21,2/21,3/21,4/21,5/21,6/21
# XY x/21/x-y/21
# prob=[ys[((x-ys)>=1) & ((x-ys)<=6)] for x,a in zip(xs,set_y)]
# print(prob)
# a=[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
# print(sum(a))
# # 1/21, 2/21*3/21. 3/21*6/21, 4/21
# for x in set_x:
#     for y in set_y:
#         if x-y>=0:
#             print(y)
#         print('='*8)