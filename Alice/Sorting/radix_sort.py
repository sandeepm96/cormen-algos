class RadixSort:
    def __init__(self,array):
        self.array = array

    def sort(self,exp):
        count = [0]*(10)
        sorted_array = [0]*(len(self.array))
        for i in range(len(self.array)):
            index = int(self.array[i]/exp)
            count[index%10] += 1
        for j in range(1,10):
            count[j] += count[j-1]
        for k in range(len(self.array)-1,-1,-1):
            index = int(self.array[k]/exp)
            sorted_array[count[index%10]-1] = self.array[k]
            count[index%10] -= 1
        self.array = sorted_array

    def result(self):
        max_element = max(self.array)
        exp = 1
        while (max_element/exp) > 0:
            self.sort(exp)
            exp *= 10
        return self.array
