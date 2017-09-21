class LCS:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def _find_lcs(self):
        m = len(self.str1)
        n = len(self.str2)
        b = [[0 for x in range(n)] for y in range(m)]
        c = [[0 for x in range(n+1)] for y in range(m+1)]
        for i in range(m):
            for j in range(n):
                if self.str1[i] == self.str2[j]:
                    c[i+1][j+1] = c[i][j] + 1
                    b[i][j] = '\\'
                elif c[i][j+1] >= c[i+1][j]:
                    c[i+1][j+1] = c[i][j+1]
                    b[i][j] = '|'
                else:
                    c[i+1][j+1] = c[i+1][j]
                    b[i][j] = '-'
        self.b = b
        self.c = c
        self.lcs = self._lcs_str()

    def _lcs_str(self):
        lcs = ''
        i = len(self.str1)
        j = len(self.str2)
        while i>0 and j>0:
            if self.b[i-1][j-1] == '\\':
                lcs += self.str1[i-1]
                i-=1
                j-=1
            elif self.b[i-1][j-1] == '|':
                i-=1
            else:
                j-=1
        return lcs[::-1]

    def result(self):
        self._find_lcs()
        return self.lcs
