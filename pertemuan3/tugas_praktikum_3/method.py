class Calculator: 
  def add(self, a, b): 
    return a + b 
  def multiply(self, a, b): 
    return a * b 
  
calc = Calculator() 
print(calc.add(6, 7)) 
print(calc.multiply(6, 7)) 
 

#__str__ method
class Person:   
    def __init__(self, name, age): 
        self.name = name     
        self.age = age 
    def __str__(self): 
        return f"{self.name} ({self.age})"  
       
p1 = Person("JohanLiebert", 17) 
print(p1) 
 
 
