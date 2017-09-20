#Main program
class MaxSubArray:
    def __init__(self,a):
        self.a = a

    def result(self):
        return str(self.max_sub_array(0,len(self.a)-1)) + ' ' + str(self.notconti())

    def notconti(self):
        a = sorted(self.a)
        sum = a[len(a)-1]
        for i in range(len(a)-2,-1,-1):
            if a[i] > 0:
                sum += a[i]
            else:
                break
        return sum
    def max_sub_array(self,low,high):
        if low == high:
            return self.a[low]
        if low > high:
            return -float('inf')
        mid = int((high+low)/2)
        left = self.max_sub_array(low,mid-1)
        right = self.max_sub_array(mid+1,high)
        left_max = self.a[mid]
        acc = self.a[mid]
        for i in range(mid-1,low-1,-1):
            acc += self.a[i]
            if acc > left_max:
                left_max = acc
        right_max = self.a[mid]
        acc = self.a[mid]
        for i in range(mid+1,high+1):
            acc += self.a[i]
            if acc > right_max:
                right_max = acc
        cross = left_max+right_max-self.a[mid]
        return max([left,right,cross])

t = int(input())
for test in range(t):
    n = int(input())
    a = list(map(int,input().split(' ')))
    s = MaxSubArray(a)
    print(s.result())
