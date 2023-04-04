class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")


class Myeditor:

    def execute(self):
        print("=======")
        print("Spell check")
        print("Naming convention")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()


p1 = Pycharm()
e1 = Myeditor()
lap1 = Laptop()
lap1.code(p1)
lap1.code(e1)
