#Example 2.14
import matplotlib.pyplot as plt
import numpy as np
x = [i for i in range(100)] # creates an array of 100 numbers called x
x = np.array(x) # converts x to a Numpy array
x = 2 * np.pi* x * 0.01 # scales x between 0 and 2 π, with a step size of 0.01
y = np.sin(x) # calculates the sine value of the array x
plt.plot(x,y) # plot the sine curve 
plt.title('Sin Plot') 
plt.xlabel('x')
plt.ylabel('Sin')
plt.show() # show the plot