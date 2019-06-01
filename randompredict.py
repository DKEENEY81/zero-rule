##predict random outcome as observed in training data
from random import randrange
from random import seed

def random_algo(train, test):
	output_values = [row[-1] for row in train]
	unique = list(set(output_values))
	predicted = list()
	for row in test:
		index = randrange(len(unique))
		predicted.append(unique[index])
	return predicted

seed(2)

train = [[0], [1], [0], [1], [0], [1]]
test = [[None], [None], [None], [None]]

predictions = random_algo(train, test)
print(predictions)