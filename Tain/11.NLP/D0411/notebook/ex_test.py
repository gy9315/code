import re
import torchtext
with open('../DATA/fra-eng/fra.txt',encoding='utf-8') as f:
    string=f.readlines()
print(string[:10])
data=[]
for x in string[:10]:
    compile=re.compile(r'^(.*?)(?=CC-BY)')
    a=re.match(compile,x)
    data.append(a.group().split('\t')[:2])
print(data)
data_list=[]
for x,y in data:
    print(x,y)
    a=re.sub(r'\u202f','',y)
    x=x.replace(' ','')
    y=a.replace(' ','')
    data_list.append([x,y])
print(data_list)
