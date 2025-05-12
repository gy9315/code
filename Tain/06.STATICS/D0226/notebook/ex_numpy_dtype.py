import numpy as np
print(np.str_)
a=np.array([['b','a'],['c','d']],dtype='S')
print(a)
b=np.array(b'abc')
print(b)
# 바이트 수에 따라 수정되는 값이 다르다
x=np.array(range(10),dtype='S2').reshape(2,5)
print(x)
x[0,0]='Hello'
print(x)
y=np.poly1d(np.array([1,2]))
x=range(0,10)
print(x)
yn=y(x)
print(yn)