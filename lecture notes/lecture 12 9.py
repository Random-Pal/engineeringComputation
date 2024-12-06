import matplotlib.pyplot as plt
import numpy as np

sites = ['Site A', 'Site B', 'Site C', ' Site D', 'Site E']
traffic_volume = [2000,3000,2500,1800,3500]
soil_stability = [8,7,6,9,5]
proximity_to_water=[50,30,40,20,45]

plt.scatter(traffic_volume, proximity_to_water, s = sites, alpha = 0.5, c = 'blue', edgecolors = 'black')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('bubble plot example')

plt.show()