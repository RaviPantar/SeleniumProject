n = int(input("enter number"))

n1, n2 = 0, 1
count = 0

if n < 0:
    print("Enter the correct number")
elif n == 1:
    print("Fibonaci number is {num}".format(num=n))
else:
    for i in range(2, n):
        sum = n1 + n2
        print(sum)
        n1 = n2
        n2 = sum
