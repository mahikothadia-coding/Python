from abc import ABC , abstractmethod

class Animal(ABC):

    def move(self):
        pass

class human(Animal):

    def move(self):
        print("I can walk and run.")

class Snake(Animal):

    def move(self):
        print("I can crawl.")

class Dog(Animal):

    def move(self):
        print("I can bark.")

class Lion(Animal):

    def move(self):
        print("I can roar.")

H = human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()
