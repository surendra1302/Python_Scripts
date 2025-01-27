# Define a class
class Animal:
    # Class attribute (shared by all instances)
    kingdom = "Animalia"

    # Constructor to initialize instance attributes
    def __init__(self, name, species):
        self.name = name  # Instance attribute
        self.species = species  # Instance attribute

    # Instance method
    def make_sound(self, sound):
        return f"{self.name} the {self.species} says {sound}"

# Create objects (instances) of the class
dog = Animal(name="Buddy", species="Dog")
cat = Animal(name="Whiskers", species="Cat")

# Access attributes and methods
print(dog.kingdom)  # Access class attribute: Animalia
print(dog.name)     # Access instance attribute: Buddy
print(dog.make_sound("Woof!"))  # Call instance method

print(cat.make_sound("Meow!"))

