def ransom_note(magazine, ransom):

    x=[]
    y=[]
    x=list(magazine)
    y=list(ransom)
    count = 0
    d={}
    l=len(y)
    for i in x :
        if i in d :
            d[i]=d[i]+1
        else :
            d[i]=1
    for i in y :
        if i in d :
            count=count+1
            d[i]=d[i]-1
            if d[i]==0 :
                del d[i]
    if count == l :
        return 'Yes'
    else :
        return 'No'

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
print answer
#if(answer):
 #   print "Yes"
#else:
 #   print "No"
