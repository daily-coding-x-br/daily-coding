from queue import Queue

            

class Node:
        
    def __init__(self,c,l=None,r=None):
        self.c=c
        self.l=l
        self.r=r
        self.s=None
        self.s=self.encode()
    def encode(self):
        def __encode(node):
            if not node:
                return "{}"
            elif node.s:
                return node.s
            return "{%s,%s,%s}" %(str(node.c),__encode(node.l),__encode(node.r))
        return __encode(self)
    def __iter__(self):
        class BFS:
            def __init__(self,node):
                self.q=Queue()
                self.q.put(node)

            def __next__(self):
                if self.q.qsize()==0:
                    raise StopIteration
                n=self.q.get()
                if n.l:
                    self.q.put(n.l)
                if n.r:
                    self.q.put(n.r)
                return n
        return BFS(self)

def sol(t,s):
    for x in t:
        if x.s==s.s:
            return True
    return False
                
                
                
            