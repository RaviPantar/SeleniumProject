import re

str = "Welocme@@star#th%gthr$!n087*"

regex = re.compile('@$!*#%')

if (regex.search(str) == None):
    print("special character present in string")
else:
    print("No String contain special character")

str1 = "india"
x = re.findall("i.{3}a", str1)
print(x)
# print(type(x))

str2 = " I love This Country"
x = re.findall("[A-Z]", str2)
print(x)

str3 = "Love you india"
print(re.findall("^you$", str3))

str4 = "Love You india"
print(re.findall("\ALove", str4))

str5 = "rav123"
print(re.findall("\d", str5))

str6 = "Ravi India first"
x = re.findall("\S", str6)
print(x)

str4 = "Ravi123"
x=re.findall("\D",str4)
print(x)
