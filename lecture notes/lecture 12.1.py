import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x/5) * np.sin(x)

plt.subplot(2,2,1)
plt.scatter(x,y1, color = 'blue', marker = 'o')
plt.title("Subplot 1: Sin(x)")

plt.subplot(2,2,2)
plt.scatter(x,y2, color = 'red', marker = 's')
plt.title("Subplot 2: Cos(x)")

plt.subplot(2,2,3)
plt.scatter(x,y3, color = 'green', marker = '^')
plt.title("Subplot 3: Tan(x)")

plt.subplot(2,2,4)
plt.scatter(x,y4, color = 'purple', marker = 'd')
plt.title('Subplot 4: ex(-x/5) * sin(x)')

plt.tight_layout()
plt.show()