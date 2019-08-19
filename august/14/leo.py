class Node:
    def __init__(self,cont,ant,prox):
        self.c=cont
        self.l=ant
        self.r=prox
class DoubleLL:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @classmethod
    def from_string(cls,s):
        init=Node(None,None,None) 
        last=init
        for letter in s:
            last.c=letter
            last.r=Node(None,last,None)
            last=last.r
        return DoubleLL(init,last.l)
    
    def is_palindrome(self):
        l=self.first
        r=self.last
        while l!=r and l.l!=r:
            if l.c!=r.c:
                return False
            l=l.r
            r=r.l
        return True
        
            
