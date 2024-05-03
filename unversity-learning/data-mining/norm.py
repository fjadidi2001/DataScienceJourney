import numpy as np
# create u
u = np.array([1,6])
print('u is',u)
# create v
v = np.array([4,2])
print('v is',v)
print('sum u+v is:')
print(u+v)
'''
"linalg" is an abbreviation for "linear algebra,"
which is a branch of mathematics that deals with vectors, vector spaces, linear transformations, and systems of linear equations.
It is commonly used in various fields such as physics, engineering, computer science, and economics.
'''


print('norm u+v is:',np.linalg.norm(u+v))
print(np.linalg.norm(u)+np.linalg.norm(v))

