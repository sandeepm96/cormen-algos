from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)
    #utility function to find subset of an element i
    def find_parent(self,parent,i):
        if parent[i] == -1:
            return i
        elif parent[i]!=-1:
            return self.find_parent(parent,parent[i])
    #utility function to do union of two sets
    def union_set(self,parent,x,y):
        x_set = self.find_parent(parent,x)
        y_set = self.find_parent(parent,y)
        parent[x_set] = y_set

    def isCyclic(self):
        parent = [-1]*(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent,i)
                y = self.find_parent(parent,j)
                if x == y:
                    return True
                self.union_set(parent,x,y)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
 
if g.isCyclic():
    print("Graph contains cycle")
else :
    print("Graph does not contain cycle ")