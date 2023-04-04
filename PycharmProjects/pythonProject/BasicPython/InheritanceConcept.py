class Person(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):

    def isEmployee(self):
        return True


P1 = Person("Ravi")
print(P1.name)
print(P1.getName())
print(P1.isEmployee())

E1 = Employee("Tom")
print(E1.name)
print(E1.getName())
print(E1.isEmployee())
