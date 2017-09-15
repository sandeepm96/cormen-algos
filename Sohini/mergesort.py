class Mergesort:
    def __init__ (self, input_array):
        self.array = input_array

    def merge_sort(self, start, end):
        if start < end:
            middle = (start+end)/2
            self.merge_sort(start, middle)
            self.merge_sort(middle + 1, end)
            self.merge(start, middle, end)

    def merge(self, start, middle, end):
        array = self.array
        first_subarray = []
        second_subarray = []
        for i in range(start, middle+1):
            first_subarray.append(array[i])
        for i in range(middle+1, end+1):
            second_subarray.append(array[i])
        first_subarray.append(10**9)
        second_subarray.append(10**9)
        first_index = 0
        second_index = 0
        for i in range(start, end+1):
            number1 = first_subarray[first_index]
            number2 = second_subarray[second_index]
            if number1 < number2:
                array[i] = number1
                first_index += 1
            else:
                array[i] = number2
                second_index += 1
        self.array = array

    def result(self):
        self.merge_sort(0, len(self.array)-1)
        return self.array
