def number_needed(a, b):
    x=[]
    y=[]
    z=[]
    x=list(a)
    y=list(b)


    for i in x :
        if i in y : continue
        else : 
            z.append(i)
    count=len(z)
    for i in z :
        x.remove(i)
    print z,x,'z,x'
    z=[]
    print count,'count1'

    for i in y :
        if i in x : continue
        else : 
            z.append(i)
    count=count+len(z)
    for i in z :
        y.remove(i)
    print z,y,'z,y'
    print count,'count2'
    d={}   
    for i in x :
        if i in d : d[i]=d[i]+1
        else : d[i]=1
    print d,'dir1'
    m={}
    for i in y :
        if i in m : m[i]=m[i]+1
        else : m[i]=1
    print m,'dir2'
    print x,y

    for i in d :
		if d[i]>=m[i] :
			count=count+(d[i]-m[i])
		else :
			count=count+(m[i]-d[i])
    return count,'finalcount'

a = raw_input().strip()
b = raw_input().strip()
print number_needed(a, b)
