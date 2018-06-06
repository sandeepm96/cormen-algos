import math
class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for i in range(vertices)]for j in range(vertices)]

    def printMST(self,parent):
        for i in range(1,self.V):
            print(parent[i],'--',i,'--weight->',self.graph[i][parent[i]])
    def minKey(self,key,mstSet):
        tempMin = math.inf
        for v in range(self.V):
            if key[v] < tempMin and mstSet[v] == False:
                tempMin = key[v]
                minIndex = v
        return minIndex

    def primMST(self):
        #adding max weight to each edge
        key = [math.inf]*self.V
        parent = [None]*self.V #array to store constructed MST
        key[0] = 0
        #set of vertices added in MST
        mstSet = [False]*self.V
        parent[0] = -1
        for node in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not
            # yet processed. u is always equal to src in first iteration
            u = self.minKey(key,mstSet)
            # Put the minimum distance vertex in the shortest path tree
            mstSet[u] = True
            # Update dist value of the adjacent vertices of the picked vertex
            # only if the current distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v]>0 and mstSet[v] == False and key[v]>self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

 
g  = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0],
           ]
 
g.primMST()