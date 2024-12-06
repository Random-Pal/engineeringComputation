import matplotlib.pyplot as plt

time_intervals=['3 Days', '7 Days', '14 Days', '28 Days']
mix_A_Strength = [25,4,50,60]
mix_B_Strength = [30,45,55,66]
mix_C_Strength = [20,35,45,55]

plt.subplot(1,3,1)
plt.bar(time_intervals, mix_A_Strength, color='skyblue')
plt.xlabel("Time")
plt.ylabel("Mix A MPa")
plt.title('Bar Chart - Set 1')

plt.subplot(1,3,2)
plt.bar(time_intervals,mix_B_Strength, color = "lightcoral")
plt.xlabel("Time")
plt.ylabel("Mix A MPa")
plt.title("Bar Chart - set 2")

plt.subplot(1,3,3)
plt.bar(time_intervals, mix_C_Strength, color = "lightgreen")
plt.xlabel("Time")
plt.ylabel("Mix A MPa")
plt.title("Bar Chart - set 3")

plt.tight_layout()
plt.show()