import numpy as np

players = np.array([
    [90, 95, 97],    # Mesii ; speed, shooting, passing
    [95, 99, 93],    # CR7; speed, shooting, passing
    [92, 85, 90]     # Neymar
])

print(players[0])
print(players[:,2])

average_shoot = np.mean(players[:,1])
print(average_shoot)

average_speed = np.max(players[:,0])
print(average_speed)

