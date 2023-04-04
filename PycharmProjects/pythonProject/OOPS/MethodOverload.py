class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a, b):
        s = a + b
        return s

    def sum(self, a, b, c):
        s = a + b + c
        return s


s3 = Student(58, 29)
print(s3.sum(5, 9, 3))
print(s3.sum(5, 9))            #Method Overload not supported,bcoz python always pick up latest defined method

