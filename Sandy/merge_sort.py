class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def _merge(self, p, q, r):
        L = []
        R = []
        for i in range(p,q+1):
            L.append(self.arr[i])
        for j in range(q+1,r+1):
            R.append(self.arr[j])
        L.append(10**9)
        R.append(10**9)
        print L
        print R
        i=0
        j=0
        for k in range(p,r+1):
            if L[i]<R[j]:
                self.arr[k]=L[i]
                i+=1
            else:
                self.arr[k]=R[j]
                j+=1

    def _merge_sort(self, p, r):
        if p<r:
            q = (p+r)/2
            self._merge_sort(p,q)
            self._merge_sort(q+1,r)
            self._merge(p,q,r)

    def result(self):
        self._merge_sort(0, len(self.arr)-1)
        return self.arr