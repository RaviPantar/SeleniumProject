from collections import Counter

# Method 1
s = str(input("Enter the String  "))
occur = {}
for i in s:
    if i in occur:
        occur[i] += 1
    else:
        occur[i] = 1
print(occur)


# Method 2
s1 = "rustompavriravi"
print(Counter(s1))

# Method 2
s2 = "ravipantarunify"
tes_occur = {}
for key in s2:
    tes_occur[key] = tes_occur.get(key, 0) + 1
#print(tes_occur)
