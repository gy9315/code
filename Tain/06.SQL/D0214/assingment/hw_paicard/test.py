a=[1,2,3,4,5]
a.pop(3)
print(a)
a.insert(3,0)
print(a)
a=[1,0,1,0]
for x in range(a.count(0)):
    a.remove(0)
print(a)
a=[]
for x in a:
    print(x)