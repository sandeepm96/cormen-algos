class MaxSubarray:
    def __init__(self, arr):
        self.arr = arr

    def _max_subarray(self, l, h):
        if l==h:
            return self.arr[l]
        else:
            m = (l+h)/2
            return max(self._max_subarray(l,m), self._max_subarray(m+1,h), self._max_cross_subarray(l,m,h))

    def _max_cross_subarray(self, l, m, h):
        max_left = -10**9
        max_right = -10**9
        left_sum = 0
        right_sum = 0
        for i in range(m, l-1, -1):
            left_sum+=self.arr[i]
            if left_sum>max_left:
                max_left = left_sum
        for i in range(m+1, h+1):
            right_sum+=self.arr[i]
            if right_sum>max_right:
                max_right = right_sum
        return max_left+max_right

    def result(self):
        maximum = self._max_subarray(0, len(self.arr)-1)
        return maximum
