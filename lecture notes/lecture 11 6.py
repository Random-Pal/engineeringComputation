import matplotlib.pyplot as plt

x = [2,3,4,5,6,7,8,9]
y = [5,6,7,8,9,10,11,12]

plt.scatter (x,y, label="ScatterPlot", color = "blue", marker = 'o', s=100)

plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.title("Scatter Plot with larger markers")

plt.legend()

plt.show()