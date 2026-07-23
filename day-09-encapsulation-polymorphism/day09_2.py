class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a sound")
    
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says : Woof!")
    
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")

# Polymorphism dalam aksi:
animals = [Dog("Rex"), Cat("Buthem"), Animal("Generic")]

for animal in animals:
    animal.make_sound()
        