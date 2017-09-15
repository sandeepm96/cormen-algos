import os,sys,inspect
sys.path.append('../')
# Import your package here
from Rishav.radixsort import RadixSort as s

def checkArrayEqual(a,b):
    if not len(a) == len(b):
        return False
    for i in range(len(a)):
        if not a[i] == b[i]:
            return False
    return True

tests = [
    [4,5,6,7,8,9,10,11,12,13,14,15],
    [4],
    [1,1,1,1,1,1,1,1,1,1,1],
    [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],
    [6,5,4,3,2,1,2,3,4,5,6],
    [3,3,3,3,3,4,4,4,4,5,5,5,6,3,3,3,1,1,1,1,4,4,3,7]
]

for test in tests:
    subject = s(test)
    if checkArrayEqual(subject.result(),sorted(test)):
        print("Test Passed")
    else:
        raise Exception('Test Failed')
