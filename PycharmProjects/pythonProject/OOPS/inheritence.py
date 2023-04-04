class A:
    def feature1(self):
        print("Faeture 1 is working")

    def feature2(self):
        print("Faeture 2 is working")


class B:
    def feature3(self):
        print("Faeture 3 is working")

    def feature4(self):
        print("Faeture 4 is working")


class C(A, B):
    def feature5(self):
        print("Faeture 5 is working")


a = A()
a.feature2()





b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()


c = C()
c.feature4()
c.feature3()
c.feature2()
c.feature1()
c.feature5()
