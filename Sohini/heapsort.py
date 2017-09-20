class Heapsort:
    def __init__ (self, input_array):
        self.array = input_array

    def heap_sort(self):
        self.build_heap()
        for i in range(self.heapsize -1, -1, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heapsize = self.heapsize -1
            self.max_heapify(0)

    def build_heap(self):
        self.heapsize = int(len(self.array))
        for i in range(len(self.array)/2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < self.heapsize and self.array[l] > self.array[i]:
            largest = l
        if r < self.heapsize and self.array[r] > self.array[largest]:
            largest = r
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.max_heapify(largest)

    def result(self):
        self.heap_sort()
        return self.array

array = [34, 23, 7, 1, 67, 3]
a = Heapsort(array)
array = a.result()
print(array )
