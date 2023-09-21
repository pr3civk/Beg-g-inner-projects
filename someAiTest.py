import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.clifford import Axes3D

observations = 1000

xs = np.random.uniform(low=-10, high=10, size=(observations, 1))
zs = xs = np.random.uniform(low=-10, high=10, size=(observations, 1))

inputs = np.column_stack((xs, zs))

noise = np.random.uniform(-1, 1, (observations, 1))


target = 2 * xs - 3 * zs + 5 + noise

print(target.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(xs, zs, target)
ax.set_xlabel("xs")
ax.set_ylabel("zs")
ax.set_zlabel("target")
ax.view_init(azim=100)
target = target.reshape(observations, 1)

init_range = 0.1
weights = np.random.uniform(-init_range, init_range, size=(2, 1))
biases = np.random.uniform(-init_range, init_range, size=1)
learning_rate = 0.02

for i in range(100):
    outputs = np.dot(inputs, weights) + biases
    deltas = outputs - target
    loss = np.sum(deltas**2) / 2 / observations
    print(i, loss)
    deltas_scales = deltas / observations
    weights = weights - learning_rate *np.dot(inputs.T, deltas_scales) 

print(weights, biases)
