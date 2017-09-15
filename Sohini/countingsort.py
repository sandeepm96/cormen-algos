class Countingsort:
    def __init__ (self, input_array):
        self.array = input_array
        self.resultant_array = [0 for i in range(0, len(self.array)+1)]

    def counting_sort(self, k):
        temp_store = []
        length = len(self.array)
        for i in range(0, k+1):
            temp_store.append(0)
        for i in range(0, length):
            temp_store[self.array[i]] = temp_store[self.array[i]] + 1
        for i in range(1, k+1):
            temp_store[i] = temp_store[i] + temp_store[i-1]
        for i in range(length-1, -1, -1):
            self.resultant_array[temp_store[self.array[i]]] = self.array[i]
            temp_store[self.array[i]] = temp_store[self.array[i]] -1

    def result(self):
        maximum = max(self.array)
        self.counting_sort(maximum)
        return self.resultant_array
