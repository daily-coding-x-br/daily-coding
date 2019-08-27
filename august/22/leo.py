
class Node:
    def __init__(self,c,l=None,r=None,p=None):
        self.c=c
        self.l=l
        self.r=r
        self.p=p
        if isinstance(l,Node):
            l.p=self
        if isinstance(r,Node):
            r.p=self
    def __hash__(self):
        return id(self)

def sol(n1,n2):
    s1=set()
    s2=set()
    aux=n1
    while aux:
        s1.add(aux)
        aux=aux.p
    aux=n2
    while aux:
        s2.add(aux)
        aux=aux.p
    aux =n1
    while aux and aux not in s2:
        aux=aux.p
    return aux