import matplotlib.pyplot as plt

labels = ['Category A', 'Category B', ' Category C',' Category D']
sizes = [30,15,25,30]

plt.pie(sizes, labels = labels, colors = ['skyblue','lightcoral','lightgreen','orange'])

plt.title('Distribution of Categories')

plt.show()