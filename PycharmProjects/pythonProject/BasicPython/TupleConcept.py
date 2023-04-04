# Tuple vs list
# store the values in tuple with (),but in List:[]
# tuple is immutable but list is mutable
names = ("Java", "Dot net", "Python", "C#")
marks = (100, 200, 30, 400)
employeedata = ("Tom", 123, 'a', 22.50, True)

print(names[0])
# print(marks[-3])
# print(employeedata)

list = [10, 20, 30]
list[1] = 100  # mutable in list
# del names

# marks[0] = 10  # immutable in tuple

t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(t1 + t2)

t3 = (1, 2, 3)
print(t3 * 4)

t4 = (1, 2, 3, 4, 5, 6)
print(t4[1:3])

# in
employeedata1 = ("Tom", 123, 'a', 22.50, True)
print(123 in employeedata1)
print(35 not in employeedata1)

print(len(employeedata1))

N = (10, 15, 28, 41)
print(max(N))
print(min(N))
print(sum(N))
