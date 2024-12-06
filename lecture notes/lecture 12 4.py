import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', ' Category C',' Category D']
values_set1 = [25,40,30,35]
values_set2 = [30,35,20,45]
values_set3 = [20,45,25,30]

plt.subplot(1,3,1)
plt.bar(categories, values_set1, color='skyblue')
plt.title('Bar Chart - Set 1')

plt.subplot(1,3,2)
plt.bar(categories,values_set2, color = "lightcoral")
plt.title("Bar Chart - set 2")

plt.subplot(1,3,3)
plt.bar(categories, values_set3, color = "lightgreen")
plt.title("Bar Chart - set 3")

plt.tight_layout()

plt.show()