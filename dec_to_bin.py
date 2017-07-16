global s
s=''
def convert_to_binary(num) :
    global s
    if num>0:
        t=num%2
        s=s+str(t)
        if num/2<=0 :
            return s
        else :
            return convert_to_binary(num/2)

    else :




x=328
m=convert_to_binary(x)
m=m[::-1]
print len(m)