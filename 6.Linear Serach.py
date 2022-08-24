a=[10,20,30,40]
k=2
f=0
for i in range(0,len(a)):
    if a[i]==k:
        f=1
        break
if f==1:
    print(k,"Found")
else:
    print(k,"Not Found")
    
