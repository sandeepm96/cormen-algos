class Insertionsort:
    def __init__ (self, input_array):
        self.array = input_array

    def insertion_sort(self):
        array = self.array
        for i in range(1, len(array)):
            j = i-1
            key = array[i]
            while (j >= 0) and (array[j] > key):
               array[j+1] = array[j]
               j -= 1
            array[j+1] = key
        self.array = array

    def result(self):
        return self.array
