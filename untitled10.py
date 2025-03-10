# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JQbgcBIFyUMMeDPXF8_2clw66OOLP4GH
"""



def tanh(x):
    return np.tanh(x)

input_size = 2
hidden_size = 2
output_size = 1

np.random.seed(42)
W1 = np.random.uniform(-0.5, 0.5, (hidden_size, input_size))
W2 = np.random.uniform(-0.5, 0.5, (output_size, hidden_size))

b1 = np.array([0.5, 0.5])
b2 = np.array([0.7])

X = np.array([0.3, -0.2])

hidden_input = np.dot(W1, X) + b1
hidden_output = tanh(hidden_input)

output_input = np.dot(W2, hidden_output) + b2
output = tanh(output_input)

print("Output of the network:", output)