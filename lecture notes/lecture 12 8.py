import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(30)
y = np.random.rand(30)
sizes = np.random.rand(30) * 500

plt.scatter(x, y, s = sizes, alpha = 0.5, c = 'blue', edgecolors = 'black')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('bubble plot example')

plt.show()