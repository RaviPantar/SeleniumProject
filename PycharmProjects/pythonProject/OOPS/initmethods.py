class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print("This is init")

    def config(self):
        print("i5,16gb,ITB", self.cpu, self.ram)


com1 = Computer('i5', 16)
com2 = Computer('i3', 24)

com1.config()
com2.config()
