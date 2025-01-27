class Animal:
    kingdom = "Animalia"
    def __init__(self, name, species):
        self.name = name 
        self.species = species 

dog = Animal(name="Buddy", species="Dog")
cat = Animal(name="Whiskers", species="Cat")

print(dog.kingdom)  
print(dog.name)    
print(cat.name)

