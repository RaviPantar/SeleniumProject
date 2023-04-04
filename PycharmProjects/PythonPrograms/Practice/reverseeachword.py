str = "I Love Python Programming"

words = str.split(" ")
str =[]
for i in words:
    str.append(i[::-1])

str.reverse()
print(str)