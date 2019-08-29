class Node:
    def __init__(self,c,l=None,r=None):
        self.c=c
        self.l=l
        self.r=r
        
def sol(root):
    def __sol(node):
        if not node.l and not node.r:
            return True,1
        cr,r=True,0
        if node.r:
            cr,r=__sol(node.r)
        cl,l=True,0
        if node.l:
            cl,l=__sol(node.l)
        if (node.l and node.r and (node.r.c==node.l.c==node.c ) and cl and cr) \
            or (node.l and not node.r and node.l.c==node.c and cl) or (node.r and not node.l and node.r.c==node.c and cr):
            return True,1+r+l
        return False, r+l
    _,res=__sol(root)
    return res
