class Computer:
    def config(self):
        print("i5", "16Gb", "1TB")


comp1 = Computer()
print(type(comp1))
print(id(comp1))

Computer.config(comp1)
comp1.config()