class MyQueue(object):

    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
        
    def peek(self):
        while True :

            if self.s1.isEmpty() :

                return self.s2.peek()

            else :

                self.s2.push(self.s1.pop()) 

    def pop(self):

        while True :

            if self.s1.isEmpty() :

                self.s2.pop()

                return
            
            else :

                self.s2.push(self.s1.pop())      
        
    def put(self, value):
        if self.s2.isEmpty() :
            self.s1.push(value)
        else :

            while True : 
                if self.s2.isEmpty() :
                    self.s1.push(value)
                    return
					
                else : 
                    self.s1.push(self.s2.pop())
                    

            

        
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

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
 
