from numpy.random import randint

def sol(n,l):
    ##O(|l|)
    l=set(l)
    
    pool=[]
    ##O(n)
    for k in range(n):
        if k  not in l: ##O(1) amortized
            pool.append(k)
    return pool[randint(len(pool))]