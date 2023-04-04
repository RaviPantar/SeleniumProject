N = int(input("Enter Number"))
fact = 1
if N <= 0:
    print(f"factorial of {N} is 1")
elif N == 1:
    print(f"factorial of {N} is 1")
else:
    for i in range(1, N + 1):
        fact = fact * i

    print(fact)
