class SelectionSort:
    def __init__(self,array):
        self.array = array
    def result(self):
        n = len(self.array)
        for i in range(n):
            minimum = i
            for j in range(i+1,n):
                if self.array[minimum] > self.array[j]:
                    minimum = j
            self.array[i],self.array[minimum] = self.array[minimum],self.array[i]
        return self.array

test = list(map(int,input().split(' ')))
t = SelectionSort(test)
print(t.result())
