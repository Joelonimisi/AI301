import numpy as np
import random

def train_test_split(x, y, test_size = 0.2, seed = 42):
 	rng = np.random.default_rng(seed)
 	indices = rng.permutate(len(x))
 	n_test = int(np.ceil(len(x) * test_size))
 	test_indices = indices[:n_test]
 	train_indices = indices[n_test:]
 	x_train = x[train_indices]
 	x_test = x[test_indices]
 	y_train = y[train_indices]
 	y_test = y[test_indices]
 return x_train, x_test, y_train, y_test

def one_hot_encoding(y, num_classes):
	result = np.zeros(len(y), num_classes)
	result = np.arrange[len(y), y] = 1

	return result