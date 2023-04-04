import numpy as np
mylist = [5, 10, 20, 15]
total = 0

print(np.sum(mylist))
for i in range(0, len(mylist)):
    total = total + mylist[i]

print("Sum of elemengts is {}".format(total))

print(sum(mylist))
