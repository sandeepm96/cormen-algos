# A Python program to print topological sorting of a graph
# using indegrees
from collections import defaultdict
 
#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def topologicalSort(self):
        indegree = [0]*self.V
        #find indegree of all nodes.
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j]+=1
        
        #creating a queue and enqueue all nodes with indegree 0.
        queue = []
        for i in range(self.V):
            if indegree[i] == 0:
                queue.append(i)
        #count of visited vertices
        count = 0
        #to store result order
        topOrder = []
        while queue:
            u = queue.pop(0)
            topOrder.append(u)
            for i in self.graph[u]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
            count+=1

        if count != self.V:
            print("there is a cycle present in the graph")
        else:
            print(topOrder)

g= Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
g.topologicalSort()