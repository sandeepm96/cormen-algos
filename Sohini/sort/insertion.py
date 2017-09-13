def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))

n= int(input());
arr = [];

for i in range(0, n):
    arr[i] = int(input());

def findpos(i):
    larger = 0;
    for j in range(0,i):
        if arr[j]>arr[i]:
            larger +=1;
    return larger;

def move(i):
    l = n;
    while(l >= i):
        arr[l+1] = arr[l];
        l -= 1;

for i in range(0, n):
    x = arr[i];
    y = i - findpos(i);
    move(y);
    arr[y] = x;
