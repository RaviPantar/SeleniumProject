factorial = 1

num = int(input("enter number"))

if num < 0:
    print("its Negative number")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
