class Radixsort:
    def __init__ (self, input_array):
        self.array = input_array

    def radix_sort(self):
        exp = 1
        largest = max(self.array)
        while largest/exp > 0:
            self.counting_sort(exp)
            exp *= 10

    def counting_sort(self, exp):
        length = len(self.array)
        count = [0] * (10)
        resultant_array = [0] * length
        for i in range(0, length):
            index = int(self.array[i]/exp)
            count[index%10] += 1
        for i in range(1, 10):
            count[i] += count[i-1]
        for i in range(length-1, -1, -1):
            index = int(self.array[i]/exp)
            resultant_array[count[index%10]-1] = self.array[i]
            count[index%10] -= 1
        self.array = resultant_array

    def result(self):
        self.radix_sort()
        return self.array

s = Radixsort([2,3,12,45,32,12,90])
print(s.result())
