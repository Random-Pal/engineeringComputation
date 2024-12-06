import numpy as np
import matplotlib.pyplot as plt

daysOneToFour = np.array([1,2,3,4])
daysFiveTo10 = np.array([5,6,7,8,9,10])
teslaStock = np.array([1000, 1200, 1300,1500])
predictedTeslaStock = 1500 + 150 * daysFiveTo10
asArray = np.array(predictedTeslaStock)

print("The predicted tesla stock for the next 6 days is:\n")
print(predictedTeslaStock)



