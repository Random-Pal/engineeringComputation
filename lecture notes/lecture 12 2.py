import matplotlib.pyplot as plt
import numpy as np

##x = np.linspace(0, 10, 100)
time = np.arange(1,7,1)

temperature_A = [25,26,28,30,32,38]
concrete_strength_A=[32,34,35,36,38,37]
productivity_A = [55,54,52,50,49,48]

temperature_B = [20,21,22,24,26,28]
concrete_strength_B=[36,35,34,38,39,40]
productivity_B = [60,58,57,55,53,52]

temperature_C = [22,24,25,26,28,30]
concrete_strength_C=[33,34,36,37,38,39]
productivity_C = [58,57,55,53,51,50]

##temps
plt.subplot(3, 3, 1)
plt.scatter(time, temperature_A, color='blue', marker='o')
plt.title("Temperature A")

plt.subplot(3, 3, 4)
plt.scatter(time, temperature_B, color='red', marker='s')
plt.title("Temperature B")

plt.subplot(3, 3, 7)
plt.scatter(time, temperature_C, color='green', marker='^')
plt.title("Temperature C")

## concrete strength
plt.subplot(3, 3, 2)
plt.scatter(time, concrete_strength_A, color='blue', marker='o')
plt.title("concrete strength A")

plt.subplot(3, 3, 5)
plt.scatter(time, concrete_strength_B, color='red', marker='s')
plt.title("concrete strength B")

plt.subplot(3, 3, 8)
plt.scatter(time, concrete_strength_C, color='green', marker='^')
plt.title("concrete strength C")

## Worker productivity
plt.subplot(3, 3, 3)
plt.scatter(time, productivity_A, color='blue', marker='o')
plt.title("worker producvity A")

plt.subplot(3, 3, 6)
plt.scatter(time, productivity_B, color='red', marker='s')
plt.title("worker producvitiy B")

plt.subplot(3, 3, 9)
plt.scatter(time, productivity_C, color='green', marker='^')
plt.title("worker producvitity C")


plt.tight_layout()
plt.show()