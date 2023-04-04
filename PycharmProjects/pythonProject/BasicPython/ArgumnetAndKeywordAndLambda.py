def login(username, password):
    print(username, password)


login("naveen", "test123")

login(username="ravi", password="Pantar")


# *args
def getMarks(*arg):
    for x in arg:
        print(x)


getMarks(10, 20, 30, 40)
getMarks("A", "B", "C", "D")


# keyword args:
# **arg
def getStudentMarks(**arg):
    for key, value in arg.items():
        print("%s== %s" % (key, value))


getStudentMarks(naveen=10, Ravi=20, Tom=40)

cube = lambda x: x * x * x
print(cube(4))
total = lambda marks: marks + 30
print(total(10))


def getStudent(**kwarg):
    for key, values in kwarg.items():
        print("%s==%s" % (key, values))


getStudent(naveen=10, arvi=20, tom=30)

cube = lambda x: x * x * x
print(cube(10))

total=lambda marks:marks+30
print(total(30))