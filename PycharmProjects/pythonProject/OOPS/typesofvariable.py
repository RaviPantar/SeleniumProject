class car:
    wheels = 4  # class variable

    def __init__(self):
        self.mil = 10  # instance variable
        self.com = "BMW"  # if you change value for one object and does'nt change in other object


c1 = car()
c2 = car()

c1.mil = 6
c1.wheels="6"

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
