class Player:
    def __init__(self, name, age, club):
        self.name = name
        self.age  = age
        self.club = club

    def show_profile(self):
        print(f"Name = {self.name}")
        print(f"Age  = {self.age}")
        print(f"Club = {self.club}")

# Child class (Class Anak) - mewarisi dari Player
class Goalkeeper (Player):
    def __init__(self, name, age, club, clean_sheets):
        super().__init__(name, age, club)   # panggil __init__ Player dulu
        self.clean_sheets = clean_sheets    # baru tambah atribut baru

    def show_profile(self):
        super().show_profile()                          # Jalankan versi Player dulu
        print(f"Clean Sheets: {self.clean_sheets}")     # tambahan info

    def save_penalty(self):
        print(f"{self.name} saved the penalty! What a save!")

# Buat object dari child class
gk = Goalkeeper ("Alisson", 31, "Liverpool", 15)
gk.show_profile()