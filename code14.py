# importing the required modul
import matplotlib.pyplot as plt

# x axis values
x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# corresponding y axis values
y = [5.948, 6.028, 4.914, 4.926, 3.966, 3.422, 2.91, 2.33, 1.826, 0.994]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('<---Frames Threshold--->')
# naming the y axis
plt.ylabel('<---Delay in seconds--->')

# giving a title to my graph
plt.title('Reducing Delay by reducing Frames')

# function to show the plot
plt.show()
