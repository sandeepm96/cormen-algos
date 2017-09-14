class Quicksort:
    def __init__ (self, input_array):
        self.array = input_array

    def quick_sort(self, low, high):
        if low < high:
            divide = self.partition(low, high)
            self.quick_sort(low, divide - 1)
            self.quick_sort(divide + 1, high)

    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i+1

    def result(self):
        self.quick_sort(0,len(self.array)-1)
        return self.array
