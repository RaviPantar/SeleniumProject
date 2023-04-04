# append
fruits = ['apple', 'mango', 'banana', 'apple']
fruits.append("Cherry")
print(fruits)

# copy
cp = fruits.copy()
print(cp)

# count
count = fruits.count('apple')
print(count)

# extend
tup = ('a', 'b', 'c')
fruits.extend(tup)
print(fruits)

# index
indx = fruits.index('apple')
print(indx)

# insert
fruits.insert(3, 'Jackfruit')
print(fruits)

# pop
fruits.pop(1)
print(fruits)

# remove
fruits.remove("Cherry")
print(fruits)

# reverse
fruits.reverse()
print(fruits)

# sort
fruits.sort()
print(fruits)


