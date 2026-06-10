import pandas as pd

# JAWABAN NO 1
data = {
    "name" : ["Ronaldo", "Messi", "Mbappe", "Neymar", "Rashford", "Son", "Leao"],
    "age" : [40, 38, 25, 34, 26, 33, 24],
    "club" : ["Al Nassr", "Inter Miami", "Real Madrid", "Al Hilal", "Manchester United", "Tottenham", "Ac Milan"],
    "goals" : [990, 800, 350, 400, 280, 320, 250]
}

df = pd.DataFrame(data)
print(df)

show_top_scorer = df[df["goals"] > 500]
print(show_top_scorer)

show_the_youngest_player = df.sort_values("age", ascending=True)
print(show_the_youngest_player)

print(df[["name", "club"]])

avg_goals = df["goals"].mean()
print(avg_goals)

total_goals = df["goals"].sum()
print(total_goals)


top_scorer_name = df.loc[df["goals"].idxmax(), "name"]
top_scorer_goals = df["goals"].max()
print(f"The Top Scorer is {top_scorer_name}, and he scored {top_scorer_goals} he has.")


youngest_player_name = df.loc[df["age"].idxmin(), "name"]
youngest_player      = df["age"].min()
print(f"and The Youngest Player in The World is {youngest_player_name}, because, his age is {youngest_player}, unbieliveble!!.")

total_player = df["name"].count()
print(total_player)
print(f"Total Best Player in 2026 are {total_player}")
