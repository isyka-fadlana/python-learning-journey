import pandas as pd

# Buat data pemain - seperti tabel excel
data = {
    "name" : ["Ronaldp", "Messi", "Mbappe", "Neymar"],
    "age" : [40, 38, 25, 34],
    "club" : ["Al Nassr", "Inter Miami", "Real Madrid", "Al Hilal"],
    "goals" : [990, 800, 350, 400]
}

# Ubah dictionary jadi DataFrame (tabel)
df = pd.DataFrame(data)
print(df)

# Lihat info tabel
print(df.shape)     # berapa baris & kolom?
print(df.columns)   # nama - nama kolom
print(df.dtypes)    # tipe data tiap kolom

# Ambil satu kolom
print(df["name"])
print(df["goals"])
print(df["club"])

# Filter - pemain dengan gol lebih dari 500
top_scorers = df[df["goals"] > 500]
print(top_scorers)

# Urutkan berdasarkan gol - dari terbesar
df_sorted = df.sort_values("goals", ascending=False)
print(df_sorted)