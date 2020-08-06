from random import seed
from random import random
from math import exp
# import matplotlib.pyplot as plt
import numpy as np
 
# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network
 
# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation
 
# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))
 
# Forward propagate input to a network output
def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs
 
# Calculate the derivative of an neuron output
def transfer_derivative(output):
	return output * (1.0 - output)
 
# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])
 
# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']
 
# Train a network for a fixed number of epochs 
def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		if(epoch > 50000):
			l_rate = 1/epoch * 100
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[int(row[-1])] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		if(epoch % 100 == 0):
	  		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
# Make a prediction with a network
def predict(network, row):
	outputs = forward_propagate(network, row)
	return outputs.index(max(outputs))

# Test training backprop algorithm
seed(1)
# dataset = [[1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, -1, 0], [0.5, 0.5, 0], [2, 0, 1], [0, 2, 1], [-2, 0, 1], [0, -2, 1], [1.5, 1.5, 1]]
# testdataset = []
w1 = np.array([[2, 2, 1, 2, 3, 0], [-1, 2, 1, 2, 3, 0], [1, 3, 1, 2, 3, 0], [-1, -1, 1, 2, 3, 0], [0.5, 0.5, 1, 2, 3, 0]])
w2 = np.array([[-1, -3, 1, 2, 3, 1], [0, -1, 1, 2, 3, 1], [1, -2, 1, 2, 3, 1], [-1, -2, 1, 2, 3, 1], [0, -2, 1, 2, 3, 1]])
dataset = np.concatenate([w1, w2], axis = 0)
w1 = np.array([[2, 2], [-1, 2], [1, 3], [-1, -1], [0.5, 0.5]])
w2 = np.array([[-1, -3], [0, -1], [1, -2], [-1, -2], [0, -2]])
# f, ax = plt.subplots(figsize=(7, 7))
# c1, c2, c3 = 'b', 'r', 'm'

# ax.scatter(*w1.T, c=c1,s = 10, label = "w1")
# ax.legend()
# ax.scatter(*w2.T, c=c2, s = 10, label = "w2")
# ax.legend()

n_inputs = len(dataset[0]) - 1
n_outputs = len(set([row[-1] for row in dataset]))
# network = [[{'weights': [-5.001747131203413, 3.540563135832001, 3.190410054416532], 'output': 0.7307902188673295, 'delta': -5.264459015387324e-07}, {'weights': [-3.417548603196333, 6.567745252006245, -1.9613880473925358], 'output': 0.9406939504125481, 'delta': 1.4373075423209061e-07}] ,[{'weights': [35.23255346924898, -33.92159698092517, -2.380639707318204], 'output': 0.00019489099053415375, 'delta': -3.797509574468813e-08}, {'weights': [-35.232584862365144, 33.92162706419902, 2.3806412561899664], 'output': 0.9998051103551635, 'delta': 3.7974571371136876e-08}]]
network = [[{'weights': [-4.261090022817013, 2.6206089965654455, 2.535633894218433], 'output': 0.518952539484332, 'delta': -0.16984235868390052}, {'weights': [-2.631283795544046, 4.293822470761023, -2.593748072333557], 'output': 0.47480234865358517, 'delta': 0.1701804160579965}], [{'weights': [34.6913195024511, -34.7988140311546, -3.6271857920593997], 'output': 0.10465110949633696, 'delta': -0.009805730971447697}, {'weights': [-34.691349759717625, 34.798844391721204, 3.627188708721416], 'output': 0.8953490432226047, 'delta': 0.009805704024717319}]]
network = initialize_network(n_inputs, 4, n_outputs)
print(network)
train_network(network, dataset, 0.5, 1000, n_outputs)
print(network)
x = np.arange(-3.5, 3.5, 0.1)
y = np.arange(-3.5, 3.5, 0.1)
# print(predict(network, [0, -2]))
# for layer in network:
# 	print(layer)

# for x in dataset:
# 	print("Expected value is ", x[-1], " but got ", predict(network, x))

# for i in range(len(x)):
# 	for j in range(len(y)):
# 		pt = [x[i], y[j]]
# 		if(predict(network, pt) == 0):
# 			c = 'r'
# 		else:
# 			c = 'b'
# 		ax.scatter(x[i], y[j], c = c, s = 1)



# plt.show()





# [[{'weights': [-4.669793531287468, 2.8229868659401065, 2.8356003853379916], 'output': 0.5166641660813545, 'delta': -0.17603952314821486}, {'weights': [-2.874258045215757, 4.743443250285333, -2.864214447196347], 'output': 0.4845746861825886, 'delta': 0.17511609478564205}], [{'weights': [34.76895228355128, -34.58107758565242, -3.333589786991384], 'output': 0.10651796518180176, 'delta': -0.010137515881597952}, {'weights': [-34.768982849013824, 34.581107993199765, 
# 3.333592427724464], 'output': 0.8934821855166596, 'delta': 0.010137488906935483}]]


