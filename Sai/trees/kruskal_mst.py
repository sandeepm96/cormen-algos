from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    # A utility function to find set of an element i
    # (uses path compression technique)
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
    def KruskalMST(self):
        result = []
        i = 0 #index for sorted edges
        e = 0 #index for result[]
        #sorted by weight
        self.graph = sorted(self.graph,key=lambda item:item[2])
        print(self.graph[0])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            parent.append(0)
        while e < self.V-1:
            print(i)
            u,v,w = self.graph[i]
            i = i+1
            x = self.find(parent,u)
            y = self.find(parent,v)
            if x!=y:
                e= e+1
                result.append([u,v,w])
                self.union(parent,rank,x,y)
            #else discard edge
        print(result)

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
 
g.KruskalMST()