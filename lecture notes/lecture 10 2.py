## mistake, didn't use all resistance values as array, just added them from get go. so, make array of 10, 20,30 ohms
## also, used wrong equations
import numpy as np
voltage = 12
resistanceTotal = 60
power = np.divide(voltage**2, resistanceTotal)
print("Power is ", power)
current = np.divide(power,voltage)
print("Current is ", current)