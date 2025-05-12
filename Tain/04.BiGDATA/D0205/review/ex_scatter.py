import matplotlib.pyplot as plt
x=[10,20,30,40,50]
y=[1,2,3,4,5]
size=[]
for a in y:
    size.append(a*50)
plt.scatter(x,y,s=size,c=range(5),cmap='jet')
plt.colorbar()
plt.show()