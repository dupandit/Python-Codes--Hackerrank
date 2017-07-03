
#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    
    def addTwoNumbers(self, l1, l2):
        list1=[]
        global list1
        list2=[]
        global list2
        
        def MakeList(l,inp):
            if inp==1:
                global list1
                list1.append(l.val)
                if l.next!=None:
                    MakeList(l.next,1)
                    
            if inp==2: 
                global list2
                list2.append(l.val)
                if l.next!=None:
                    MakeList(l.next,2)

                   
        MakeList(l1,1)
        MakeList(l2,2)

        list1=list1[::-1]
        list2=list2[::-1]
        
        #print list1
        #print list2
        
        temp1=''
        temp2=''
        for i in list1 : 
            temp1=temp1+str(i)
        for i in list2 : 
            temp2=temp2+str(i)
            
        
        t1=int(temp1)
        t2=int(temp2)
        t=t1+t2
        #print t
        global result_list
        result_list=[]
        for i in str(t):
            result_list.append(i)
        result_list=result_list[::-1]
        
        #print result_list
        
        def Make_chain(l,k):
            global result_list
            #print result_list
            if k<len(result_list)-1:
                l.next=ListNode(result_list[k+1])
            else :
                l.next=None
            return l.next

                
         
        l3=ListNode(result_list[0])
        Make_chain(l3,0)

            
            
        for i in range(len(result_list)):
            if i==0:
                temp=Make_chain(l3,i)
            else :
                temp=Make_chain(temp,i)
                
        return l3