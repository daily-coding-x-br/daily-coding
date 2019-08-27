def sol(l):
    n=len(l)
    def change(id):
        if 1<=l[id]<=n and l[l[id]-1]!=l[id]:
            l[l[id]-1],l[id]=l[id],l[l[id]-1]
            if 1<=l[id]<=id:
                change(id)
    for id in range(n):
        change(id)
    
    for i in range(n):
        if l[i]!=i+1:
            return i+1
        