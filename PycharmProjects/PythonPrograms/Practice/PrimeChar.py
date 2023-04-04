s = "mynameisravi"
c = len(s)
count = 0
l = []
d = " "
for i in range(1, c):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        l.append(i)

for k in l:
    d = d+s[k]

print(d)
