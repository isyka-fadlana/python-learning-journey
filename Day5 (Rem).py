import numpy as np

# Array - seperti list tapi jauh lebih cepat untuk matematika
scores = np.array([50, 60, 70, 80])
print(scores)
print(type(scores))

print(scores + 10)
print(scores * 100)
print(scores > 65)

print(np.sum(scores))
print(np.mean(scores))
print(np.max(scores))
print(np.min(scores))

students = np.array([
    [80, 90, 95],       # Arhan : mtk, ipa, ips
    [78, 80, 75],       # Marcel
    [90, 80, 50]        # Bened   
])

print(students)
print(students.shape)

# akses data
print(students[0])
print(students[1][2])
print(students[:, 0])



