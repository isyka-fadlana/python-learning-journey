# Class = blueprint/cetakan
class Player:
    def __init__(self, name, age, club, goals):
        self.name = name
        self.age  = age
        self.club = club
        self.goals= goals

    def show_profile(self):
        print(f"Name: {self.name}")
        print(f"Age : {self.age} ")
        print(f"Club: {self.club}")
        print(f"Goals: {self.goals}")

# Object = hasil cetakan dari blueprint
ronaldo = Player ("Ronaldo", 40, "Al Nassr", 900)
messi   = Player ("Messi", 37, "Inter Miami", 800)

ronaldo.show_profile()
print("---")
messi.show_profile()

# Method tambahan dan update data
class Player:
    def __init__(self, name, age, club, goals):
        self.name = name
        self.age  = age
        self.club = club
        self.goals= goals

    def show_profile(self):
        print(f"{self.name} | Age: {self.age} | Club: {self.club} | Goals: {self.goals}")

    def add_goal(self):
        self.goals += 1
        print(f"{self.name} scored! Total goals now: {self.goals}")
    
    def transfer(self, new_club):
        print(f"{self.name} moved from {self.club} to {new_club}")
        self.club = new_club

# Buat object 
mbappe = Player("Mbappe", 25, "Real Madrid", 350)

mbappe.show_profile()
mbappe.add_goal()
mbappe.transfer("PSG")
mbappe.show_profile()   


