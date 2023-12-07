#Example 2.14
import matplotlib.pyplot as plt
import numpy as np
x = [i for i in range(100)]
x = np.array(x)
x = 2 * np.pi* x * 0.01
y = np.sin(x)
plt.plot(x,y)
plt.title('Sin Plot')
plt.xlabel('x')
plt.ylabel('Sin')
plt.show()