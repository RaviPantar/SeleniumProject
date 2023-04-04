class Car:
    wheel = 4
    __Salary = 100
    def __init__(self, color):
        #print("car class constuct")
        self.color = color


    def test(self):
        #print("test method")
        print(Car.__Salary)

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price


c1=Car("Red")
c1.test()
print(c1.setPrice(1000))
print(c1.getPrice())
print(Car.wheel)

#constructor overloding is not possible,it will pick lstest constructor value

#blank class
class pop:
    pass
p1=pop()

