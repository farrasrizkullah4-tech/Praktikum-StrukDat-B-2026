class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def greet(self) :
        print("Hello, my name is " + self.name)

p1 = Person("Embege", 99)
p1.greet()

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name
    
    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")

p1 = Person("Mbappe")
p1.welcome()