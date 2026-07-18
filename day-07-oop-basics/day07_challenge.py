class Player:
    def __init__(self, name, age, club, goals):
        self.name = name
        self.age  = age
        self.club = club
        self.goals= goals
    
    def show_profile(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"Club: {self.club}")
        print(f"goals: {self.goals}")

    def retire(self):
        self.age +=20
        print(f"{self.name} has retire from football in {self.age} years old.")

    def celebrate_goal(self):
        self.goals += 1
        print(f"Goal !!!{self.club} ! and Score plus one! Now is {self.goals}")


Mbappe = Player ("mbappe", 25, "Real Madrid", 300)
Rasford= Player ("M Rashford", 26, "FC Barcelona", 200)
Lingard= Player ("J Lingard", 23, "Manchester United",300)

Mbappe.show_profile()
Mbappe.retire()
Mbappe.celebrate_goal()


