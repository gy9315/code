# 29.1
def hello():
    print('Hello, woerd')

hello()
# 29-2
def add(a,b):
    '''이 함수는 ~~'''
    print(a+b)
add(10,20)
print(add.__doc__)
# 29-3
def add(a,b):
    return a+b
print(add(1,40))
# 29-4
def add_sub(a,b):
    return [a+b,a-b]

print(add_sub(50,20))
x=add_sub(50,20)
x.append(30)
print(x)
a,b,c=x
print(a)

# 29-5
def mul(a,b):
    return a*b
def add(a,b):
    print(a+b)
    print(mul(a,b))

add(9,4)
    

# 29-7
def qu(a,b):
    print(f'몫: {a//b} 나머지: {a%b}')
    return a,b
x=qu(10,3)
print(len(x))
# 29-8
def calc(a,b):
    if not b==0: 
        return [a+b,a-b,a*b,a/b] 
    else: return [a+b,a-b,a*b,'계산불가']
x=calc(10,20)
print(f'덧셈: {x[0]} 빼기: {x[1]}, 곱셈: {x[2]}, 나눗셈: {x[3]}')
# 30
print(*[1,2,3])
print([1,2,3])