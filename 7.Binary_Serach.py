def BS(a,k,low,high):
    while low<=high:
        mid=low+high//2
        if k==a[mid]:
            return mid
        elif k>a[mid]:
            low=mid+1
        else:
            high=mid-1
            return -1
a=[10,20,30]
k=2
low=0
high=len(a)-1
r=BS(a,k,low,high)
if r==-1:
    print(k,"Not Found")
else:
    print(k,"Found")
