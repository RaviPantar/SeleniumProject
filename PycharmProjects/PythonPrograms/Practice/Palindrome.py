N = int(input("Enter the Number"))
num1 = N
rev = 0
while N != 0:
    rem = N % 10
    rev = rev * 10 + rem
    N //= 10
if rev == num1:
    print("Palindrome")
else:
    print("Not palindrome")

num = 123456
print(str(num)[::-1])
