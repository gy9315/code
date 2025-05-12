# def solution(arr, n):
#     return list(map(lambda x:x+n if not arr.index(x)%2 else x, arr)) if len(arr)%2 else list(map(lambda x: x+n if arr.index(x)%2 else x, arr))
# print(solution([49, 12, 100, 276, 33],27))

def solution(arr):
    list1=[]
    for x in arr:
        list1.append(len(x))
    if max(list1) > len(arr):
        arr.extend([[0]*max(list1)]*(max(list1)-len(arr)))
    else:
        for x in arr:
            x.append(0*(len(arr)-max(list1)))
    return arr
print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))