mylist = ["Geeks", "for", "Geeks"]
N = 2
word = "Geeks"
count = 0
for i in range(0, len(mylist)):
    if mylist[i] == word:
        count = count + 1
    if count == N:
        del mylist[i]

print(mylist)
