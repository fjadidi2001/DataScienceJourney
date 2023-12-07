# EXERCISE 2.6

import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return 3*x + 4

def func2(x):
    return 2*x**2 + 1

def func3(x):
    return x**3 + 9

x = np.linspace(-10, 10, 50)

plt.plot(x, func1(x), color = 'blue', marker = "s", label='3x+4')
plt.plot(x, func2(x), color = 'red', marker = "o", label='2x2+1')
plt.plot(x, func3(x), color = 'green', marker = "d", label='x3+9')
plt.legend()
plt.show()