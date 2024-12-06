import matplotlib.pyplot as plt

strain = [0,1,2,3]
stress = [1,100,200,300]

fig, ax = plt.subplots(figsize=(2,5))
fig.set_facecolor('lightgray')

ax.plot(strain, stress ,color='blue',linestyle='--', marker = 'x',markersize = 10, label = 'Stress-Strain Curve')

ax.set_xlabel("Strain")
ax.set_ylabel("Stress")
ax.set_title("Stress-Strain Curve for Material A")
ax.grid(True, linestyle = "--", alpha = 0.6)

ax.set_xticks([0,1,2,3])
ax.set_yticks([1,100,200,300])

ax.legend()

ax.set_xlim(-1,4) # 0 3
ax.set_ylim(1,310) # 0 300

ax.annotate('Yield Point', xy=(1,100), xytext=(0.13,100),arrowprops=dict(arrowstyle='->'))

plt.show()