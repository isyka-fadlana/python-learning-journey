# Function - A machine that can be called multiple times = mesin yang bisa dipanggi berkali kali
def sapa(nama):
    print("Halo,", nama, "! selamat datang.")

# Call the Function = Panggil fungsinya
sapa("Ronaldo")
sapa("Messi")
sapa("Neymar")

# Function dengan return - menghasilkan nilai balik
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

hasil = hitung_luas(5, 3)
print("Luasnya adalah", hasil)
 
# Langsung pakai tanpa variabel
print("Luas Lapangan:", hitung_luas(100,45))

# Dictionary - data berpasangan label:nilai
pemain = {
    "name"  : "CR7",
    "age"   : 41,
    "club"  : "Al Nassr",
    "goals" : 990
}

# Ambil data dengan labelnya
print(pemain["name"])
print(pemain["age"])
print(pemain["goals"])

# tambah data baru
pemain["posisi"] = "LW"
print(pemain)

# Loop Dictionary
for label, nilai in pemain.items() :
    print(label,":", nilai)

# Hasil Tantangan pertama
striker = {
    "nama": "Ronaldo",
    "umur": 39,
    "klub": "Al Nassr",
    "gol": 900
}

winger = {
    "nama": "Messi",
    "umur": 39,
    "klub": "Inter Miami",
    "gol": 800
}

def tampilkan_profil(pemain):
    print("Welcome,", pemain, "! Ready to win!.")

tampilkan_profil(striker)
tampilkan_profil(winger)

for label, nilai in striker.items():
    print(label, ":", nilai)

# Hasil tantangan - namun yang lebih rapih dan efisien
# Dictionary
striker = {
    "nama"  : "Ronaldo",
    "umur"  :   40,
    "klub"  :   "Al-Nassr",
    "gol"   :   800
}

winger = {
    "nama": "Messi",
    "umur": 39,
    "klub": "Inter Miami",
    "gol": 800
}

# Function

def tampilkan_profil(pemain) :
    print("=== Profil Pemain ===")
    for label, nilai in pemain.items():
        print(label, ":", nilai)
    print("---")

tampilkan_profil(striker)
tampilkan_profil(winger)