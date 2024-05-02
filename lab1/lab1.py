import matplotlib.pyplot as plt

x1 = int(input("Enter starting coordinate x1:"))
y1 = int(input("Enter starting coordinate y1:"))
x2 = int(input("Enter terminating coordinate x2:"))
y2 = int(input("Enter terminating coordinate y2:"))

# Plot the points
plt.scatter([x1, x2], [y1, y2])

# Label the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the coordinates next to the points
plt.text(x1, y1, f'({x1}, {y1})',color='black')
plt.text(x2, y2, f'({x2}, {y2})',color='black')

# Show the plot
plt.show()
