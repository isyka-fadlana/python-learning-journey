import numpy as np

# Array - seperti list tapi jauh lebih cepat untuk matematika
scores = np.array([85, 92, 78, 95, 88])

print(scores)
print(type(scores))

# Operasi matematika langsung ke semua item sekaligus
print(scores + 10) # tambah 10 ke semua nilai
print(scores * 2)  # kali 2 semua nilai
print(scores > 85) # cek mana yang lebih dari 85 → True/False

# Statistik
print(np.sum(scores))       # Total
print(np.mean(scores))      # Rata - rata
print(np.max(scores))       # Nilai tertinggi
print(np.min(scores))       # Nilai terendah

# Array 2D - seperti tabel/matrix
player = np.array([
    [90, 99, 88],   # Ronaldo : speed, shooting, passing
    [88, 92, 95],    # Messi
    [95, 78, 80],    # Mbappe
])

print(player)
print(player.shape)

# Akses data
print(player[0])        # baris pertama - semua stats Ronaldo
print(player[0][1])     # baris 0, kolom - shooting Ronaldo
print(player[:, 0])     # semua baris, kolom 0 - speed semua pemain