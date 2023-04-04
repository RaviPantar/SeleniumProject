class A:
    def __init__(self):
        print("this is A")

    def feature1(self):
        print("Faeture 1 is working")

    def feature2(self):
        print("Faeture 2 is working")


class B:

    def __init__(self):
        print("this is B")
        super().__init__()

    def feature3(self):
        print("Faeture 3 is working")

    def feature4(self):
        print("Faeture 4 is working")


class C(A, B):
    def __init__(self):
        print("This is C")
        super().__init__()  # MRO - Method resloution order # this is c, this is A

    def feat(self):
        super().feature2()



c = C()
c.feat()
