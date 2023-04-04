x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 5))


def my_fun(n):
    return lambda a: a * n


multiplier = my_fun(2)

print(multiplier(11))


