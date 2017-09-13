class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def _sort(self):
        for i in range(1,len(self.arr)):
            key = self.arr[i]
            j = i-1
            while j>=0 and self.arr[j]>key:
                self.arr[j+1] = self.arr[j]
                j-=1
            self.arr[j+1] = key

    def result(self):
        self._sort()
        return self.arr