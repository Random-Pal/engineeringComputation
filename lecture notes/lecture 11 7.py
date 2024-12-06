import matplotlib.pyplot as plt

diameter = [2.3,2.5,2.7,3.0,3.2,3.4]
weight = [7.2,7.5,7.8,8.0,8.2,8.4]

plt.scatter (diameter,weight, label="Bolts", color = "blue", marker = 'o', s=50)

plt.xlabel("Diameter")
plt.ylabel("Weight")
plt.title("Bolt Quality Control")

plt.legend()

plt.show()