class BubbleSort:
    def __init__(self,array):
        self.array = array
    def result(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0,n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j],self.array[j+1] = self.array[j+1],self.array[j]
        return self.array

test = list(map(int,input().split(' ')))
t = BubbleSort(test)
print(t.result())
