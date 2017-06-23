#!/bin/python

import sys
import string


def MakeWeight() : # Make dictionary to store weight alphabet relation
    t=0
    d={}
    alp=string.ascii_lowercase
    for i in alp : 
        t=t+1
        d[i]=t
    return d
    
def MakeUniformSubstr(s) : # Make a list containing all uniform substrings of string s
    # initialization
    subst=[] # stores all uniform substring
    
    y='' # temporary string inorder to find uniformity of substring and finally add y to the list. Then make it empty and continue the same
    
    temp='' # This temporary string is used to check whether previous character is same as this. If yes we join this new same character to previously formed uniform substring with this character
    
    count=0  # Counter only used to do some operation for 1st characters
    
    l=len(s)    # these two variables are used to deal with last character
    c=0
    for i in s :
        c=c+1
        if c==l :    # If it is last character : 1) check if i == temp, which is previous character. If same append them and add to list. If not, append the previous formed substring to list and then lastly append this remaining last character to the list
            
            if i==temp : 
                y=y+i
                if y not in subst :
                    subst.append(y)
            else : 
                if y not in subst :
                    subst.append(y)
                if i not in subst :
                    subst.append(i)
        else : 
            if count == 0 : 
                y=y+i
                temp=i
                count=count+1
            else : 
                if i==temp :
                    y=y+i
                    if y not in subst :
                        subst.append(y)
                    temp=i
                else : 
                    if i not in subst :
                        subst.append(i)
                    if y not in subst :
                        subst.append(y)
                    y=''+i
                    temp=i
    #print subst
    return subst

def CalculateWeights(li,d) :
    finalweights={}
    for subst in li :
        wt=0
        for i in subst : 
            wt=wt+d[i]
        finalweights[subst]=wt
    return finalweights
        
    
    
s = raw_input().strip()
d=MakeWeight()
li=MakeUniformSubstr(s)
finalsw=CalculateWeights(li,d) # Pass both substring and weight-alphabet dict to this function which will return dictionary calculating weights of individual substrings in that list

weights=[]
for i in finalsw : 
    weights.append(finalsw[i])  # we gather all weights in one string
n = int(raw_input().strip())
#print weights
for a0 in xrange(n):
    x = int(raw_input().strip())
    if x in weights : 
        print 'Yes'
    else : 
        print 'No'
    
