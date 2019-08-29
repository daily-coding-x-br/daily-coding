def sol(s):
    n=len(s)
    table=[0]*(n+1)
    table[-1]=1
    if s[-1]!='0':
        table[n-1]=1
    for i in reversed(range(n-1)):
        if  s[i]!='0':
            table[i]+=table[i+1]
        if s[i]=='1' or (s[i]=='2' and int(s[i+1])<7):
            table[i]+=table[i+2]
    return table[0]