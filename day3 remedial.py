# Function - A machine that can be called multiple times = mesin yang bisa dipanggil berkali kali
def sapa(nama):
    print(f"Halo {nama}! selamat datang yaa")

# Call the Function = Panggil fungsinya
sapa("Ronaldo")
sapa("Messi")
sapa("Neymar")

# Function dengan retrun - menghasilkan nilai balik
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

hasil = hitung_luas(5, 3)
print("Luas adalah", hasil)

# Langsung pakai tanpa variabel
print("Luas Lapangan:", hitung_luas(100,45))

# Dictionary - data berpasangan label:nilai
pemain = {
    "name"      :   "Ronaldo",
    "UCL"       :   5,
    "Country"   :   "Portugal",
    "goals"     :   990
}

# Ambil data dengan labelnya
print(pemain["name"])
print(pemain["UCL"])
print(pemain["goals"])

# tambah data baru
pemain["posisi"] = "LW"
print(pemain)

# Loop Dictionary
for label, nilai in pemain.items()  :
    print(label,":", nilai)

# hasil tantangan pertama
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

def show_profile(pemain):
    print("Welcome,",pemain, "! Ready to win!!")

show_profile(striker)
show_profile(winger)

for index, value in striker.items():
    print(index, ":", value)

# Hasil tantangan - namun yang lebih rapih dan efisien
# Dictionary
striker = {
    "name"      :   "Ronaldo",
    "UCL"       :   5,
    "Country"   :   "Portugal",
    "goals"     :   990
}

winger = {
    "name"      :   "Messi",
    "UCL"       :   4,
    "Country"   :   "Argentina",
    "goals"     :   800
}

# Function
def show_profile(pemain) :
    print("--player profile--")
for index, value in pemain.items():
    print(index, ":", value)
print("...")

show_profile(striker)
show_profile(winger)

nama = "Aufa"
umur = 14
tinggi =1.62
asal = "Pituruh"
aktif = True

print(nama)
print(umur)
print(type(umur))   # cek tipe datanya