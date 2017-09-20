class CountingSort:
    def __init__(self,array):
        self.array = array
        self.sorted_array = [0 for i in range(len(self.array))]
        self.count = []

    def sort(self):
        largest = max(self.array)
        self.count = [0 for i in range(largest+1)]
        for i in self.array:
            self.count[i] += 1
        for j in range(1,len(self.count)):
            self.count[j] = self.count[j] + self.count[j-1]
        for k in range(len(self.array)-1,-1,-1):
            self.sorted_array[self.count[self.array[k]]-1] = self.array[k]
            self.count[self.array[k]] -= 1

    def result(self):
        self.sort()
        return self.sorted_array
