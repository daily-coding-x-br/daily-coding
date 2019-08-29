from queue import Queue
class Node:
    def __init__(self,c,l=None,r=None):
        self.c=c
        self.l=l
        self.r=r
        
def sol(root):
    q=Queue()
    sums=[]
    def __sol(node,level):
        if level==len(sums):
            sums.append(0)
        sums[level]+=node.c
        if node.r:
            q.put((node.l,level+1))
        if node.r:
            q.put((node.r,level+1))
        if q.qsize():
            __sol(*q.get())
    __sol(root,0)
    im,m=0,None
    for i,v in enumerate(sums):
        if m==None or v<m:
            im,m=i,v
    return im
    
            