class max_sub_array:
    def __init__ (self, input_array):
        self.array = input_array

    def max_crossing_subarray(self, low, mid, high):
        array = self.array
        left_sum = -1
        s = 0
        max_left = 0
        max_right = 0
        for i in range(mid, low-1, -1):
            s = s + array[i]
            if s > left_sum:
                left_sum = s
                max_left = i
        right_sum = -1
        s = 0
        max_left = 0
        max_right = 0
        for i in range(mid, low-1, -1):
            s = s + array[i]
            if s > left_sum:
                right_sum = s
                max_right = i
        return {max_left, max_right, left_sum + right_sum}

    def max_sub_array(self, low, high):
        if high == low:
            return{low, high, self.array[low]}
        else:
            mid = int((low+high)/2)
            left_low, left_high, left_sum = max_sub_array(low, mid)
            right_low, right_high, right_sum = max_sub_array(mid+1, high)
            cross_low, cross_high, cross_sum = max_crossing_subarray(low, mid, high)
            if left_sum >= right_sum and left_sum >= cross_sum:
                return {left_low, left_high, left_sum}
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return {right_low, right_high, right_sum}
            else:
                return {cross_low, cross_high, cross_sum}

    def result(self):
        return self.array
