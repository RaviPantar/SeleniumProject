thistupel = ("apple", "mango", "banana", "apple")
print(thistupel)

# len
print(len(thistupel))

# count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(5))

# index
index=thistuple.index(8)
print(index)

# type of tuple
print(type(thistupel))

# Access the tuple
thistupel = ("apple", "banana", "cherry")
print(thistupel[1])

# Negative Index
print(thistupel[-1])

# convert tuple to list
x = list(thistupel)
x[2] = "Strawberry"

# add item
x.append("orange")
print(tuple(x))

# unpack tuple
fruits = ("app", "ban", "cher")
(red, yellow, green) = fruits
print(red)
print(yellow)
print(green)

# using asterik
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(red, *green, yellow) = fruits
print(red)
print(green)
print(yellow)

# loop
thistuple1 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple1):
    print(thistuple1[i])
    i = i + 1

# Join tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Muliply tuple
tuple4 = (1, 2, 3)
z = tuple4 * 3
print(z)
