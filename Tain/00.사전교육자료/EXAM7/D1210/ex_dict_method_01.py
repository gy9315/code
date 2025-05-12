# dict 자료형 전용 함수 즉, method
# [1] dict에서 key만 추출하는 method: keys()
colordict={'red':'#FF0000','green':'#00FF00', 'blue':'#0000FF'}
# key만 추출-> dict_keys type
keys=colordict.keys()
print(keys)
# [2] dict에서 values만 추출하는 method: values()
values=colordict.values()
print(values)
# [3] dict에서 key와 values을 tuple형태로 추출하는 method: items()
items=colordict.items()
items=list(items)
items=list(items[0])
items.reverse()
print(items)