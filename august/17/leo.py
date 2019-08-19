class Node:
    def __init__(self,cont,r):
        self.c=cont
        self.r=r
class Queue:
    def __init__(self,first=None,last=None):
        self.first=first
        self.last=last
    def insert(self,c):
        if not self.first:
            self.first=Node(c,None)
            self.last=self.first
        else:
            self.last.r=Node(c,None)
            self.last=self.last.r
    def pop(self):
        if not self.first:
            return None
        res=self.first
        self.first=self.first.r
        return res
class BTNode:
    def __init__(self,c,left=None,right=None):
        self.c=c
        self.left=left
        self.right=right
    def BFS(self,l=Queue()):
        print(self.c)
        if self.left:
            l.insert(self.left)
        if self.right:
            l.insert(self.right)
        x=l.pop()
        if x:
            x.c.BFS(l)

