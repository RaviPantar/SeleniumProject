class Base(object):
    def __init__(self, x):
        self.x = x


class Child(Base):

    def __init__(self, x, y):
        Base.x = x
        self.y = y

    def printWorks(self):
        print(Base.x, self.y)


ob = Child(10, 20)
ob.printWorks()
