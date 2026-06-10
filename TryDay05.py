import numpy as np
scores = np.array([90, 95, 99, 98, 97])

print(scores)
print(scores + 5)
print(np.max(scores))
print(np.min(scores))
print(np.mean(scores))

print(scores[scores > 80])