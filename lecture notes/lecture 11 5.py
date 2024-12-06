import matplotlib.pyplot as plt

time = [0,1,2,3,4,5,6,7,8,9,10]
temp_sensor_A = [300,305,310,312,315,318,320,322,324,326,328]
temp_sensor_B = [298,303,308,310,313,315,316,318,320,322,325]

plt.plot(time, temp_sensor_A, label = "Sensor A", color = "blue", linestyle = 'solid', marker = 'o')
plt.plot(time, temp_sensor_B, label = "Sensor B", color = "red", linestyle = 'dashed', marker = 's')

plt.xlabel("Time (min) ")
plt.ylabel("Temperature(C)")
plt.title("Sensor Data Over Time")
plt.grid(True, linestyle = '--', alpha = 0.6)

plt.legend()

##plt.annotate("Sensor Spike A")

##plt.xlim(-1,4)
##plt.ylim(1,310)


plt.show()