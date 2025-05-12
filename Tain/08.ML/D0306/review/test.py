def solution(my_string):
    list1=[0]*52
    compare=list(range(ord('A'), ord('Z')+1))+list(range(ord('a'), ord('z')+1))
    dict1={x:my_string.count(x)for x in list(set([x for x in my_string]))}
    for x in dict1:
        for a,b in enumerate(compare):
            if ord(x)==b:
                list1[a]=dict1[x]
    return list1

