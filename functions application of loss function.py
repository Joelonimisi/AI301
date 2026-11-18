import numpy as np

def mse(y, y_pred):
	actual = np.array(y)
	predicted = np.array(y_pred)
	result = np.mean((actual - predicted) ** 2)
	return result

def mae(y, y_pred):
	actual = np.array(y)
	predicted = np.array(y_pred)
	result = np.mean(np.abs(actual - predicted))
	return result

def bce(y, p):
	result = -(y * np.log(p) + (1 - y) * np.log(1 - p))
	return result
