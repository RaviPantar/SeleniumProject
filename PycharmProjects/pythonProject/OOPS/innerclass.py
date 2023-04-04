class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 4

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Ravi", 28)
s2 = Student("Raj", 1)

# print(s1.lap.brand)
lap1 = Student.Laptop()
print(lap1)

# print(s1.name, s1.rollno)
# print(s2.name, s2.rollno)

s1.show()
