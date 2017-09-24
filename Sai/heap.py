from heapq import *
class heap:
    def __init__(self):
        self.heap = list()
    def push(self,item):
        heappush(self.heap, item)
    def printheap(self):
        print(self.heap)
    def heapsort(self):
        return [heappop(self.heap) for i in range(len(self.heap))] 

# h = heap()
# h.push(4)
# h.push(12)
# h.push(8)
# h.push(19)
# print(h.heapsort())