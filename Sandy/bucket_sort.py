class BucketSort:
    def __init__(self, arr):
        self.arr = arr
        self.sorted_arr = []

    def _bucket_sort(self):
        buckets = [[] for x in range(10)]
        for x in self.arr:
            buckets[int(x*10)].append(x)
        for buck in buckets:
            self.sorted_arr += self._ins_sort(buck)

    def _ins_sort(self, array):
        for i in range(1,len(array)):
            key = array[i]
            j=i-1
            while j>=0 and array[j]>key:
                array[j+1] = array[j]
                j-=1
            array[j+1] = key
        return array

    def result(self):
        self._bucket_sort()
        return self.sorted_arr