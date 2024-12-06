import matplotlib.pyplot as plt

x = [0,1,2,3]
y1 = [1, 100,200,300]
y2 = [25,40,50,55]

plt.plot(x, y1, label = "line 1", color = "red", linestyle = 'solid', marker = 'o')
plt.plot(x, y2, label = "line 2", color = "blue", linestyle = 'dotted', marker = "s")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Title of Graph")
plt.grid(True, linestyle = '--', alpha = 1)

plt.legend()

plt.xlim(-1,4)
plt.ylim(1,310)


plt.show()