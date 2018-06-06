#Main program
class BucketSort:
    def __init__(self,array):
        self.array = array
        self.sorted_array = []

    def sort(self):
        buckets = [[] for i in range(10)]
        for i in self.array:
            buckets[int(i*10)].append(i)
        for buck in buckets:
            self.sorted_array += self.insert_sort(buck)

    def insert_sort(self,arr):
        for i in range(1,len(arr)):
            for j in range(i-1,-1,-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr

    def result(self):
        self.sort()
        return self.sorted_array

test = list(map(float,input().split(' ')))
t = BucketSort(test)
print(t.result())
