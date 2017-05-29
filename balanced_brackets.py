def is_matched(expression):
    express=[]
    express=list(expression)
    s=True
    l=len(express)
    print 'l=',l,'expression=',expression,'s=',s
    j=0
    if l==0 :
        return s
    count=0
    for i in range(l) :
        if i==l-1 :
            for k in range(l/2):
                if (express[k]== '[' and express[j-1-k]==']') or (express[k]== '(' and express[j-1-k]==')') or (express[k]== '{' and express[j-1-k]=='}')  :
                    count=count+1 
                else : continue
            print 'count=',count,'s=',s
            if count == l/2 :
                return True
            else :
                return False

        else :
            if (express[i] == ']' or express[i]== '}' or express[i]==')') and (express[i+1]=='(' or express[i+1]=='{' or express[i+1]=='[') :
                j=i+1
                for k in range(j/2):
                    if (express[k]== '[' and express[j-1-k]==']') or (express[k]== '(' and express[j-1-k]==')') or (express[k]== '{' and express[j-1-k]=='}')  :
                        count=count+1 
                    else : continue
                print 'count=',count,'s=',s

                if count == j/2 :
                    s=s and True
                else :
                    s=s and False
                is_matched(expression[j:l])
                
  
                
  

    
    
    
 

        
t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
