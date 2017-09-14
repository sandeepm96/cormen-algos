class Heapsort:
    def __init__ (self, input_array):
        self.array = input_array
        self.result = []

    def heap_sort(self):
        self.build_heap()
        for i in range(len(self.array), 1, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heapsize = self.heapsize -1
            self.result.append(self.array[1])
            self.max_heapify(i)

    def build_heap(self):
        self.heapsize = len(self.array)
        for i in range(len(self.array), 0, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        if l < len(self.heapsize) and self.array[l] > self.array[i]:
            largest = l
        else:
            largest = i
        if r < len(self.heapsize) and self.array[r] > self.array[largest]:
            largest = r
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.max_heapify(largest)

    def result(self):
        self.heapsort()
        return self.result
