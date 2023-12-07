# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating vectors X and Y
x = np.linspace(-2, 2, 100)
y = x ** 2

fig = plt.figure(figsize = (12, 7))
# Create the plot
plt.plot(x, y, alpha = 0.4, label ='Y = X²',
		color ='red', linestyle ='dashed',
		linewidth = 2, marker ='D', 
		markersize = 5, markerfacecolor ='blue',
		markeredgecolor ='blue')

# Add a title
plt.title('Equation plot')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add Text watermark
fig.text(0.9, 0.15, 'Fateme-Jadidi', 
		fontsize = 12, color ='green',
		ha ='right', va ='bottom', 
		alpha = 0.7)

# Add a grid
plt.grid(alpha =.6, linestyle ='--')

# Add a Legend
plt.legend()

# Show the plot
plt.show()
