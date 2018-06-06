from collections import defaultdict
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self,v,w):
        self.graph[v].append(w)
        self.graph[w].append(v)
    
    def isCycleUtil(self,v,visited,parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                if (self.isCycleUtil(i,visited,v)):
                    return True
            elif parent != i:
                return True
        return False

    def isCyclic(self):
        visited = [False]*(self.V)
        for i in range(self.V):
            if visited[i] == False:
                if (self.isCycleUtil(i,visited,-1))==True:
                    return True
        return False

# Create a graph given in the above diagram
# g = Graph(5)
# g.addEdge(1, 0)
# g.addEdge(0, 2)
# g.addEdge(2, 0)
# g.addEdge(0, 3)
# g.addEdge(3, 4)
 
# if g.isCyclic():
#     print("Graph contains cycle")
# else :
#     print("Graph does not contain cycle ")
g1 = Graph(4)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
 
 
if g1.isCyclic():
    print("Graph contains cycle")
else :
    print("Graph does not contain cycle ")
