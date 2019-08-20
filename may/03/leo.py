def sol(l,N):
    seen = set()
    for k in l:
        if (N-k) in seen:
            return True
        seen.add(k)
    return False
