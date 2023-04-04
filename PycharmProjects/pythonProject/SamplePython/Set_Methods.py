# add element
fruits = {"apple", "Strawberry", "cherry"}
fruits.add("mango")
print(fruits)

# copy element
cp = fruits.copy()
print(cp)

# difference
fruits = {"apple", "banana", "mango"}
mnc = {"google", "microsoft", "apple"}
z = fruits.difference(mnc)
print(z)  # mango ,banana

# discard
fruits1 = {"apple", "banana", "mango"}
fruits1.discard("banana")
print(fruits1)  # apple.mango

# intersection
section = fruits.intersection(mnc)
print(section)  # apple

# pop
fruits2 = {"apple", "banana", "mango"}
pop = fruits2.pop()
print(fruits2)  # apple, mango

# remove
fruits3 = {"apple", "banana", "mango"}
remove = fruits3.remove("apple")
print(fruits3)  # banana,mango

# symmetric difference
sym = fruits.symmetric_difference(mnc)
print(sym)  # {'banana', 'mango', 'google', 'microsoft'}

# union
u = fruits.union(mnc)
print(u)  # {'microsoft', 'google', 'mango', 'apple', 'banana'}

# update
fruits.update(mnc)
print(fruits)
