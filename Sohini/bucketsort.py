class Bucketsort:
    def __init__ (self, input_array):
        self.array = input_array
        self.resultant_array = []

    def bucket_sort(self):
        length = len(self.array)
        minimun = min(self.array)
        maximum = max(self.array)
        number_of_buckets = int((maximum - minimun)**0.5)
        self.bucket_list = [[] for x in range(number_of_buckets+2)]
        for i in range(0, length):
            bucket_index = (self.array[i] - minimun)/number_of_buckets
            self.bucket_list[bucket_index].append(self.array[i])
        for index in range(0, 10):
            self.insertion_sort(index)

    def insertion_sort(self, i):
        array = self.bucket_list[i]
        for i in range(1, len(array)):
            j = i-1
            key = array[i]
            while (j >= 0) and (array[j] > key):
               array[j+1] = array[j]
               j -= 1
            array[j+1] = key
        self.resultant_array.extend(array)

    def result(self):
        self.bucket_sort()
        return self.resultant_array

b = Bucketsort([23, 56, 12, 78, 32, 3, 5, 4])
print(b.result())
