import numpy as np
from queue import Queue
class Node:
    def __init__(self,c,p,l=None,r=None):
        self.l=l
        self.c=c
        self.r=r
        self.p=p
        self.passed=False

class TreeGen:
    def __init__(self,eps=1e-3,a=0.75,b=1.0):
        assert (a+b)/2<1 and b>=1
        self.eps=eps
        self.a=a
        self.b=b
        self.q=Queue()
        self.root=TreeGen.__gen_node(1)
        self.q.put(self.root)
        print('Average leaf height will be {}'.format(np.log2(eps)/np.log2((a+b)/2)))
    def __str__(self):
        def __encode(node):
            if not node:
                return "{}"
            return "{%s,%s,%s}" %(str(node.c),__encode(node.l),__encode(node.r))
        return  __encode(self.root)
    def __gen_node(p):
        return Node(np.random.randint(low=0,high=10000000),p)
    def __next__(self):
        if self.q.qsize()==0:
            raise StopIteration
        n=self.q.get()
        if not n.passed:
            n.passed=True
            pl=n.p*np.random.uniform(low=self.a,high=self.b)
            pr=n.p*np.random.uniform(low=self.a,high=self.b)
            if pl>self.eps:
                n.l=TreeGen.__gen_node(pl)
                self.q.put(n.l)
            if pr>self.eps:
                n.r=TreeGen.__gen_node(pr)
                self.q.put(n.r)
        else:
            if n.l:
                self.q.put(n.l)
            if n.r:
                self.q.put(n.r)
        return n
    def __iter__(self):
        return self
            