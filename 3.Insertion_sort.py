def Insertion_sort(a):
    for i in range(1,len(a)):
        temp=a[i]
        j=i-1
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp
a=[40,20,10,30,50]
Insertion_sort(a)
print(a)
