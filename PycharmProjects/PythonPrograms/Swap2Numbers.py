# num1 = 10
# num2 = 20

num1 = input("Enter number value:")
num2 = input("Enter number value:")

print("Before swaping num1", num1)
print("Before swaping num2", num2)

# Aproach1
# temp = num1
# num1 = num2
# num2 = temp

# Approach2
num1, num2 = num2, num1

print("After swaping num1", num1)
print("After swaping num2", num2)
