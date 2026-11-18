w = 1.0
learning_rate = 0.1
iterations = 10

for i in range(iterations):
	gradient = 2 * (w - 5)
	w = w - learning_rate * gradient
	loss = (w - 5) ** 2
