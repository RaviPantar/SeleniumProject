def test():
    print("Hello world")


test()


def abc(a):
    print(a + 10)


abc(10)


def country(name="India"):
    print(name)


country()
country("UK")


# pass list to a function
def city(list):
    for i in list:
        print(i)


list = ["My", "Name", "is", "ravi"]
city(list)


def capitalname(countryname):
    if countryname == "india":
        return "new delhi"


print(capitalname("india"))


# Recursion in python
def fact(num):
    if num > 1:
        num = num * fact(num - 1)
    return num


print(fact(4))


def login(usernmae, password):
    print("login with %s and %s" % (usernmae, password))


login("Ravi", "Pantar")
