import numpy as np
import matplotlib.pyplot as plt
from pandas import Series
from sklearn.preprocessing import MinMaxScaler
data = np.linspace(10, 100, 10)
# print(data)
series = Series(data)
# print(Series(data))
series = np.asarray(series)
print(series)
scaler = MinMaxScaler()
scaledData = scaler.fit_transform(series.reshape(-1, 1))

print("Scaled Data :", scaledData)

def sigmoid(nums):
    return 1 / (1 + np.exp(-nums))

nums = np.linspace(-10, 10, 50)
p = sigmoid(nums)
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.plot(nums, p)
plt.show()

def der_sigmoid(nums):
    return sigmoid(nums) * (1 - sigmoid(nums))
nums = np.linspace(-10, 10, 50)
p = der_sigmoid(nums)
plt.xlabel("x")
plt.ylabel("Derivative of Sigmoid(x)")
plt.plot(nums, p)
plt.show()

def relu(nums):
    return np.maximum(0, nums)
nums = np.linspace(-10, 10, 50)
p = relu(nums)
plt.xlabel("x")
plt.ylabel("ReLU(x)")
plt.plot(nums, p)
plt.show()

def tanh(x):
    return np.tanh(x)
x = np.linspace(-10, 10, 50)
p = tanh(x)
plt.xlabel("x")
plt.ylabel("tanh(x)")
plt.plot(nums, p)
plt.show()

def softmax(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)
x = np.linspace(-10, 10, 50)
p = softmax(x)
plt.xlabel("x")
plt.ylabel("Softmax(x)")
plt.plot(nums, p)
plt.show()