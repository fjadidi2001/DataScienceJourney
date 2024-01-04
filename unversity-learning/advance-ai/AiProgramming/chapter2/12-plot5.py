# Import libraries
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 50)

fig = plt.figure(figsize = (14, 8))

# Plot y = cos(x)
y = np.cos(x)
plt.plot(x, y, 'b', label ='cos(x)')

# Plot degree 2 Taylor polynomial
y2 = 1 - x**2 / 2
plt.plot(x, y2, 'r-.', label ='Degree 2')

# Plot degree 4 Taylor polynomial
y4 = 1 - x**2 / 2 + x**4 / 24
plt.plot(x, y4, 'g:', label ='Degree 4')

# Add features to our figure
plt.legend()
plt.grid(True, linestyle =':')
plt.xlim([-6, 6])
plt.ylim([-4, 4])

plt.title('Taylor Polynomials of cos(x) at x = 0')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Show plot
plt.show()
