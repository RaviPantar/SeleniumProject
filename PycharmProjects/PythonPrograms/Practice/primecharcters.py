str = "mypythonprogram"

m = len(str)

l = []

d = " "

for i in range(2, m):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        l.append(i)

for k in l:
    d += str[k]

print(d)
