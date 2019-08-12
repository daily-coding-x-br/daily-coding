def couple_primes(n):
    assert(n>2)
    is_prime = [False,False]
    for t in range(2,n-1):
        for k in range(2,int(t/2)+1):
            if not t%k:
                is_prime.append(False)
                break
        else :
            is_prime.append(True)
    for k in range(2,int(n/2)+1):
        print(k)
        if is_prime[k] and is_prime[n-k]:
            return (k,n-k)