def sol(l):
    table=[l[0],l[1]]
    for i in range(2,len(l)):
        if l[i]<=0:
            table.append(table[-1])
        else:
            table.append(max((table[-1],l[i]+table[-2])))
    return max((table[-1],table[-2]))