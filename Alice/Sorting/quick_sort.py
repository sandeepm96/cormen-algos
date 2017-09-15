class QuickSort:
    def __init__(self,array):
        self.array = array
    def partition(self,low,high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low,high):
            if self.array[j] <= pivot:
                i = i + 1
                self.array[i],self.array[j] = self.array[j],self.array[i]
        self.array[i+1],self.array[high] = self.array[high],self.array[i+1]
        return i+1
    def sort(self,low,high):
        if low < high:
            pivot = self.partition(low,high)
            self.sort(low,pivot-1)
            self.sort(pivot+1,high)
    def result(self):
        self.sort(0,len(self.array)-1)
        return self.array
