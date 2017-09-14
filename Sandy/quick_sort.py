class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def _partition(self, p, r):
        pivot_ele = self.arr[r]
        i = p-1
        for j in range(p,r):
            if self.arr[j] <= pivot_ele:
                i+=1
                self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
        self.arr[i+1], self.arr[r] = self.arr[r], self.arr[i+1]
        return i+1

    def _quick_sort(self, p, r):
        if p<r:
            q = self._partition(p,r)
            self._quick_sort(p,q-1)
            self._quick_sort(q+1,r)

    def result(self):
        self._quick_sort(0, len(self.arr)-1)
        return self.arr