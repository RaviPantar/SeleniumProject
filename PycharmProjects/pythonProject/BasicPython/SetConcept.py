# set is not order based
# it stores diffrent type of data
# it performas diffrerent mathmatical operation
# it does not store duplicates

# define set use {}

s1 = {100, "Tom", "12.33", True}
print(s1)
s2 = {1, 2, 3, 1, 2, 3}
print(s2)

s3 = set("Naveen")
print(s3)
s4 = set([1, 2, 3, 4, 1])  # list
print(s4)
s5 = set((15, 20, 25, 75))  # tuple
print(s5)

# while creating a set objects you can store only numbers,Strings,tuple
# list and dictionary objects are not allowed

set1 = {(10, 20), 10, 30, 40}
print(set1)
# set1 = {{10, 20}, 10, 30, 40}  not alllowed

# set operations
# union: |
p1 = {1, 2, 3, 4, 5}
p2 = {4, 5, 6, 7, 8}
print(p1 | p2)
print(p1.union(p2))

# Intersection: &
p3 = {1, 2, 3, 4, 5}
p4 = {4, 5, 6, 7, 8}
print(p3 & p4)
print(p3.intersection(p4))

# diffrence : - or diffrence()
p5 = {1, 2, 3, 4, 5}
p6 = {4, 5, 6, 7, 8}
print(p5 - p6)
print(p6 - p5)
print(p5.difference(p6))

# symantic diifrence:^
p7 = {1, 2, 3, 4, 5}
p8 = {4, 5, 6, 7, 8}
print(p7 ^ p8)
print(p7.symmetric_difference(p8))

t1 = {"Java", "Python", "C++"}
t1.add("perl")
print(t1)

# update
t2 = {"Java", "Python", "C++"}
t2.update(["C", "VBA"])
print(t2)
t2.update(("Ruby", "Javascript"))
print(t2)

# clear
print(t2.clear())

# copy
lang = {1, 2, 3}
l1 = lang.copy()
print(l1)

# dicard
l2 = l1.discard(3)
print(l2)
print(l1)

# remove
stud = {"Naveen", "Tom", "Ram"}
stud.remove("Tom")
print(stud)
