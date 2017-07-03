def Bubble_Sort(arr):
    l=len(arr)
    for i in range(l):
        index=0
        for i in range(l-1):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    return arr





arr=[]
while True :
    x=raw_input('Enter number and type done at the end\n')
    if x == 'done':
        break
    else :
        arr.append(int(x))
print arr,Bubble_Sort(arr)