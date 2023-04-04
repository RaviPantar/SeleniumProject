score = [10, 20, 60, 45, 90]
print(score[0])
print(score[-1])
print(score[:])  # new copy of list
print(score + [1, 2, 3, 5])  # list are mutable
print(score + ["A", "B", "C"])
number = [1, 2, 4, 8]
number[2] = 90
print(number)
number.append(100)
print(number)
number.append(7 * 3)
print(number)

name = ['a', 'b', 'c', 'd', 'e', 'f']
print(name)
name[2:5] = ['C', 'D', 'E']
print(name)
name[2:5] = []
print(name)
name[:] = []
print(name)
test = [20, 30, 40, 50, 60]
print(len(test))
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[1])
print(x[0][2])
