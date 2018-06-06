from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self,parent,rank,x,y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
         # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        #If ranks are same, then make one as root and increment
        # its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
    def isCyclic(self):
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find(parent,i)
                y = self.find(parent,j)
                if x == y:
                    return True
                self.union(parent,rank,x,y)
        return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)
if g.isCyclic():
    print("Graph contains cycle")
else :
    print("Graph does not contain cycle ")