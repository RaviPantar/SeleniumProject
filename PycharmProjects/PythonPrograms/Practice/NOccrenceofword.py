mylist = ["Geeks", "for", "Geeks"]
word = "Geeks"
count = 0
for i in range(0, len(mylist)):
    if mylist[i] == word:
        count = count + 1

print(count)
