def solution(my_string, queries):
    for x in queries:
        str=my_string[x[0]:x[1]+1]
        if x[0]!=0:
            my_string=my_string[:x[0]]+my_string[x[0]:].replace(str,str[-1::-1],1)
        else: 
            my_string=my_string.replace(str,str[-1::-1],1)    
    return my_string

'''
rm
remrgorpsam
remrgorp
progrmersam
mersa
prograsremm
sremm
programmers
programmers
'''
print(solution('rermgorpsam',[[2, 3], [0, 7], [5, 9], [6, 10]]))
