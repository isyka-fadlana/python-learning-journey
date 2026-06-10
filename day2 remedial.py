Nama = "Ken"
umur = 14
hobi = "Basket"
berat_badan = 40


print(Nama)
print(hobi)
print(type(umur))
print(f"Haloo!! kenalin guys.. nama aku {Nama}. salam kenal yaaa")
print(f"hobi aku itu bermain {hobi}")
print(f"umur aku sekarang {umur} tahun")
print(f"umur aku 23 tahun yang akan datang adalah {umur + 23} tahun")\

print(berat_badan)
print(berat_badan * 100)

extracurriculars = ["Basket", "Futsal", "Badminton"]
print(f"my first extra is", extracurriculars[0])
print(len(extracurriculars))

extracurriculars.extend(["Voli", "Swimming"])
print(extracurriculars)
print(len(extracurriculars))

for extracurricular in extracurriculars:
    print("saya sedang bermain", extracurricular)

for index, extracurricular in enumerate(extracurriculars):
    print(f"extra {index}: {extracurricular}")

# Condition - if / elif /  else
score = 46
if score > 90:
    print("Amazingg!")
elif score >75 :
    print("good job")
else:
    print("don't give up")