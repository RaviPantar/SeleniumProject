str = "I Love Python Programming"

words = str.split(" ")

words.reverse()

str1 = " "
for i in words:
    str1 += i
print(str1, ' ')

# str=" "
# print(str.join(words))
# output = ' '.join(words)
# print(output)
