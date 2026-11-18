import numpy as np

X = np.array([5, 2])

W1 = np.array([[0.5, 0.2],
			   [0.3, 0.4]
			  ])

B1 = np.array([1, -1])
Z1 = np.dot(X, W1.T) + B2
A1 = np.maximum(0, Z1)

W2 = np.array([[0.4, 0.6],
			   [-0.2, 0.5]
			  ])

B2 = np.array([0.2, 0.1])
Z2 = np.dot(A1, W2.T) + B2
A2 = np.maximum(0, Z2)

W3 = np.array([0.7, -0.4])
B3 = -0.2
Z3 = np.dot(A2, W3) + B3

output = 1 / (1 + np.exp(-Z3))

print("First hidden layer: ", A1)
print("Second hidden layer: ", A2)
print("Final output: ", output)
