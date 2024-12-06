import numpy as np
import matplotlib.pyplot as plt

slope = 500
flightTimes = [5,10,20,30]
bValue = 100
##velocity = np.multiply(flightTimes, slope) + bValue
velocity = np.add(bValue, np.multiply(slope,flightTimes))

plt.plot(flightTimes,velocity)
plt.xlabel("Time")
plt.ylabel("Velocities")
plt.title("TITLE")
##include title on exam
plt.grid(True, linestyle = '--', alpha =1)
plt.show()
