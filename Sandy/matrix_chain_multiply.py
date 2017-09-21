class MatChainMult:
    def __init__(self, p):
        self.p = p
        self._mat_chain_order()

    def _mat_chain_order(self):
        n = len(self.p) - 1
        m = [[0 for x in range(n)] for y in range(n)]
        s = [[0 for x in range(n-1)] for y in range(n-1)]
        for l in range(1,n):
            for i in range(n-l):
                j = i+l
                m[i][j] = 10**9
                for k in range(i,j):
                    q = m[i][k] + m[k+1][j] + self.p[i]*self.p[k+1]*self.p[j+1]
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j-1] = k
        self.m,self.s = m,s

    def _optimal_parens(self,i,j,str):
        if i==j:
            str += 'A{}'.format(i+1)
        else:
            str += '({0}{1})'.format(self._optimal_parens(i,self.s[i][j-1],str), self._optimal_parens(self.s[i][j-1]+1,j,str))
        return str

    def optimal_cost(self):
        return self.m[0][len(self.m)-1]

    def optimal_order(self):
        return self._optimal_parens(0,len(self.p)-2,'')
