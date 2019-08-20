class Node:
    def __init__(self,c,left=None,right=None):
        self.c=c
        self.left=left
        self.right=right
def serialize(root):
   if not root:
       return "{}"
   return "{%s,%s,%s}" % (root.c,serialize(root.left),serialize(root.right))
def deserialize(s):
    assert(s[0]=='{' and s[-1]=='}' )
    def close_idx(s,i0):
        assert s[i0]=='{'
        count=0
        for i,c in enumerate(s[i0:]):
            if c=='{':
                count+=1
            if c=='}':
                count-=1
            if count==0:
                return i+i0
    if s=='{}':
        return None
    i0=s.find(',')
    if i0==-1:
        return Node(s[1:-1],None,None)
    i0=i0+1
   
    i1=close_idx(s,i0)+1
    return Node(s[1:i0-1],deserialize(s[i0:i1]),deserialize(s[i1+1:-1] ))
