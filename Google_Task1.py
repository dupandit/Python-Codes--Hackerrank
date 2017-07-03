# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    # write your code in Python 2.7
    # Initialization
    l=len(A)
    temp=[] 
    final_list=[] # stores subarrays of length K
    index=0  #
    
    # Task 1 is to make subarrays of length K and store it in another list
    while True : 
        m=index  
        
        for i in range(K) :
            temp.append(A[m])
            m=m+1
        final_list.append(temp)
        
        if m==l:
            break
        index=index+1
        temp=[]


        

    # Task 2 : Compare these subarrays in final_list
    list1=[]
    list2=[]
    while len(final_list)>1 : 
        
        list1=final_list[0]
        list2=final_list[1]
    
        for i in range(K) :
            if list1[i]==list2[i]:
                pass
            elif list1[i]>list2[i] :
                del final_list[1]
                break
            elif list2[i]>list1[i] :
                del final_list[0]
                break
    return final_list[0]
                