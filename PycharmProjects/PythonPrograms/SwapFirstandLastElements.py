mylist = [25, 35, 9, 24, 29]
#
# size = len(mylist)
# temp = mylist[0]
# mylist[0] = mylist[size - 1]
# mylist[size - 1] = temp
#
# print(mylist)

# mylist[0], mylist[-1] = mylist[-1], mylist[0]

# get = (mylist[-1], mylist[0])
# mylist[0], mylist[-1] = get

# start, *middle, end = mylist
# mylist = [end, *middle, start]

first = mylist.pop(0)
last = mylist.pop(-1)

mylist.insert(0, last)
mylist.append(first)

print(mylist)
