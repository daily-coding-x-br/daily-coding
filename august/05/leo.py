import math
        
def next_permutation(a):
    n=len(a)
    i=n-2
    while i >=0:
        if a[i]<a[i+1]:
            break
        i-=1
    if i>=0:
        for j in range(i+1,n):
            if (j==n-1 and a[j]>a[i]) or (a[j]>=a[i] and a[j+1]<a[i]):
                a[i],a[j]=a[j],a[i]
    
    print(a)
    t=math.ceil((n-1-i)/2)
    print(t)
    for j in range(1,t+1):
        a[i+j],a[n-j]=a[n-j],a[i+j]
        