import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 10])
ypoints = np.array([0, 500])

plt.plot(xpoints, ypoints)
plt.show()




xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,2,10])

plt.plot(xpoints,ypoints,'o') # This 'o' is for draw graph without line.
plt.show()





# Marker argument is use for mark dots at each points.

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()


# Change marker line width, type, color and size, face and edge color 

ypoints = np.array([2, 7, 1, 9])

plt.plot(ypoints, linestyle = '-' ,c = 'Gold', lw = 3,  marker = 'o', ms = 10, mfc = 'b', mec = 'r')
plt.show()


# also assign multiple line

y1 = np.array([1,3,5,7,9])
y2 = np.array([2,4,6,8,10])

plt.plot(y1)
plt.plot(y2)
plt.show()

#---Sports data----------------------------------------------------------------------------------------------------------------------------------->
# Title, Grids and Labels

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

# Scatter plots----------------------------------------------------------------------------------------------------------------------------------->

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()


# Dots colors, transparescy and size

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()


#------------------------------------------------------------------------------------------------------------------------------------------------->
# Histogram

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

#_________________________________________________________________________________________________________________________________________________>
#Pie chart

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 