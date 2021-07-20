import matplotlib.pyplot as plt

x_values = list(range(1, 101))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.rainbow, edgecolor='none', s=50)

# Set the chart title and labels
plt.title('Cube numbers')
plt.xlabel('Values')
plt.ylabel('Cube of value')

# Set the range for each axis
plt.axis([0, 100, 0, 10201])

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()