#Python script to generate random inputs for the program
#Change it according to requirements
import random
n = random.randrange(1,10,1)
print(str(n))
for i in range(n-1):
    x = i
    y = random.randrange(1,n,1)
    if x == y:
        i -= 1
        continue
    print(str(x) + " "+str(y))
