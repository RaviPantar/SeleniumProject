class Base1(object):
    def __init__(self):
        self.str1 = "Ravi"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Pantar"
        print("Base2")


class child(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

        print("child")

    def printStrings(self):
        print(self.str1, self.str2)


ob = child()
ob.printStrings()
