import numpy as np
class ProblemSolver:
    def __init__(self,table):
        self.table=np.array(table)
        self.n,self.m=self.table.shape
        self.visited=np.zeros((self.n,self.m))
    def check(self,i,j,word):
        assert(0<=i<self.n and 0<=j<self.m)
        if len(word)==1 and  self.table[i,j]==word[0] and not self.visited[i,j]:
            return True
        if self.table[i,j]!=word[0] or self.visited[i,j]:
            return False
        
        self.visited[i,j]=1
        word=word[1:]
        if i>0 and self.check(i-1,j,word):
            return True
        if i<self.n-1 and self.check(i+1,j,word):
            return True
        if j>0 and self.check(i,j-1,word):
            return True
        if j<self.m-1 and self.check(i,j+1,word):
            return True
        self.visited[i,j]=0
        return False
    
def solve(table,word):
    p=ProblemSolver(table)
    for i in range(p.n):
        for j in range(p.m):
            if p.check(i,j,word):
                return True
    return False
        
            