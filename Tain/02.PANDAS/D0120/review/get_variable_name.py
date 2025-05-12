x=[1,2,3,4]
y=[5,6,7,8]
name = [1, 2, 3, 4]  # 변수 정의

def get_varible(x):
    for a,b in globals().items():
        print(a,b)
        if b == x:
            return a
    return None
print(get_varible(x))


