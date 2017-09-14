class CountingSort:
    def __init__(self, arr):
        self.arr = arr
        self.sorted_arr = [0 for x in range(len(self.arr)+1)]

    def _count_sort(self):
        largest = max(self.arr)
        count_arr = [0 for x in range(largest+1)]
        for i in range(len(self.arr)):
            count_arr[self.arr[i]] += 1
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i-1]
        for i in range(len(self.arr)):
            self.sorted_arr[count_arr[self.arr[i]]] = self.arr[i]
            count_arr[self.arr[i]] -= 1

    def result(self):
        self._count_sort()
        return self.sorted_arr[1:]