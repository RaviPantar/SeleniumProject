mylist = [15, 6, 7, 10, 12, 20, 10, 4, 10, 4]
x = 10
coun = 0
s = "Hello"

# for ele in mylist:
#     if (ele == x):
#         coun = coun + 1
# print("{} has occured {} times".format(x, count))


# mylist1 = [15, 6, 7, 10, 12, 20, 10, 4, 10]
# x = 10
# print("{} has occured {} times".format(x, mylist1.count(x)))

from collections import Counter

dict = Counter(mylist)
print("{} has occured {} times".format(x, dict[x]))
print(dict)
s="ravisverma"
d=Counter(s)
print(d)
