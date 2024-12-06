import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', ' Category C',' Category D']
values = [25,40,30,35]

##plt.barh(categories, values, color = 'lightcoral')
plt.bar(categories, values, color = 'lightcoral')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal bar plot example')

plt.show()