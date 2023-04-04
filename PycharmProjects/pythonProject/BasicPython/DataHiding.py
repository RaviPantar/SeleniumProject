class Employee:
    # hidden data member pr private variable of class
    __salary = 100

    def hello(self):
        print("my salary is", Employee.__salary)


e1 = Employee()
#e1.hello()
#print(e1.__salary)  # this is not right to access private variable
print(e1._Employee__salary)
e1.hello()

