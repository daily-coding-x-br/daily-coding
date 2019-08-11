import json

    
class HashTree:
    def __init__(self,s):
        self.tree=json.loads(s)
        has_father={}
        for p,fl in self.tree.items():
            if not has_father.get(p):
                has_father[p]=False
            for f in fl:
                has_father[f]=True
        roots=[course for course,value in has_father.items() if not value]
        self.new_courses=set(self.tree.keys())
        self.res=[]
        for t in roots:
            self.dfs(t)
        
    def dfs(self,father):
        for t in self.tree[father]:
            if t in self.new_courses:
                self.new_courses.remove(t)
                self.dfs(t)
        self.res.append(father)
                
        

    