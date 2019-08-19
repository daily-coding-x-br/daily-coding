def sol(a,b):
    if len(a)!=len(b):
        return False
    s=a+a
    return b in s