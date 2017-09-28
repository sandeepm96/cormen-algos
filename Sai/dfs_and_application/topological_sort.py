# In topological sorting, we use a temporary stack. We don’t print the vertex immediately,
#  we first recursively call topological sorting for all its adjacent vertices,
#  then push it to a stack. Finally, print contents of stack. Note that a vertex is pushed
#  to stack only when all of its adjacent vertices (and their adjacent vertices and so on)
#  are already in stack.
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def topologicalSortUtil(self,v,visited,stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
        stack.insert(0,v)

    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
        print(stack)

g= Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
print("Following is a Topological Sort of the given graph")
g.topologicalSort()