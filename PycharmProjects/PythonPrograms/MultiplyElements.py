import numpy as numpy

mylist = [1, 2, 3, 4]

# result = 1
#
# for x in mylist:
#     result = result * x
#
# print(result)

print(numpy.prod(mylist))
print(numpy.sum(mylist))
print(numpy.array([5, 6, 8, 9]) + 10)
b = numpy.array([1.1, 2.0, 3.2])
print(b.dtype)
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print(numpy.add(a, b))
print(numpy.concatenate(a, b))
numpy.tolist()