# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, K):
    # write your code in Python 2.7
    #print 'string=',S
    #print 'Key=',K
    s=[]
    s=S.split('-')
    #print s
    temp=''
    for i in s :
        temp=temp+i
    s=temp
    #print s
    stri=''.join(s)
    
    temp_list=[]
    count =1
    for i in reversed(stri) :
        if count==K+1:
            temp_list.append('-')
            count=0            
        else :
            temp_list.append(i)
        count=count+1
    temp=[]
    temp=temp_list[::-1]
	
    #print temp_list
    S=''.join(temp)
    return S