def Selection_sort(a):
    for i in range(0,len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
a=[20,10,30,40,50]
Selection_sort(a)
print(a)
