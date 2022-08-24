def Quick_Sort(a,low,high):
    if low<high:
        loc=paration(a,low,high)
        Quick_Sort(a,low,loc-1)
        Quick_Sort(a,loc+1,high)
def paration(a,low,high):
    i=low
    j=high
    pivot=a[i]
    while i<j:
        while a[i]<=pivot and i<j:
            i=i+1
        while a[j]>pivot:
            j=j-1
        if i<j:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        temp=a[low]
        a[low]=a[j]
        a[j]=temp
        return j

a=[30,10,20,40,50]
Quick_Sort(a,0,len(a)-1)
print(a)
