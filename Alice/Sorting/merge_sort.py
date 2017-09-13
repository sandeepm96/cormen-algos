#Main program
class MergeSort:
    def __init__(self,array):
        self.array = array
    def result(self):
        self.sort(0,len(self.array)-1)
        return self.array
    def sort(self,front,rear):
        if front>rear or front == rear:
            return
        mid = int((front+rear)/2)
        self.sort(front,mid)
        self.sort(mid+1,rear)
        self.merge(front,mid,rear)

    def merge(self,front,mid,rear):
        n1 = mid-front+1
        n2 = rear-mid
        L = []
        R = []
        for i in range(n1):
            L.append(self.array[front+i])
        for j in range(n2):
            R.append(self.array[mid+j+1])
        L.append(float('inf'))
        R.append(float('inf'))
        i = 0
        j = 0
        for k in range(front,rear+1):
            if L[i]<=R[j]:
                self.array[k]=L[i]
                i=i+1
            else:
                self.array[k]=R[j]
                j=j+1

test = list(map(int,input().split(' ')))
t = MergeSort(test)
print(t.result())
