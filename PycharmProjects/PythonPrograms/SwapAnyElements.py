mylist = [25, 30, 19, 27, 74]

# pos1, pos2 = 1, 3
# mylist[pos1], mylist[pos2] = mylist[pos2], mylist[pos1]
# print(mylist)

# pos1, pos2 = 1, 3
# first_ele = mylist.pop(pos1)
# second_ele = mylist.pop(pos2 - 1)
# mylist.insert(pos1, second_ele)
# mylist.insert(pos2, first_ele)

pos1, pos2 = 1, 3
get = (mylist[pos1], mylist[pos2])
mylist[pos2], mylist[pos1] = get
print(mylist)
