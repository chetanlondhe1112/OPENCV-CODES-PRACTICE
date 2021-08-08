# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# corresponding y axis values
y = [0.48, 1.03, 1.56, 2.67, 3.97, 4.93, 7.18, 9.93, 11.20, 12.30]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('<---Distance in cm--->')
# naming the y axis
plt.ylabel('<---Time for detection in seconds--->')

# giving a title to my graph
plt.title('Alcohol Detection')

# function to show the plot
plt.show()
