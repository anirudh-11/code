from random import seed
from random import random
from math import exp
import matplotlib.pyplot as plt
import numpy as np
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

# Initialize a network
def initialize_network(n_inputs, n_hidden_layer, n_hidden, n_outputs):
	network = list()
	for i in range(n_hidden_layer):
		if(i == 0):
		    hidden_layer = [{'weights':np.array([random() for i in range(n_inputs + 1)])} for i in range(n_hidden[0])]
		else:
		    hidden_layer = [{'weights':np.array([random() for i in range(n_hidden[i - 1] + 1)])} for i in range(n_hidden[i])]
		network.append(hidden_layer)
		print(1)
	output_layer = [{'weights':np.array([random() for i in range(n_hidden[-1] + 1)])} for i in range(n_outputs)]
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
	return (activation > 0) * activation + (activation < 0) * 0.01*activation

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
	return (output > 0) + (output < 0) * 0.01

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
		# if(epoch > 50000):
		# 	l_rate = (1/epoch)* 1000
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[int(row[-1])] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		if(epoch % 100 == 0):
	  		print('>epoch=%d, lrate=%.4f, error=%.4f' % (epoch, l_rate, sum_error))


# Make a prediction with a network
def predict(network, row):
	outputs = forward_propagate(network, row)
	return outputs.index(max(outputs))

# Test training backprop algorithm

w1 = np.array([[2, 2, 0], [-1, 0.8, 0], [1, 0.5, 0], [2, 3, 0], [-2, 2.5, 0]])
w2 = np.array([[-1, 0, 1], [0, -1, 1], [2, 1, 1], [-1, -2, 1], [0, -2, 1]])
dataset = np.concatenate([w1, w2], axis = 0)
w1 = np.array([[2, 2], [-1, 0.8], [1, 0.5], [2, 3], [-2, 2.5]])
w2 = np.array([[-1, 0], [0, -1], [2, 1], [-1, -2], [0, -2]])

w1 = np.array([[0, 0, 0], [0, 1, 0], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [0.5, 0.5, 0], [0.5, -0.5, 0], [-0.5, 0.5, 0], [-0.5, -0.5, 0]])
w2 = np.array([[0, 2, 1], [0, -2, 1], [2, 1, 1], [-2, 0, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1]])
dataset = np.concatenate([w1, w2], axis = 0)
w1 = np.array([[1, 0], [0, 0], [0, 1], [-1, 0], [0, -1], [0.5, 0.5], [0.5, -0.5], [-0.5, 0.5], [-0.5, -0.5]])
w2 = np.array([[2, 0], [0, 2], [-2, 0], [0, -2], [1, 1], [1, -1], [-1, 1], [-1, -1]])

f, ax = plt.subplots(figsize=(7, 7))
c1, c2, c3 = 'b', 'r', 'm'

ax.scatter(*w1.T, c=c1,s = 10, label = "w1")
ax.legend()
ax.scatter(*w2.T, c=c2, s = 10, label = "w2")
ax.legend()

n_inputs = len(dataset[0]) - 1
n_outputs = len(set([row[-1] for row in dataset]))
network = initialize_network(n_inputs, 4, [n_inputs, n_inputs, n_inputs, n_inputs], n_outputs)
print(network)
train_network(network, dataset, 0.0005, 20000, n_outputs)
print(network)

x = np.arange(-2.5, 2.5, 0.1)
y = np.arange(-2.5, 2.5, 0.1)

winsound.Beep(frequency, duration)
for i in range(len(x)):
	for j in range(len(y)):
		pt = [x[i], y[j]]
		if(predict(network, pt) == 0):
			c = 'r'
		else:
			c = 'b'
		ax.scatter(x[i], y[j], c = c, s = 1)

winsound.Beep(frequency, duration)
plt.show()

# [[{'weights': array([1.72938324, 0.91130803, 0.81806938]), 'output': -0.018226215056494476, 'delta': -0.00012852410566686686}, {'weights': array([1.14716318, 1.14873416, 1.60102822]), 'output': -0.00694869519523726, 'delta': 0.0001326652211401261}], [{'weights': array([-1.39639018,  1.59624787, -1.03620368]), 'output': -0.010218445153515594, 'delta': -9.391573019788626e-05}, {'weights': array([ 1.33240103, -1.37682402,  1.47973591]), 'output': 1.465028161085409, 'delta': -0.0097444800912981}], [{'weights': array([-1.56870797, -1.6566937 ,  2.40589318]), 'output': -5.1799979318261084e-05, 'delta': 5.179997931826108e-07}, {'weights': array([ 1.74973069, 
#  1.81546958, -1.63648445]), 'output': 1.005366974921091, 'delta': -0.00536697492109095}]]