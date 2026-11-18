import numpy as np

X = np.array([5, 8])
W = np.array([0.8, 0.5])
b = 1

z = np.dot(X, W) + b
output = np.maximum(0, z)
