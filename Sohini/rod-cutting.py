class rodCutting:
    def __init__(self, price_array, n):
        self.length = n
        self.input_array = price_array

    def cut_rod(self):
        r = [-1] * self.length
        r[0] = 0
        for i in range(0, self.length):
            for j in range(0, i+1):
                q = max(q, self.input_array[j] + r[i-j])
            r[i] = q
        return r[self.length]

    def result(self):
        max_profit = self.cut_rod()
        print(max_profit)
