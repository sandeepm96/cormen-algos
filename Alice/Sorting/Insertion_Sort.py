#Main program
class InsertionSort:
    def __init__(self,array):
        self.array = array
    def result(self):
        for i in range(1,len(self.array)):
            for j in range(i-1,-1,-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j],self.array[j+1] = self.array[j+1],self.array[j]
        return self.array

test = list(map(int,input().split(' ')))
t = InsertionSort(test)
print(t.result())
