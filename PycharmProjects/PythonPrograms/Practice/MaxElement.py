arr = [22, 92, 33, 12, 25]
max = arr[0]
n = len(arr)

for i in range(1, n):
    if arr[i] > max:
        max = arr[i]

print(max)
