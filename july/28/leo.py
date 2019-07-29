class Node:
    def __init__(self,id):
        self.id=id
        self.neigh=set()
    def add_neigh(self,b):
        self.neigh.add(b)
class DirectedGraph:
    def __init__(self):
        self.nodes={}
        self.nodes_id=set()
    def add_edge(self,a,b):
        if a not in self.nodes_id:
            self.nodes_id.add(a)
            self.nodes[a]=Node(a)
        if b not in self.nodes_id:
            self.nodes_id.add(b)
            self.nodes[b]=Node(b)
        self.nodes[a].add_neigh(b)
    
        
class ProblemSolve:
    def __init__(self,lines):
        self.graphs={'e':DirectedGraph(),'n':DirectedGraph()}
        self.been_to=set()
        self.checks={'n':set(),'e':set()}
        self.lines=lines
    def parse_line(self,line):
        a,direc,b=line.split()
        if direc in ['N','NE','NW']:
            self.graphs['n'].add_edge(b,a)
        if direc in ['S','SE', 'SW']:
            self.graphs['n'].add_edge(a,b)
        if direc in ['W','NW', 'SW']:
            self.graphs['e'].add_edge(a,b)
        if direc in ['E','NE', 'SE']:
            self.graphs['e'].add_edge(b,a)
    def check_cycle(self,node_id,direc):
        self.been_to.add(node_id)
        self.checks[direc].add(node_id)
        for t in self.graphs[direc].nodes[node_id].neigh:
            if t in self.been_to:
                return False
            elif t not in self.checks[direc] and  not self.check_cycle(t,direc):
                return False
        self.been_to.remove(node_id)
        return True
    def solve(self):
        for l in self.lines:
            self.parse_line(l)
        for d in ['n','e']:
            for node_id in self.graphs[d].nodes_id:
                if node_id not in self.checks[d] and not self.check_cycle(node_id,d):
                    return False
        return True
            
        