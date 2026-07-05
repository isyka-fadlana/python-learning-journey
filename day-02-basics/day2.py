# variable - seperti kotak berlabel untuk menyimpan sesuatu
nama = "Aufa"
umur = 14
tinggi =1.62
asal = "Pituruh"
aktif = True

print(nama)
print(umur)
print(type(umur))   # cek tipe datanya

# Staring operations
print("Halo, nama saya " + nama)
print("Saya berasal dari " + asal)
print(f"Umur saya {umur} tahun")    # f-string - cara modern
print(f"umur saya 10 tahun yang akan datang adalah {umur + 10} tahun")

# Operasi dasar
print(umur + 2)
print(tinggi * 100)

# List - seperti daftar belanja
skills = ["Python", "Git", "Docker"]
print("My first skill is", skills[0])        # ambil item pertama
print(len(skills))                           # hitung isi list

skills.append("FastAPI")    # tambah item baru
print(skills)

# Loop - lakukan sesuatu berulang
for skill in skills:
    print("Saya sedang belajar:", skill)

# if/else - pengambilan keputusan
nilai = 60
if nilai > 85:
    print("Lulus dengan baik!")
elif nilai > 75:
    print("Lulus biasa aja")
else: 
    print("Belajar lagi ya kids")
