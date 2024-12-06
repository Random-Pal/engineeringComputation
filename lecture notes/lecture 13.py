import numpy as np
import matplotlib.pyplot as plt

input = [100,200,300,400,500,600]
output = np.exp(input) #or npfloat_power(inputs,10)
print(output)

mean = np.mean(output)
std = np.std(output)
#median
#sum = np.sum(output)
print(mean, std, sum)

plt.scatter(input,output)
plt.show()

##on exam, wants x, y axis, etc.