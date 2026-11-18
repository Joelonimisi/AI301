import numpy as np

X = np.array([3, 4])

W1 = np.arry([0.5, 0.2])
b1 = 1

W2 = np.array([0.3, 0.4])
b2 = -1

z1 = np.dot(X, W1) + b1
z2 = np.dot(X, W2) + b2

a1 = np.maximum(0, z1)
a2 = np.maximum(0, z2)

hidden_output = np.array([a1, a2])
print(hidden_output)