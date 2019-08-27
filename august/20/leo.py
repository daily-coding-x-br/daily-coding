class Node:
    def __init__(self,content,l=None,r=None):
        self.c=content
        self.l=l
        self.r=r

def get_paths(root):
    def __get_paths(node,res,path):
        path.append(node.c)
        if not (node.l or node.r):
            res.append(path.copy())
        if node.l:
            __get_paths(node.l,res,path)
        if node.r:
            __get_paths(node.r,res,path)
        del path[-1]
    res=[]
    path=[]
    __get_paths(root,res,path)
    return res