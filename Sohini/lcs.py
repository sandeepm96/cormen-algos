class lcs:
    def __init__(self, array1, array2):
        self.first_array = array1
        self.second_array = array2
        self.b = [[0] * len(self.first_len)-1] * len(self.second_array)-1
        self.c = [[0] * len(self.first_len)] * len(self.second_array)

    def lcs_length(self):
        first_len = len(self.first_array)
        second_len = len(self.second_array)
        for i in range(0, first_len):
            self.c[i][0] = 0
        for i in range(0, second_len):
            self.c[0][i] = 0
        for i in range(0, first_len):
            for j in range(0, second_len):
                if self.first_array[i] == self.second_array[j]:
                    self.c[i][j] = self.c[i-1][j-1] + 1
                    # 0 is northwest
                    self.b[i][j] = 0
                elif self.c[i-1][j] > self.c[i][j-1]:
                    self.c[i][j] = self.c[i-1][j]
                    # 1 is north
                    self.b[i][j] = 1
                else:
                    self.c[i][j] = self.c[i][j-1]
                    # 2 is west
                    self.b[i][j] = 2
        self.print_lcs(first_len, second_len)

    def print_lcs(self, i, j):
        if i == 0 or j == 0:
            return
        elif self.b[i][j] == 0:
            self.print_lcs(i-1, j-1)
            print(self.first_array[i])
        elif self.b[i][j] == 1:
            self.print_lcs(i-1, j)
        else:
            self.print_lcs(i, j-1)

    def result(self):
        self.lcs_length()
