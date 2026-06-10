import pandas as pd

# JAWABAN NO 1
data = {
    "name" : ["Ronaldp", "Messi", "Mbappe", "Neymar"],
    "age" : [40, 38, 25, 34],
    "club" : ["Al Nassr", "Inter Miami", "Real Madrid", "Al Hilal"],
    "goals" : [990, 800, 350, 400]
}

df = pd.DataFrame(data)
print(df)

show_palyer = df[df["age"] < 35]
print(show_palyer)

df_sorted = df.sort_values("age", ascending=True)
print(df_sorted)

print(df[["name", "goals", "club"]]) 



