class HeapSort:
    def __init__(self,array):
        self.array = array
        self.arr_size = len(self.array)

    def result(self):
        self.buildHeap()
        for i in range(len(self.array)-1,-1,-1):
            self.array[0],self.array[i] = self.array[i],self.array[0]
            self.arr_size -= 1
            self.heapify(0)
        return self.array

    def buildHeap(self):
        for i in range(int((len(self.array))/2),-1,-1):
            self.heapify(i)

    def heapify(self,i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < self.arr_size and self.array[left] > self.array[largest]:
            largest = left
        if right < self.arr_size and self.array[right] > self.array[largest]:
            largest = right
        if not i == largest:
            self.array[i],self.array[largest] = self.array[largest],self.array[i]
            self.heapify(largest)

test = list(map(int,input().split(' ')))
t = HeapSort(test)
print(t.result())
