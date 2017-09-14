class RadixSort:
    def __init__(self, arr):
        self.arr = arr

    def _count_sort(self, exp):
        n = len(self.arr)
        sorted_arr = [0] * (n)
        count_arr = [0] * (10)
        for i in range(n):
            index = int(self.arr[i]/exp)
            count_arr[index%10] += 1
        for i in range(1, 10):
            count_arr[i] += count_arr[i-1]
        for i in range(n-1,-1,-1):
            index = int(self.arr[i]/exp)
            sorted_arr[count_arr[index%10]-1] = self.arr[i]
            count_arr[index%10] -= 1
        self.arr = sorted_arr

    def _radix_sort(self):
        maximum = max(self.arr)
        exp = 1
        while maximum/exp > 0:
            self._count_sort(exp)
            exp *= 10

    def result(self):
        self._radix_sort()
        return self.arr