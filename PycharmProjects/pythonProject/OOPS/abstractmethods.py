from abc import ABC, abstractmethod


class Animal(ABC):
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("can walk and run")


class Snake(Animal):
    def move(self):
        print("It can crawel")


class Dog(Animal):
    def move(self):
        print("can bark")


d = Dog()
print(d.move())
s = Snake()
print(s.move())
