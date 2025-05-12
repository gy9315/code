str='123456789'
str_num=''
if len(str)>5 and not len(str)%3:
    for data in range(1,int(len(str)/3)+1):
        str_num=str_num+','+str[-(3*data):]
    if len(str)%3==1:        
        str_num=str[0]+str_num
    else:str_num=str[:len(str)%3-1]+str_num
elif len(str)//3==1:
    for data in [len(str)//3]:
        str_num=str_num+','+str[-(3*data):]
    if len(str)%3==1:        
        str_num=str[0]+str_num
    else:str_num=str[:len(str)%3-1]+str_num
    
elif len(str)>3 and len(str)%3:
    for data in range(int(len(str)/3)-1):
        str_num=str_num+','+str[-(3*data):]
    str_num=str[:len(str)%3-1]+str_num
else: str_num=str
print(str_num)
