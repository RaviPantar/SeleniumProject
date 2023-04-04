from collections import Counter
s = "My name is ravi your name is raj"

words = {}

for i in s.split(" "):
    if i in words:
        words[i] += 1
    else:
        words[i] = 1



print(Counter(s.split(" ")))
