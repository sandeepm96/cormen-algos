from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    #recursive function to perform traversal
    def DFSUtil(self,v,visited):
        #mark viisted nodes and print them 
        visited[v]=True
        print(v)
        #Recurring function to print all vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False :
                self.DFSUtil(i,visited)
        
    #driver function of DFS
    def DFS(self,v,num_of_nodes):
        # mark all nodes not unvisited
        visited = [False] * (num_of_nodes)
        # visited = [False] * (len(self.graph))
        self.DFSUtil(v,visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(3, 4)

g.DFS(2,5)