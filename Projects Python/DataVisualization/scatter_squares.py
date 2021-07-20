import matplotlib.pyplot as plt

x_values = list(range(1, 101))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=100)

# Set chart title and label axes
plt.title('Square numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set the range for each axis
plt.axis([0, 101, 0, 10201])

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

#plt.savefig('square_plot.png', bbox_inches='tight')
plt.show()