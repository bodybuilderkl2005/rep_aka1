def Mergesort(a):
    if len(a)>1:
        mid=len(a)//2
        lefthalf=a[:mid]
        righthalf=a[mid:]
        Mergesort(lefthalf)
        Mergesort(righthalf)
        merge(a,lefthalf,righthalf)
def merge(a,lefthalf,righthalf):
    i=j=k=0
    while i<=len(lefthalf)-1 and j<=len(righthalf)-1:
        if lefthalf[i]<righthalf[j]:
            a[k]=lefthalf[i]
            i=i+1
            k=k+1
        else:
            a[k]=righthalf[j]
            j=j+1
            k=k+1
    if i>len(lefthalf)-1:
        while j<=len(righthalf)-1:
            a[k]=righthalf[j]
            j=j+1
            k=k+1
    else:
        while i<=len(lefthalf)-1:
            a[k]=lefthalf[i]
            i=i+1
            k=k+1
a=[50,30,20,10,40]
Mergesort(a)

print(a)
