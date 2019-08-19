##we assume it refers to the MAXIMUM number of hops
def sol(l):
    n=len(l)
    aux=list(range(n))
    for i in reversed(range(0,n-1)):
        aux[i]=max(aux[i:i+l[i]+1])
    return aux[0]==n-1