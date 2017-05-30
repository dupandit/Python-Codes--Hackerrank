class Stack():
  
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        return self.items.append(item)
  
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

def is_matched(expression):
    s=Stack()
    for i in expression :
        if i == '(' or i == '{' or i == '[' :
            s.push(i)
        else :
            if i == ')' :
                if s.isEmpty() == True :
                    return False
                else :
                    x=s.pop()
                    #print x,i
                    if x == '(':
                        pass
                    else :
                        return False
            
            elif i == '}' :
                if s.isEmpty() == True :
                    return False
                else :
                    x=s.pop()
                    #print x,i
                    if x == '{':
                        pass
                    else :
                        return False
            
            elif i == ']' :
                if s.isEmpty() == True :
                    return False
                else :
                    x=s.pop()
                    #print x,i
                    if x == '[':
                        pass
                    else :
                        return False
    return s.isEmpty() 

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
