import numpy as np

stats = np.array([
    [95, 99, 90, 90],       # Ronaldo; speed, shooting, passing, stamina
    [90, 99, 95, 90],       # Messi
    [95, 90, 95, 90]        # Neymar
])

print(stats[1])
print(stats[:,3])

avg_pass = np.mean(stats[:,2])
print(avg_pass)

max_shoot = np.max(stats[:,1])
print(max_shoot)

