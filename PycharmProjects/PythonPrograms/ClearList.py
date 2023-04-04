mylist = [6, 4, 0, 9]

# Approach 1: Clear Method
# mylist.clear()
# print(mylist)

# Approach 2
# Initialist list with No value
# mylist=[]
# print(mylist)

# Approach 3
# mylist *= 0
# print(mylist)

# Approach 4

#del mylist[1:3]
del mylist[:-1]
print(mylist)
