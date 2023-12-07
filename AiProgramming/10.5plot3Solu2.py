# EXERCISE 2.6

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 10)

y1 = 3*x + 4

y2 = 2*x**2 + 1

y3 = x**3 + 9


plt.plot(x, y1, color = 'blue', marker = "s", label='3x+4')
plt.plot(x, y2, color = 'red', marker = "o", label='2x2+1')
plt.plot(x, y3, color = 'green', marker = "p", label='x3+9')
plt.legend()
plt.show()