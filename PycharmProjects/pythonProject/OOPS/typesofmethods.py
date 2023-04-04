class Student:
    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # instance methods bcoz we are passing self,its belongs to particular object
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):  # Accessor
        return self.m1

    def set_m1(self, value):  # mutator
        self.m1 = value

    @classmethod  # class methods
    def info(clss):
        return clss.school

    @staticmethod
    def schoolinformation():  # static Methods
        print("")


s1 = Student(34, 67, 32)
s2 = Student(80, 32, 12)

print(s1.avg())
print(Student.info())
print(s1.get_m1())
