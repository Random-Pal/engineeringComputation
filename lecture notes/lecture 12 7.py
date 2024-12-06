import matplotlib.pyplot as plt

project_phases = ['Design', 'Team', 'Implementation', 'Documentation']
time_allocation = [20,15,30,10]

plt.pie(time_allocation, labels = project_phases, colors = ['green', 'blue', 'purple', 'orange'] )
plt.title("Time Allocated")
plt.show()