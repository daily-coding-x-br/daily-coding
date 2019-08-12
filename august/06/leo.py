import math

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
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
        a[i+j],a[n-j]=a[n-j],a[i+j]# -*- coding: utf-8 -*-

def all_permutations(a):
    res=[a]
    for i in range(fact(len(a))-1):
        a=a.copy()
        next_permutation(a)
        res.append(a)
    return res