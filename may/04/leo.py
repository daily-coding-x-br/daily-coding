def sol(l):
    n=len(l)
    forward=[1]*n
    backward=[1]*n
    for i in range(1,n):
        forward[i]=l[i]*forward[i-1]
    for i in reversed(range(n-1)):
        backward[i]=l[i]*backward[i+1]
    res=[]
    for i in range(n):
        res.append(backward[n-1-i]*forward[n-1-i])
    return res
