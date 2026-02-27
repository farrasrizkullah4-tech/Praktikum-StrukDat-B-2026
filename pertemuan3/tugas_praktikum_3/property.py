class Person: 
  species = "Human"  # Class property    

  def __init__(self, name): 
        self.name = name  # Instance/object property 

p1 = Person("Farras") 
p2 = Person("Ataya") 

print(p1.name) 
print(p2.name) 
print(p1.species) 
print(p2.species) 
 
class Person: 
  lastname = "" #sebelum dimofikasi 
  def __init__(self, name): 
    self.name = name 
 
p1 = Person("Farras") 
p2 = Person("Ataya") 
 
Person.lastname = "Uzumaki" #setelah dimodifikasi 
print(p1.lastname) 
print(p2.lastname) 
 
 
